# Server-Clients-Chat
This is a Python GUI Server/Clients multi-Thread Asynchronous Chat, using Socket, Threading, and Tkinter

******

I am a really huge fan of automation. I have some automated house programm that runs under Arduino, Actuators and Sensors (for example, an automated curtains related to the position of the sun).
This is great but I have one device per application. This makes a lot of independants devices and each one has his properties.
I want to regroups theses devices togethers and make a central server (Raspberry Pi) which can control everything.

To achieve my goal, I decided to start by implementing a communication chat in LAN to understand the data communication.

******

There are 2 scripts:
-> clientSide.py
-> serverSide.py

let's start with the serverSide.py

  I create a basic socket server, listening for connexions.
  Once a new client appear, the server creates a Thread.
  If a client send a message, the server will broadcast this message to all others clients.
  If a client leaves the chat, the server broadcast this event to all others clients.
  
 now the clientSide.py
 
  A tkinter GUI is built.
  This is a simple GUI with Listbox, scrollbar, Entry, Button.
  
 
  The client connect to the server.
  It will be ask his name as first entry.
  The client is in a listening loop from the server: a Thread is created for this purpose. This way I don't need to refresh the GUI.
  The client can send messages.
  If the client wants to quit, he can send {quit} or direclty close the window.
  
  I set the maximum connected clients to 5. It can be more.
  5 clients is enough for my purpose, because I use this chat for LAN, with a Raspberry Pi as the server and our family devices as Clients.
