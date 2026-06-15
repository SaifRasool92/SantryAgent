import os, subprocess, hashlib
KEY="12345"
def run(cmd):
    h = hashlib.md5(cmd.encode())
    s = subprocess.Popen(cmd, shell=True)
    return h
