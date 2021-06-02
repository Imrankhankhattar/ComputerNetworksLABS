import socket
import time
ADDRESS="localhost"
PORT=6667
c=socket.socket()
c.connect((ADDRESS,PORT))

Username="imran"#Give username Here
Password="0341"#Give Password
Operation="Sineup"#Give operation i.e Authonitication/Authoriztaion/Sineup

if(Operation=='Authorization'):# If Authorization give name of resource to check permission of the above user
    Operation=input("Enter any one from R1/R2/R3 for checking permission: \n")
c.send(Username.encode("utf-8"))
time.sleep(1)
c.send(Password.encode("utf-8"))
time.sleep(1)
c.send(Operation.encode("utf-8"))
print("Server Response:::")
data=c.recv(1024)
print(data.decode("utf-8"))
