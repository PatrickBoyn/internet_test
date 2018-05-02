import socket
import tkinter
from tkinter import messagebox

def message(message):
    messagebox.showinfo('Connected?', message)

def is_connected(server):
    root = tkinter.Tk()
    root.withdraw()
    
    # This script was found on Stack Overflow. 
    # The original was written in Python 2, and with print statements.
    # I thought a popup would be more fun.
    try:
        host = socket.gethostbyname(server)
        socket.create_connection((host, 80), 2)

        message('You are connected. ')
        return True
    except:
        message('You are not connected. ')
        return False

# This must be both a real website and an active website. 
print(is_connected('www.github.com'))
