import pickle
import socket
import time
from math import ceil
request_packet = []
packet_size = 100
packet_type1 = "0x0000"
packet_type2 = "0x0001"


def communicate(address, port):
    # connection with server
    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    # requesting file list
    ADRESS=((address,port))
    s.sendto(pickle.dumps(packet_type1),ADRESS)
    req,addr=s.recvfrom(1024)
    message = pickle.loads(req)
    print(message)
    # requesting a file to download
    inputuser = input("Enter File name: ")
    request_packet.append(packet_type2)
    request_packet.append(inputuser)
    s.sendto(pickle.dumps(request_packet),ADRESS)
    # file response
    req,addr=s.recvfrom(1024)
    message = pickle.loads(req)
    if(message[0] == '0x1111'):
        print(message[1])
    else:
        # with open('client.txt', 'wb') as f:
        #     print ('file opened')
        total_packets = (ceil(message[2]/100))
        mes = ""
        #     print(floor(total_packets))
        while (total_packets >= 1):
            print('receiving data...')
            data,addr=s.recvfrom(1024)
            data = pickle.loads(data)
            mes = mes+data[2]
            total_packets = total_packets-1
        print("file recieved succesfully..!")
        with open('client.txt', 'wb') as f:
            print(mes)
            arr = bytes(mes, "utf-8")
            f.write(arr)
            f.close()
