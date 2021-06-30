import socket
from commonthread import commonThread
ADDRESS="localhost"
PORT=6667

def main():
    s = socket.socket()
    s.bind((ADDRESS,PORT))
    s.listen(5)
    print("Server is listening at : ",PORT)
    while True:
        c, addr = s.accept()
        print("Connected With : ", addr)
        clientthread = commonThread(c)
        clientthread.start()
        
if __name__ == "__main__":
    main()
