from pathlib import Path
import os

def __check_directory(path: Path, files: list) -> None:
    for file in files:
        file_path = os.path.join(path, file)
        check_empty_dir(file_path)

def check_empty_dir(path: Path) -> None:
    if not Path(path).is_dir:
        return
    files = os.listdir(path)
    if files:
        __check_directory(path, files)
        return
    os.rmdir(path)

if __name__ == '__main__':
    check_empty_dir("C:/")