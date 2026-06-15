import subprocess, socket
SECRET="API_KEY_9999"
def exec_server():
    s = socket.socket()
    s.bind(("0.0.0.0", 5000))
    subprocess.Popen("echo " + SECRET, shell=True)
