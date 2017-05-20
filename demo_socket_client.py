# demo_socket_client.py
import socket

ser_host = '127.0.0.1'
ser_port = 8080

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

client.connect((ser_host, ser_port))

client.sendall("hello".encode())

print(client.recv(1024).decode('utf-8'))

while True:
    sendbuf = input("Input>>")
    try:
        client.send(sendbuf.encode('utf-8'))
    except socket.error as err_msg:
        print(err_msg)
    if not sendbuf or sendbuf == 'exit':
        break
    recvbuf = client.recv(1024)
    print(recvbuf.decode('utf-8'))
client.close()
print('Connection was closed...')