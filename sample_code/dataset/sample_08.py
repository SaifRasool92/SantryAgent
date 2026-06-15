import socket
def open_port():
    s = socket.socket()
    s.bind(("0.0.0.0", 8080))
