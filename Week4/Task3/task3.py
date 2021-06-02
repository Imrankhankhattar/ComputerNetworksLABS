
import socket
s=socket.socket()
host="www.google.com"
port=80

server_ip=socket.gethostbyname(host)
print(server_ip)
s.connect((host,port))
requets="GET/https://namal.edu.pk//HTTP/1.1\r\n\r\n"
s.send(requets.encode("utf-8"))
response=s.recv(2048)
print(response)