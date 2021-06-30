from threading import Thread
from os import listdir
from os.path import isfile, join
import time
import pickle
import os
BUFFER = 100
packetTypes=['0x0000','0x0001','0x0011','0x0010','0x0012','0x1111']
path = 'fileStore/'
files = [f for f in listdir(path) if isfile(join(path, f))]
#files=['balochistan.txt', 'kpk.txt', 'punjab.txt', 'sindh.txt']
print(files)
class commonThread(Thread):
    def __init__(self,ADDRESS,PORT,clientsocket):
        Thread.__init__(self)
        self.clientsocket = clientsocket
        self.responce=[]
        self.request=[]
        
    def run(self):
        print("Connected")
        data,addr=(self.clientsocket.recvfrom(1024))
        self.request=pickle.loads(data)
        if(self.request==packetTypes[0]):
            self.SendFilesList(addr)    
        data,addr=(self.clientsocket.recvfrom(1024))    
        self.request=pickle.loads(data)
        self.responce=[]
        if(self.request[0]==packetTypes[1] and self.request[1] in files):
            self.SendFile(addr)
        else:
            message=[packetTypes[5],"File Does not Exits"]
            self.clientsocket.sendto(pickle.dumps(message),addr)
    def SendFilesList(self,addr):
        self.responce=files
        self.responce.insert(0,hex(len(files)))
        self.responce.insert(0,packetTypes[3])
        self.clientsocket.sendto(pickle.dumps(self.responce),addr)        
    def SendFile(self,addr):
        self.responce.append(packetTypes[2])
        self.responce.append(self.request[1])
        size_of_file=(os.stat(join(path,self.request[1]))).st_size
        self.responce.append(size_of_file)
        print(self.responce)
        self.clientsocket.sendto(pickle.dumps(self.responce),addr)
        #send files in packets
        self.PACKET(addr)
    def PACKET(self,addr):
        self.responce=[]
        packetNo=0
        f = open(join(path,self.request[1]), 'r')
        packet = f.read(BUFFER)
        while (True):
            if not packet:
                break
            self.responce.append(packetTypes[4])
            self.responce.append(hex(packetNo))
            self.responce.append(packet)
            print("file sending ....")
            self.clientsocket.sendto(pickle.dumps(self.responce),addr)
            self.responce=[]
            packet=f.read(BUFFER)
            packetNo=packetNo+1
        print("file sent succesfully..!")
        f.close()
        
        