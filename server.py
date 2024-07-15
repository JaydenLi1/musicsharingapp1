import socket
from threading import Thread
IP_ADDRESS = '127.0.0.1'
PORT = 8080
SERVER = None
clients = {}


def accept_connections():
    global SERVER
    global clients

    while True:
        client, addr = SERVER.accept()
        print(client, addr)


def setup():
    print('\n\t\t\t\tIP MESSANGER\n')
    global PORT
    global IP_ADDRESS
    global SERVER

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.bind((IP_ADDRESS, PORT))

    SERVER.listen(100)
    print("\t\t\tSERVER is waiting for incoming connections...")
    print("\n")

    accept_connections()


setup_thread = Thread(target=setup)
setup_thread.start()
