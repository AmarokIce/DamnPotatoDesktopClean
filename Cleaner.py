import os
import shutil
import datetime
from pathlib import Path

desktop_path = str(os.path.join(os.path.expanduser("~"), 'Desktop'))

def get_data_last(file: Path) -> str:
    last_modified_time = os.path.getmtime(file)
    last_modified_time = datetime.datetime.fromtimestamp(last_modified_time)
    return str(last_modified_time.year) + "-" + str(last_modified_time.month)

def check_file_should_delete(file: Path) -> bool:
    if (file.name.endswith(".bak") or file.name.endswith(".log") or file.name.endswith(".dwl")):
        return True
    return False;

def delete_file(file: Path) -> None:
    os.remove(file)

def move_file(file: Path, type: str) -> None:
    new_dir = str(desktop_path) + "/CAD/" + type + str(get_data_last(file))
    path = Path(new_dir)
    if not path.is_dir():
        os.makedirs(path)
    shutil.move(file, new_dir + "/" + file.name)

def add_dir_with_file(dir: Path, file: str) -> Path:
    return Path(os.path.join(dir, file))

def check_file(file: Path) -> None:
    if file.name.endswith(".dwg"):
        move_file(file, "dwg/")
    elif file.name.endswith(".ppt") or file.name.endswith(".pptx"):
        move_file(file, "ppt/")
    elif file.name.endswith(".pdf") or file.name.endswith(".xlsx") or file.name.endswith(".xls"):
        move_file(file, "报单/")
    elif check_file_should_delete(file):
        delete_file(file)

def check_dir(dir: Path) -> None:
    for file in os.listdir(dir):
        file_path = add_dir_with_file(dir, file)

        try:
            if Path(file_path).is_dir():
                check_dir(file_path)
            else:
                check_file(file_path)
        except:
            pass

if __name__ == "__main__":
    check_dir("C:/")