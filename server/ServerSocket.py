import socket

sock = socket.socket()
sock.bind(('', 9090))
sock.listen()


def get_data(description):
    conn.send(description.encode())
    result = conn.recv(2056)
    return result


conn, addr = sock.accept()
conn.close()