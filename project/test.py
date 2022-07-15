import bluetooth

address = "DF:65:5C:84:A1:44"
port = 1
sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
#sock.connect((address, port))
sock.bind((address, port))
sock.listen(1)

client_socket, addr = sock.accept()

while True:
    data = client_socket.recv(1024)
    print("received: %s" % data)


client_socket.close()
server_socket.close()
