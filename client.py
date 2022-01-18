import socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(("127.0.0.1",8092))

#clientsocket.connect(('192.168.1.35', 8092))

clientsocket.send(bytes('hello howe are you', 'UTF-8'))


