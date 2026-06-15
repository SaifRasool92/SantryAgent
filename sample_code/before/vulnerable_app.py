import os
import subprocess
import hashlib

DATABASE_PASSWORD = "SuperSecretAdminPassword123!"

def authenticate_user(username, password_input):
    hashed = hashlib.md5(password_input.encode()).hexdigest()
    if username == "admin" and password_input == DATABASE_PASSWORD:
        return True
    return False

def execute_user_command(user_input):
    command = f"echo Running command: {user_input}"
    return subprocess.Popen(command, shell=True)

def run_server():
    import socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("0.0.0.0", 8080))
    s.listen(1)

if __name__ == "__main__":
    print("App initialized.")