#identity server
# first of all import the socket library
import socket 
from threading import Thread
import time
import random
import csv
from Threads import CommonThread
# next create a socket object
UserDeatails=["jaleel","0000","imran","0000","azam","0000"]
print(UserDeatails)
s = socket.socket() 
ADDRESS="localhost"
PORT = 9998 
print("id server STARTED")
def Randome_key():
    return random.randint(1000,9999)
def login(UserName,password):#checks if username already existss
    print(UserName,password)
    for i in range(len(UserDeatails)):
        if(UserDeatails[i]==UserName and UserDeatails[i+1]==password):
            return Randome_key()
        i=i+2
    return "User Not Found"       
def main():
    s=socket.socket()
    s.bind((ADDRESS,PORT))
    s.listen(5)
    while True:
        c,addr=s.accept()
        print("Connnected with Identity server...!",addr)
        data=c.recv(2048).decode("utf-8")
        time.sleep(0.5)
        data2=c.recv(2048).decode("utf-8")
        time.sleep(0.5)
        print(data,data2)
        responce=str(login(data,data2))
        c.send(responce.encode("utf-8"))
main()