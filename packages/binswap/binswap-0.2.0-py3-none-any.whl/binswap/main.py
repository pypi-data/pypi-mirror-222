import os
import time
import logging
import argparse
import platform
import subprocess
from pathlib import Path
from typing import Optional
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

logger = logging.getLogger(__name__)
log_formatter = logging.Formatter(
    "[%(levelname)s] %(asctime)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
)
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(log_formatter)
logger.addHandler(stream_handler)
logger.setLevel(logging.INFO)


class FileChangeHandler(FileSystemEventHandler):
    def __init__(self, binary_path: str) -> None:
        super().__init__()
        self.binary_path: str = os.path.normpath(binary_path)
        self.process: Optional[subprocess.Popen] = None

    def on_created(self, event) -> None:
        if event.is_directory:
            return

        src_path = os.path.splitext(os.path.basename(event.src_path))[0].split(" ")[0]
        bin_path = os.path.splitext(os.path.basename(self.binary_path))[0].split(" ")[0]
        if src_path == bin_path:
            logger.info("Replacement binary created. Relaunching...")
            if self.process:
                try:
                    self._terminate_process(self.process)
                    self.process.wait(timeout=5)
                except subprocess.TimeoutExpired:
                    logger.warning(
                        "Old process did not terminate. Forcing termination..."
                    )
                    self.process.kill()
            self.process = self._create_subprocess(self.binary_path)

    def on_deleted(self, event) -> None:
        if event.src_path.endswith(os.path.basename(self.binary_path)):
            logger.info("Binary file deleted. Exiting...")
            if self.process:
                try:
                    self._terminate_process(self.process)
                    self.process.wait(timeout=5)
                except subprocess.TimeoutExpired:
                    logger.warning(
                        "Old process did not terminate. Forcing termination..."
                    )
                    self.process.kill()
            os._exit(0)

    @staticmethod
    def _terminate_process(process: subprocess.Popen) -> None:
        if platform.system() == "Windows":
            subprocess.run(["taskkill", "/F", "/T", "/PID", str(process.pid)])
        else:
            process.terminate()

    @staticmethod
    def _create_subprocess(binary_path: str) -> subprocess.Popen:
        if platform.system() == "Windows":
            interpreter = _get_script_interpreter(binary_path)

            if interpreter:
                return subprocess.Popen(
                    [interpreter, binary_path],
                    creationflags=subprocess.CREATE_NEW_CONSOLE,
                )
            elif os.path.isfile(binary_path) and binary_path.lower().endswith(".exe"):
                return subprocess.Popen(
                    [binary_path], creationflags=subprocess.CREATE_NEW_CONSOLE
                )
            else:
                logger.error(f"Unsupported file type for Windows: {binary_path}")
        else:
            return subprocess.Popen([binary_path])


def count_dir_files(directory: Path) -> int:
    return sum(1 for _ in directory.iterdir() if _.is_file())


def _get_script_interpreter(script_path: str) -> str:
    interpreter_mapping = {
        "py": "python",
        "js": "node",
        "rb": "ruby",
        "php": "php",
        "sh": "bash",
        "pl": "perl",
        "lua": "lua",
    }

    script_extension = script_path.lower().split(".")[-1]
    return interpreter_mapping.get(script_extension, "")


def init_file_monitoring(binary_path: str, monitored_directory: str) -> None:
    """
    Monitor dir for changes and auto relaunch executable (.exe) or script files.

    Args:
        binary_path (str): Path to the executable or script file.
        monitored_directory (str): Directory to be monitored.

    Example:
        init_file_monitoring("/path/to/binary", "/path/to/directory")
    """
    event_handler = FileChangeHandler(binary_path)
    observer = Observer()

    try:
        observer.schedule(event_handler, str(monitored_directory), recursive=False)
        observer.start()

        file = os.path.basename(binary_path)
        file_count = count_dir_files(monitored_directory)
        logger.info(f"Number of files in the directory: {file_count}")
        logger.info(f"Monitoring directory: {monitored_directory}")
        logger.info(f"File: {file}")
        logger.info("Press Ctrl+C to stop.")
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        logger.info("Stopping file monitoring...")
    except Exception as e:
        logger.error(f"An error occurred: {e}")
    finally:
        observer.stop()
        observer.join()


def main():
    parser = argparse.ArgumentParser(
        description="Monitor directory and automatically relaunch binary."
    )
    parser.add_argument(
        "--bin", type=Path, required=True, help="Path to the actual binary."
    )
    parser.add_argument(
        "--dir",
        type=Path,
        required=False,
        default=Path.cwd(),
        help="Directory to be monitored. Defaults to the current working directory.",
    )
    args = parser.parse_args()

    if not args.bin.exists():
        logger.error("Binary file does not exist. Please provide a valid path.")
        return

    init_file_monitoring(args.bin, args.dir)


if __name__ == "__main__":
    main()
