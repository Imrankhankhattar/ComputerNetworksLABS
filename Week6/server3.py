#palindrom server
# first of all import the socket library
import socket 
from threading import Thread
import time
from Threads import CommonThread
# next create a socket object
s = socket.socket() 
ADDRESS="localhost"
PORT = 8888 
print("Server3 STARTED")
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
        print("client Connnected with server3",addr)
        data=c.recv(2048).decode("utf-8")
        time.sleep(0.5)
        c.send(checkpalindrome(data).encode("utf-8"))
main()
   