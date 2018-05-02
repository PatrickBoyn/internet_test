import socket
import tkinter
from tkinter import messagebox

def message(message):
    messagebox.showinfo('Connection?', message)

def is_connected(server):
    root = tkinter.Tk()
    root.withdraw()
    try:
        host = socket.gethostbyname(server)
        s = socket.create_connection((host, 80), 2)
        message('You are connected.')
        return True
    except:
        message('You are not connected. ')
        return False

print(is_connected('www.github.com'))
