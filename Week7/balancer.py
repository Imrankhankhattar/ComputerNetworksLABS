# first of all import the socket library
import socket 
from threading import Thread
import time
from Threads import CommonThread
# next create a socket object
s = socket.socket() 
ADDRESS="localhost"
PORT = 6667 
print("Server STARTED")

def main():
    s=socket.socket()
    s.bind((ADDRESS,PORT))
    s.listen(5)
    while True:
        c,addr=s.accept()
        print("client Connnected",addr)
        client_thread=CommonThread(c)
        client_thread.start()
main()        