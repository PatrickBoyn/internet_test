import socket
import tkinter
from tkinter import messagebox

def message(message):
    messagebox.showinfo('Connected?', message)

def is_connected(server):
    root = tkinter.Tk()
    root.withdraw()
    try:
        host = socket.gethostbyname(server)
        socket.create_connection((host, 80), 2)

        message('You are connected. ')
        return True
    except:
        message('You are not connected. ')
        return False

# This must be both a real website and an active website. 
print(is_connected('www.cnn.com'))
