import socket
import time
def communicate(ADDRESS,PORT):
    string=input("Enter Any String: ")
    print('Operations Availible: ')
    print('\x1b[3;30;42m' + '1.Echo '+'2.length '+'3.palindrome '+'\x1b[0m')
    operation=input("Enter Any Operation from above list: ")
    c=socket.socket()
    c.connect((ADDRESS,PORT))
    c.send(string.encode("utf-8"))
    time.sleep(0.5)
    c.send(operation.encode("utf-8"))
    time.sleep(0.5)
    data=c.recv(1024).decode("utf-8")
    print('\x1b[7;30;42m' + 'Server Responce :'+ data + '\x1b[0m')
    choice=input("If you want to CONTINUE communication press y else n: ")
    if(choice=="y"):
        communicate("localhost",6667)
    else:
        print("Diconnecting with server......")
        time.sleep(2)
        return