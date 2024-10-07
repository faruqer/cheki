import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind(('localhost', 12345))

server_socket.listen(5)
print("Server listening on port 12345...")

while True:
    client_socket, addr = server_socket.accept()
    print(f"Connection from {addr} has been established!")
    while True:
        command = input("Enter a command: ")
        client_socket.send(f"{command}".encode("utf-8"))
        recived_data = client_socket.recv(81920)
        print(recived_data.decode("utf-8"))
