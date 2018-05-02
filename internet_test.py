import socket

def is_connected(server):
    try:
        host = socket.gethostbyname(server)
        s = socket.create_connection((host, 80), 2)
        print("There is a connection.")
        return True
    except:
        print("Sorry you are not connected.")
        return False

print(is_connected('www.github.com'))
