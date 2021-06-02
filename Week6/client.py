
import socket
import time
ADDRESS="localhost"
PORT=6667
def communicate():
    string=input("Enter Any String: ")
    operation=input("Enter Operation: ")
    c=socket.socket()
    c.connect((ADDRESS,PORT))
    c.send(string.encode("utf-8"))
    time.sleep(0.5)
    c.send(operation.encode("utf-8"))
    time.sleep(0.5)
    data=c.recv(1024).decode("utf-8")
    print('\x1b[6;30;42m' + 'Server Responce :'+ data + '\x1b[0m')
communicate()
while(True):
    choice=input("If you want to CONTINUE communication press y else n: ")
    if(choice=="y"):
        communicate()
    else:
        break           
  


