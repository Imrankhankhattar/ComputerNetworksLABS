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
    def __init__(self, clientsocket):
        Thread.__init__(self)
        self.clientsocket = clientsocket
        self.responce=[]
        self.request=[]
        
    def run(self):
        print("Connected")
        self.request=pickle.loads(self.clientsocket.recv(1024))
        if(self.request==packetTypes[0]):
            self.SendFilesList()    
        self.request=pickle.loads(self.clientsocket.recv(1024))
        self.responce=[]
        if(self.request[0]==packetTypes[1] and self.request[1] in files):
            self.SendFile()
        else:
            message=[packetTypes[5],"File Does not Exits"]
            self.clientsocket.send(pickle.dumps(message))
    def SendFilesList(self):
        self.responce=files
        self.responce.insert(0,hex(len(files)))
        self.responce.insert(0,packetTypes[3])
        self.clientsocket.send(pickle.dumps(self.responce))        
    def SendFile(self):
        self.responce.append(packetTypes[2])
        self.responce.append(self.request[1])
        size_of_file=(os.stat(join(path,self.request[1]))).st_size
        self.responce.append(size_of_file)
        print(self.responce)
        self.clientsocket.send(pickle.dumps(self.responce))
        #send files in packets
        self.PACKET()
    def PACKET(self):
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
            self.clientsocket.send(pickle.dumps(self.responce))
            self.responce=[]
            packet=f.read(BUFFER)
            packetNo=packetNo+1
        print("file sent succesfully..!")
        f.close()
        
        