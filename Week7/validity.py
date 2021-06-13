import socket 
import time
ADDRESS="localhost"
SCHEME="utf-8"
ServerPORT=6667
print("Server2 STARTED")
def valid(key):
    c=socket.socket()
    c.connect((ADDRESS,ServerPORT))
    c.send("server".encode(SCHEME))
    time.sleep(0.5)
    c.send("server".encode(SCHEME))
    time.sleep(0.5)
    c.send(key.encode(SCHEME))
    time.sleep(0.5)
    return c.recv(2048).decode(SCHEME)