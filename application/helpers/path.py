import glob, os

def find_exe_files(path: str = "./*.exe", recursive: bool = False) -> list:
    pattern = os.path.join(path)
    exe_files = glob.glob(pattern, recursive=recursive)
    return exe_files

def path_exist (path: str) -> str:
    return os.path.exists(path)