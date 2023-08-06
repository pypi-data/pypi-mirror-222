import json
import logging
import subprocess
import os
import sys
import threading
import time
import pkg_resources

from typing import IO, Callable
from pathlib import Path


def output_stream_watcher(pipe: IO[bytes], funcs: list[Callable[[bytes], None]], verbose=False):
    try:
        with pipe:
            for line in iter(pipe.readline, b''):
                message = line.decode()
                if (verbose):
                    print(message)
                for func in funcs:
                    func(message)
    except Exception as e:
        print(f"reading pipe output with error {e}")


class RCloneWrapper:
    """
    Wrapper class for rclone.
    """

    def __init__(self, cfg):
        self.cfg = '\n'.join(f'[{name}]\n' + '\n'.join(f'{k} = {v}' for k,
                             v in settings.items()) for name, settings in cfg.items())

        self.log = logging.getLogger("RClone")
        self.log.setLevel(logging.DEBUG)
        console_handler = logging.StreamHandler()
        self.log.addHandler(console_handler)
        self.config_path = pkg_resources.resource_filename(
            "pyrclone", "rclone.conf")
        self.rclone_path = pkg_resources.resource_filename(
            "pyrclone", "rclone")
        with open(self.config_path, 'w', encoding="utf-8") as cfg_file:
            self.log.info("rclone config: ~%s~", self.cfg)
            cfg_file.write(self.cfg)
            cfg_file.flush()
            self.cfg_file = cfg_file
        self.mount_err_count = 0
        self.rclone_process = None

    def _execute(self, command_with_args):
        self.log.debug("Invoking : %s", " ".join(command_with_args))
        try:
            proc = subprocess.run(
                command_with_args,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE, check=True
            )

            out = proc.stdout.decode("utf-8")
            return {
                "code": proc.returncode,
                "out": out,
            }
        except subprocess.CalledProcessError as exception:
            raise RuntimeError(
                f"rclone running with error, please check the config again! output:${proc.stdout.decode()} ${proc.stderr.decode()}")

    def get_vfs_cache_upload_status(self):
        results = self.run_cmd("rc", ["vfs/stats"])
        if (results.get("code") != 0):
            return False
        out = json.loads(results.get("out"))
        return out["diskCache"]["uploadsInProgress"] == 0 and out["diskCache"]["uploadsQueued"] == 0

    def inc_error_count(self, message: str):
        self.mount_err_count += 1
        self.log.error(message)

    def get_err_count(self):
        return self.mount_err_count

    def get_rclone_status(self):

        if self.rclone_process is None:
            return False
        if self.rclone_process.poll() is not None:
            return False
        if self.get_err_count() > 2:
            return False
        return True

    def _execute_async(self, command_with_args, verbose=False):
        self.log.debug("Invoking : %s", " ".join(command_with_args))
        process = subprocess.Popen(
            command_with_args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        error_watcher = threading.Thread(target=output_stream_watcher, args=(
            process.stderr, [self.inc_error_count], verbose))
        error_watcher.start()
        return process

    def run_cmd(self, command, extra_args=[]):
        command_with_args = [self.rclone_path,
                             command, "--config", self.cfg_file.name]
        command_with_args += extra_args
        command_result = self._execute(command_with_args)

        return command_result

    def run_cmd_async(self, command, extra_args=[], verbose=False):
        command_with_args = [self.rclone_path,
                             command, "--config", self.cfg_file.name]
        command_with_args += extra_args
        command_result = self._execute_async(command_with_args, verbose)

        return command_result

    def copy(self, source, dest, flags=[]):
        return self.run_cmd(command="copy", extra_args=[source] + [dest] + flags)

    def sync(self, source, dest, flags=[]):
        return self.run_cmd(command="sync", extra_args=[source] + [dest] + flags)

    def listremotes(self, flags=[]):
        return self.run_cmd(command="listremotes", extra_args=flags)

    def ls(self, dest, flags=[]):
        return self.run_cmd(command="ls", extra_args=[dest] + flags)

    def lsjson(self, dest, flags=[]):
        return self.run_cmd(command="lsjson", extra_args=[dest] + flags)

    def delete(self, dest, flags=[]):
        return self.run_cmd(command="delete", extra_args=[dest] + flags)

    def mount(self, remote_path: str, local_path: Path, flags=[], verbose=False):
        if sys.platform == "win32":
            if local_path.exists():
                raise ValueError(
                    f"Mount path {local_path} already exists, please delete it first")
            if local_path.parent.exists() is False:
                raise ValueError(
                    f"Mount path parent {local_path.parent} does not exist, please create it first")
        else:
            if local_path.exists() is False:
                raise ValueError(
                    f"Mount path {local_path} does not exist, please create it first"
                )
        process = self.run_cmd_async(command="mount", extra_args=[
                                     remote_path] + [str(local_path)] + flags, verbose=verbose)
        for i in range(10, 0, -1):
            self.log.info(f"Waiting for mount to be ready in {i} seconds")
            time.sleep(1)
        self.rclone_process = process
        return process
