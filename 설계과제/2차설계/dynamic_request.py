import socket
import time


request = "GET /freeweb-1.0.0-BUILD-SNAPSHOT/home/main HTTP/1.1\r\n"
request += "Host: 172.30.1.19:8080\r\n"
request += "Cache-Control: no-store, must-revalidate\r\n"
request += "\r\n"

request1 = "GET /freeweb-1.0.0-BUILD-SNAPSHOT/home/Myinfo HTTP/1.1\r\n"
request1 += "Host: 172.30.1.19:8080\r\n"
request1 += "Cache-Control: no-store, must-revalidate\r\n"
request1 += "\r\n"

request2 = "GET /freeweb-1.0.0-BUILD-SNAPSHOT/UserRegister/devRegisterProcess HTTP/1.1\r\n"
request2 += "Host: 172.30.1.19:8080\r\n"
request2 += "Cache-Control: no-store, must-revalidate\r\n"
request2 += "\r\n"


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('172.30.1.19', 8080))


while True:
 sock.send(request.encode())
 sock.send(request1.encode())
 sock.send(request2.encode())