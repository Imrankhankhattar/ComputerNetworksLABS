#length Checker
# first of all import the socket library
import socket 
from threading import Thread
import time
from Threads import CommonThread
# next create a socket object
s = socket.socket() 
ADDRESS="localhost"
PORT = 7777 
print("Server2 STARTED")
def main():
    s=socket.socket()
    s.bind((ADDRESS,PORT))
    s.listen(5)
    while True:
        c,addr=s.accept()
        print("client Connnected with server2",addr)
        data=c.recv(2048).decode("utf-8")
        time.sleep(0.5)
        c.send(str(len(data)).encode("utf-8"))
main()