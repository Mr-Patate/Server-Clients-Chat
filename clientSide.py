from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import tkinter

# The receive function is listeling in While loop
# It will display messages that are oncoming
def receive():
    while True:
        try:
            msg = client_socket.recv(BUFSIZ).decode("utf8")
            # the message is added a the end of the list on tkinter Listbox
            msg_list.insert(tkinter.END, msg)
        except OSError:
            break

# if the Button send is pressed, the function is activated
# That mean we send the text message to others
def send(event=None):
    """Handles sending of messages."""
    msg = my_msg.get()
    # Clear the tk.Entry
    my_msg.set("")
    client_socket.send(bytes(msg))
    # The client can exit the chat by writting {quit}
    if msg == "{quit}":
        client_socket.close()
        top.destroy()

# If the client close the window, this function is activated
# The message {quit} is anyway sent in order to have a clean exit
def on_closing(event=None):
    my_msg.set(bytes("{quit}"))
    send()

# Creating the tkinter window
top = tkinter.Tk()
top.title("Chat Chat Chat")

messages_frame = tkinter.Frame(top)
my_msg = tkinter.StringVar()  # For the messages to be sent.
my_msg.set("Type Here !")
scrollbar = tkinter.Scrollbar(messages_frame)  # To navigate through past messages.
# Following will contain the messages.
msg_list = tkinter.Listbox(messages_frame, height=15, width=50, yscrollcommand=scrollbar.set)
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
msg_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
msg_list.pack()
messages_frame.pack()

entry_field = tkinter.Entry(top, textvariable=my_msg)
entry_field.bind("<Return>", send)
entry_field.pack()
send_button = tkinter.Button(top, text="Send", command=send)
send_button.pack()

top.protocol("WM_DELETE_WINDOW", on_closing)

# The client has the possibility to log on an other Host:Port if he wants
HOST = input('Enter host: ')
PORT = input('Enter port: ')
# The client has only to know the IP adress of the server. Port is automatically matched with serverSide.py if empty
if not PORT:
    PORT = 7000
else:
    PORT = int(PORT)

BUFSIZ = 1024
ADDR = (HOST, PORT)

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDR)

# Create a thread for the communcation: This way we don't need to refresh the window
receive_thread = Thread(target=receive)
receive_thread.start()
tkinter.mainloop()