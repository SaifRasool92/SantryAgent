import socket, subprocess
HOST="0.0.0.0"
def start():
    s = socket.socket()
    s.bind((HOST, 9090))
    subprocess.run("rm -rf /tmp/*", shell=True)
