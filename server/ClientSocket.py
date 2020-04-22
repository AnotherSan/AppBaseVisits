import socket

sock = socket.socket()
sock.connect(('localhost', 9090))

while True:
    data = sock.recv(1024)
    print(data.decode())
    answer = input()
    sock.send(answer.encode())

sock.close()