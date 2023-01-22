# psu_client.py

import socket
import time

SERVER = "roof.local"
PORT = 5050

FORMAT = 'utf-8'
HEADER = 64


if __name__ == '__main__':
    print(f"Connecting to {SERVER}:{PORT}")
    # ip = netifaces.ifaddresses(iface)[netifaces.AF_INET][0]['addr']


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER, PORT))


def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    response = client.recv(2048).decode(FORMAT)
    print(response)


send("s")
connected = True
while connected:
    command = input("Command: R(x, T(x, P(tt, S(tatus, Q(uit, K(ill: ")
    send(command)
    if command == "q" or command == "k":
        time.sleep(1.0) # to allow reception of server response
        connected = False
    
