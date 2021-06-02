
import socket
ADDRESS="localhost"
PORT=6667

Record=["imrankhan","imr4534","azha","0341","ali","pass333"]#storing username at even places and passwords at odd indexes
size=Record.__len__()

def checkRecord(UserName,Password):
    i=0
    while(i<size):
        if(Record[i]==UserName):
            if(Record[i+1]==Password):
               return "User Authorized"
            else:
                return "User Not Authoried"      
        i+=1                  
    return "User Not Authorized"  


s=socket.socket()
s.bind((ADDRESS,PORT))
s.listen(5)
print("Listening.......")
while True:
    c,addr=s.accept()
    print("client Connnected",addr)
   # c.send("Salama Laikum".encode("utf-8"))
    data=c.recv(2048)
    username, password = [str(i) for i in data.decode('utf-8').split('\n')]
    result=checkRecord(username,password)
    c.send(result.encode("utf-8"))
    
