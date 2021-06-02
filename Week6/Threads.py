from threading import Thread
import socket
import time
import random
import csv
SCHEME="utf-8"
ADDRESS="localhost"
server_ports=[6666,7777,8888]
class CommonThread(Thread):
    def __init__(self,socket):
        Thread.__init__(self)
        self.client_socket=socket
    def run(self):
        print("Client Server Communication Started....")
        data=self.client_socket.recv(2048)
        time.sleep(0.5)
        operation=self.client_socket.recv(2048)
        time.sleep(0.5)
        clientdata=balancer(data,operation.decode(SCHEME))
        self.client_socket.send(clientdata.encode(SCHEME))

def balancer(string,operation):
    operation=operation.lower()
    if(operation=="echo" or operation=="e"):
        PORT=server_ports[0]
    elif(operation=="length" or operation=="l"):
        PORT=server_ports[1]
    elif(operation=="palindrome" or operation=="p"):
        PORT=server_ports[2]
    else:
        return "Invalid operation"
    c=socket.socket()    
    c.connect((ADDRESS,PORT))
    c.send(string)
    data=c.recv(1024).decode("utf-8")
    return data         
    
   
