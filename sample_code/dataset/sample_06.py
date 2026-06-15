import subprocess
def run_ls(dir_path):
    return subprocess.Popen(f"ls {dir_path}", shell=True)
