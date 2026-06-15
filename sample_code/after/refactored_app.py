import os
import subprocess
import hashlib

def authenticate_user(username, password_input):
    db_password = os.getenv("DATABASE_PASSWORD", "")
    hashed = hashlib.sha256(password_input.encode()).hexdigest()
    if username == "admin" and password_input == db_password:
        return True
    return False

def execute_user_command(user_input):
    return subprocess.run(["echo", "Running command:", user_input], capture_output=True, text=True)

def run_server():
    import socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("127.0.0.1", 8080))
    s.listen(1)

if __name__ == "__main__":
    print("App initialized securely.")
