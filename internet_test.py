import socket
import tkinter
from tkinter import messagebox


def is_connected(server):
    root = tkinter.Tk()
    root.withdraw()
    
    # This script was found on Stack Overflow. 
    # The original was written in Python 2, and with print statements.
    # I thought a popup would be more fun. I also put it all in functions
    # So that the program could be more modular. 
    try:
        host = socket.gethostbyname(server)
        socket.create_connection((host, 80), 2)

        message('You are connected. ')
        return True
    except:
        message('You are not connected. ')
        return False


def message(message):
    messagebox.showinfo('Connected?', message)


if __name__ == "__main__":
    # This must be both a real website and an active website. 
    is_connected('www.github.com')
