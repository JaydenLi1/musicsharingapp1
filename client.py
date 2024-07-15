import socket
from threading import Thread
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
PORT = 8080
IP_ADDRESS = '127.0.0.1'
SERVER = None
name = None
listbox = None
textarea = None
labelChat = None
text_message = None


def setup():
    global SERVER
    global PORT
    global IP_ADDRESS

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS, PORT))
    musicWindow()


def musicWindow():
    print('\n\tMessage')
    window = Tk()
    window.title('Music Sharing')
    window.geometry('500x300')
    global name
    global listbox
    global textarea
    global labelChat
    global text_message
    global musicpathdata

    nameLabel = Label(window, text="Enter Your Name", font=('Calibri', 10))
    nameLabel.place(x=10, y=8)

    name = Entry(window, width=30, font=('Calibri', 10))
    name.place(x=120, y=8)
    name.focus()

    connectServer = Button(
        window, text='connect to chat server', font=('Calibri', 10), bd=1)
    connectServer.place(x=350, y=6)

    separator = ttk.Separator(window, orient='horizontal')
    separator.place(x=0, y=35, relwidth=1, height=0.5)

    connectButton = Button(window, text='connect', bd=1, font=('Calibri', 10))
    connectButton.place(x=282, y=160)

    disconnectButton = Button(
        window, text='disconnect', bd=1, font=('Calibri', 10))
    disconnectButton.place(x=350, y=160)
    labelUsers = Label(window, text='active users', font=('Calibri', 10))
    labelUsers.place(x=10, y=50)

    listbox = Listbox(window, height=5, width=67, font=(
        'Calibri', 10), activestyle='dotbox')
    listbox.place(x=10, y=70)

    refreshButton = Button(window, text='refresh', bd=1, font=('Calibri', 10))
    refreshButton.place(x=435, y=160)
    scrollbar1 = Scrollbar(listbox)
    scrollbar1.place(relheight=1, relx=1)
    scrollbar1.config(command=listbox.yview)

    labelChat = Label(window, text='chatwindow', font=('Calibri', 10))
    labelChat.place(x=10, y=180)

    textarea = Text(window, width=67, height=6, font=('Calibri', 10))
    textarea.place(x=10, y=200)

    scrollbar2 = Scrollbar(listbox)
    scrollbar2.place(relheight=1, relx=1)
    scrollbar2.config(command=listbox.yview)

    attach = Button(window, text='attach and send', bd=1, font=('Calibri', 10))
    attach.place(x=30, y=309)

    text_message = Entry(window, width=37, font=('Calibri', 12))
    text_message.pack()
    text_message.place(x=158, y=306)

    send = Button(window, text='send', bd=1, font=('Calibri', 10))
    send.place(x=450, y=305)

    musicpathlabel = Label(window, text='', fg='blue', font=('Calibri', 10))
    musicpathlabel.place(x=10, y=315)
    window.mainloop()


setup()
