#!/usr/bin/env python3

"""Stuff that doesn't go anywhere else
"""

import asyncio
import logging
import os
import signal
import sys
import time
import traceback
from collections.abc import AsyncIterator, Callable, Coroutine, Iterator
from functools import wraps
from pathlib import Path
from typing import NoReturn, cast

from asyncinotify import Event, Inotify, Mask


def log() -> logging.Logger:
    """Logger for this module"""
    return logging.getLogger("medit.misc")


def watchdog(
    afunc: Callable[..., Coroutine[object, object, object]]
) -> Callable[..., Coroutine[object, object, object]]:
    """Watch for async functions to throw an unhandled exception"""

    @wraps(afunc)
    async def run(*args: object, **kwargs: object) -> object:
        """Run wrapped function and handle exceptions"""
        try:
            return await afunc(*args, **kwargs)
        except asyncio.CancelledError:
            log().info("Task cancelled: `%s`", afunc.__name__)
        except KeyboardInterrupt:
            log().info("KeyboardInterrupt in `%s`", afunc.__name__)
        except Exception:  # pylint: disable=broad-except
            log().exception("Exception in `%s`:", afunc.__name__)
            asyncio.get_event_loop().stop()
        return None

    return run


def impatient(func):
    @wraps(func)
    def run(*args: object, **kwargs: object) -> object:
        try:
            t1 = time.time()
            return func(*args, **kwargs)
        finally:
            if (duration := time.time() - t1) > 0.1:
                log().warn("%s took %.2fs!", func.__name__, duration)

    return run


async def fs_changes(
    *paths: Path,
    queue: asyncio.Queue[str] = asyncio.Queue(),
    mask: Mask = Mask.CLOSE_WRITE
    | Mask.MOVED_TO
    | Mask.CREATE
    | Mask.MODIFY
    | Mask.MOVE
    | Mask.DELETE
    | Mask.MOVE_SELF,
    postpone: bool = False,
    timeout: float = 2,
) -> AsyncIterator[Path]:
    """Controllable, timed filesystem watcher"""

    # pylint: disable=too-many-locals

    async def fuse_fn(queue: asyncio.Queue[str], timeout: float) -> None:
        await asyncio.sleep(timeout)
        await queue.put("timeout")

    def expand_paths(path: Path, recursive: bool = True) -> Iterator[Path]:
        yield path
        if path.is_dir() and recursive:
            for file_or_directory in path.rglob("*"):
                name = file_or_directory.name
                if file_or_directory.is_dir() and all(
                    p not in file_or_directory.absolute().as_posix()
                    for p in {
                        "/.venv",
                        "/.git",
                        "/dist",
                        "/__pycache__",
                    }
                ):
                    yield file_or_directory

    def task(name: str) -> asyncio.Task[str | Event]:
        """Creates a task from a name identifying a data source to read from"""
        return asyncio.create_task(
            cast(asyncio.Queue[str] | Inotify, {"inotify": inotify, "mqueue": queue}[name]).get(),
            name=name,
        )

    with Inotify() as inotify:
        for path in set(sub_path.absolute() for p in paths for sub_path in expand_paths(Path(p))):
            log().debug("add fs watch for %s", path)
            inotify.add_watch(path, mask)
        fuse = None
        changed_files = set()
        tasks = set(map(task, ("inotify", "mqueue")))

        while True:
            done, tasks = await asyncio.wait(
                fs=tasks,
                return_when=asyncio.FIRST_COMPLETED,
            )
            for event in done:
                event_type, event_value = event.get_name(), event.result()
                tasks.add(task(event_type))
                if event_type == "inotify":
                    assert isinstance(event_value, Event)
                    if event_value.path:
                        changed_files.add(event_value.path)
                    if postpone and fuse:
                        fuse.cancel()
                        del fuse
                        fuse = None
                    if not fuse:
                        fuse = asyncio.create_task(fuse_fn(queue, timeout))
                elif event_type == "mqueue":
                    if event_value == "timeout":
                        del fuse
                        fuse = None
                        for file in changed_files:
                            yield file
                        changed_files.clear()


def setup_logging(level: str | int = logging.DEBUG) -> None:
    '''
    def thread_id_filter(record):
        """Inject thread_id to log records"""
        record.thread_id = threading.get_native_id()
        return record

    handler = logging.StreamHandler()
    handler.setFormatter(
        logging.Formatter("%(asctime)s | %(levelname)s | %(thread_id)s | %(message)s")
    )
    handler.addFilter(thread_id_filter)
    logger().addHandler(handler)
    logging.getLogger().setLevel(level)
    '''
    use_col = "TERM" in os.environ
    col_terminator = "\033[0m" if use_col else ""
    logging.basicConfig(
        format=f"%(levelname)s %(asctime)s.%(msecs)03d %(name)-12s│ %(message)s{col_terminator}",
        datefmt="%H:%M:%S",
        level=getattr(logging, level) if isinstance(level, str) else level,
    )
    for name, color in (
        ("DEBUG", "\033[32m"),
        ("INFO", "\033[36m"),
        ("WARNING", "\033[33m"),
        ("ERROR", "\033[31m"),
        ("CRITICAL", "\033[37m"),
    ):
        logging.addLevelName(
            getattr(logging, name),
            f"{color if use_col else ''}({name[0] * 2})",
        )


def throw(exc: Exception) -> NoReturn:
    """Make raising an exception functional"""
    raise exc


def print_stacktrace_on_signal(sig, frame):
    """interrupt running process, and provide a python prompt for
    interactive debugging.
    see http://stackoverflow.com/questions/132058
       "showing-the-stack-trace-from-a-running-python-application"
    """
    try:
        print(f"signal {sig} received - print stack trace", file=sys.stderr)

        def print_stack_frame(stack_frame, file):
            for _f in traceback.format_stack(stack_frame):
                for _l in _f.splitlines():
                    print(_l, file=file)

        def print_stack_frames(file):
            print("++++++ MAIN ++++++++", file=file)
            print_stack_frame(frame, file)
            for task in asyncio.all_tasks():
                print(f"++++++ {task.get_coro().__name__} ++++++++", file=file)
                for stack in task.get_stack(limit=1000):
                    print_stack_frame(stack, file)

        print_stack_frames(sys.stderr)
        with open(Path("~/medit-traceback.log").expanduser(), "w") as trace_file:
            print_stack_frames(trace_file)
    except Exception:
        log().exception("Could not fully write application stack trace")


def setup_introspection_on_signal():
    """Install signal handlers for some debug stuff"""

    def setup_signal(sig, func, msg):
        signal.signal(sig, func)
        signal.siginterrupt(sig, False)
        sig_str = {signal.SIGUSR1: "USR1", signal.SIGUSR2: "USR2"}.get(sig, sig)
        print(f"Run `kill -{sig_str} {os.getpid()}` to {msg}", file=sys.stderr)

    # setup_signal(signal.SIGUSR1, increase_loglevel, "increase log level")
    setup_signal(signal.SIGUSR2, print_stacktrace_on_signal, "print stacktrace")
