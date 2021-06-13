import socket
import time
ADDRESS="localhost"
SCHEME="utf-8"
def services(PORT,key):
    c=socket.socket()
    c.connect((ADDRESS,PORT))
    c.send(key.encode(SCHEME))
    time.sleep(0.5)
    c.send(input("Enter String :").encode(SCHEME))
    time.sleep(0.5)
    output=c.recv(2048).decode(SCHEME)
    print(output)
    choice=input("If you want to CONTINUE communication press y else n: ")
    if(choice=="y"):
        services(int(PORT),key)
    else:
        print("Diconnecting with server......")
        time.sleep(2)
        return 
def communicate(ADDRESS,PORT):
    user=input("Enter USERNAME: ")
    password=input("Enter  PASSWORD: ")
    c=socket.socket()
    c.connect((ADDRESS,PORT))
    c.send(user.encode(SCHEME))
    time.sleep(0.5)
    c.send(password.encode(SCHEME))
    time.sleep(0.5)
    data=c.recv(1024).decode(SCHEME)
    print('\x1b[7;30;42m' + 'Server Responce :'+ data + '\x1b[0m')
    if(data=="User Not Found"):
        pass
    else:
        print("User Authonticated..!")
        print("Press e for echo ,p for palindrome,l for length checker")
        choice=input("Enter service name please: ")
        c.send(choice.encode(SCHEME))
        time.sleep(0.5)
        port=c.recv(1024).decode(SCHEME)
        print("Your server port is:  ",port) 
        print("Your key is:  ",data)
        services(int(port),data)    
    