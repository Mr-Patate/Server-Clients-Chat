from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread

# If a new client login, a new Thread is created
def accept_incoming_connections():
    while True:
        client, client_address = SERVER.accept()
        print("%s:%s has connected." % client_address)
        client.send(bytes("Welcome on Chat Chat Chat. Please enter your name!"))
        addresses[client] = client_address
        Thread(target=handle_client, args=(client,)).start()

# For each client
# The function waits for message from a client (while loop) and to broadcast the message
# If a client leaves the chat, a message is send to all the clients
def handle_client(client):  # Takes client socket as argument.
    name = client.recv(BUFSIZ).decode("utf8")
    welcome = 'Welcome %s! If you ever want to quit, type {quit} to exit.' % name
    client.send(bytes(welcome))
    msg = "%s has joined the chat!" % name
    broadcast(bytes(msg))
    clients[client] = name

    while True:
        msg = client.recv(BUFSIZ)
        if msg != bytes("{quit}"):
            broadcast(msg, name+": ")
        else:
            client.send(bytes("{quit}"))
            client.close()
            del clients[client]
            broadcast(bytes("%s has left the chat." % name))
            break

# Function used to send message to all clients
def broadcast(msg, name=""):
    for sock in clients:
        sock.send(bytes(name)+msg)


clients = {}
addresses = {}

# On this script, host is localhost: 127.0.0.1
HOST = ''
PORT = 7000
BUFSIZ = 1024
ADDR = (HOST, PORT)

SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)

if __name__ == "__main__":
    SERVER.listen(5)
    print("Waiting for connection...")
    # When a new client comes, a new Thread is created
    ACCEPT_THREAD = Thread(target=accept_incoming_connections)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close()