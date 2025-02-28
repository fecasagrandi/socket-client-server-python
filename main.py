import socket

PASSWORD = "casa1234"  

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect(('localhost', 6969))

request = f"{PASSWORD}\r\nGET /pagina.html HTTP/1.0\r\n\r\n"
cliente.send(request.encode())

while True:
    data = cliente.recv(512)
    if len(data) < 1:
        break
    print(data.decode(), end='')

cliente.close()
