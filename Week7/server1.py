#ECHO server
# first of all import the socket library
import socket 
from threading import Thread
import time
from Threads import CommonThread
from validity import valid
# next create a socket object
s = socket.socket() 
ADDRESS="localhost"
PORT = 6666 
SCHEME="utf-8"
def main():
    s=socket.socket()
    s.bind((ADDRESS,PORT))
    s.listen(5)
    while True:
        c,addr=s.accept()
        print("Connnected with Echo server",addr)
        key=c.recv(2048).decode(SCHEME)
        time.sleep(0.5)
        string=c.recv(2048).decode(SCHEME)
        time.sleep(0.5)
        if(valid(key)=="1"):
            c.send(string.encode(SCHEME))
        else:    
            c.send("invalid token or username...!".encode(SCHEME))
main()

