from threading import Thread
import socket
import time
import random
import csv
SCHEME="utf-8"
ADDRESS="localhost"
server_ports=[6666,7777,8888]
user_record=[]
ID_PORT=9998
class CommonThread(Thread):
    def __init__(self,socket):
        Thread.__init__(self)
        self.client_socket=socket
    def run(self):
        print("Client Server Communication Started....")
        username=self.client_socket.recv(2048)
        time.sleep(0.5)
        password=self.client_socket.recv(2048)
        time.sleep(0.5)
        if(username==password and username=='server'):
            key=self.client_socket.recv(2048).decode(SCHEME)
            self.client_socket.send(checkvalidity(key).encode(SCHEME))
            return
        print("Checking credentials......please wait!")
        clientdata=balancer(username.decode(SCHEME),password.decode(SCHEME))
        key=clientdata
        if(clientdata=="User Not Found"):
            self.client_socket.send(clientdata.encode(SCHEME))
        else:
            print("User Authonticated..!")
            self.client_socket.send(clientdata.encode(SCHEME))
            choice=self.client_socket.recv(2048)
            choice=choice.decode(SCHEME)
            print(choice)
            time.sleep(0.5)
            if(choice=="e"):
                clientdata=server_ports[0]
            elif(choice=="l"):
                clientdata=server_ports[1]
            elif(choice=="p"):
                clientdata=server_ports[2]
            else:
                clientdata="invalid choice"
        self.client_socket.send(str(clientdata).encode(SCHEME))
        SetRecord(username.decode(SCHEME),key)    
def checkvalidity(key):
    for i in range(len(user_record)):
        if(user_record[i]==key):
            return "1"
    return "0"        
def SetRecord(username,key):
        key_updated=False
        for i in range(len(user_record)):
            if(user_record[i]==username):
                user_record[i+1]=key
                key_updated=True
        if(key_updated==False):    
            user_record.append(username)
            user_record.append(key)
        print(user_record)        
def balancer(usr,ps):
    usr=usr.lower()
    ps=ps.lower()
    c=socket.socket()    
    c.connect((ADDRESS,ID_PORT))
    c.send(usr.encode(SCHEME))
    time.sleep(0.5)
    c.send(ps.encode(SCHEME))
    time.sleep(0.5)
    data=c.recv(1024).decode(SCHEME)
    return data         
    
   
