# demo_socket_server.py
import socket
import threading
import time

host = '127.0.0.1'
port = 8080

ser = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ser.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

ser.bind((host, port))

ser.listen(5)

print('Server is running...')       # 打印运行提示

def tcplink(connect, addr):
    print('Accept new connection from %s:%s...' % addr)
    connect.send(b'Welcome!\r\n'+b'Please tell me your name:')
    data = connect.recv(1024)
    connect.send(('Hello, %s' % data.decode('utf-8')).encode('utf-8'))
    while True:
        data = connect.recv(1024)
        time.sleep(5)
        if not data or data.decode('utf-8') == 'exit':
            break
        print("Source: %s, Data: %s, Size: %s" % (addr[0], data.decode('utf-8'), len(data)))
        connect.send(b'Data Receive')
    connect.close()
    print('Connection from %s:%s closed' % addr)

while True:
    sock, addr = ser.accept()
    pthread = threading.Thread(target=tcplink, args=(sock, addr))   #多线程处理socket连接
    pthread.start()


