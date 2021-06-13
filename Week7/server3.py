#palindrom server
# first of all import the socket library
import socket 
from threading import Thread
import time
from Threads import CommonThread
from validity import valid
# next create a socket object
s = socket.socket() 
ADDRESS="localhost"
PORT = 8888 
print("Server3 STARTED")
SCHEME="utf-8"
def Palindrome(s):
    return s==s[::-1]
def checkpalindrome(s):
    if(Palindrome(s)):
        return "Yes! the string is palindrome....."
    else:
        return "No !the string is not palindrome....."    
def main():
    s=socket.socket()
    s.bind((ADDRESS,PORT))
    s.listen(5)
    while True:
        c,addr=s.accept()
        print("Client connected with palindrome sevrer",addr)
        key=c.recv(2048).decode(SCHEME)
        time.sleep(0.5)
        string=c.recv(2048).decode(SCHEME)
        time.sleep(0.5)
        if(valid(key)=="1"):
            c.send(checkpalindrome(string).encode("utf-8"))
        else:    
            c.send("invalid token or username...!".encode(SCHEME))
main()
   