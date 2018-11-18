import socket
import time
sk = socket.socket()


class user():
    def __init__(self, username, passwd):
        self.username = username
        self.passwd = passwd


class login():
    def __init__(self, user: user):
        self.user = user

    def setIP(self, ip="127.0.0.1", port=8090):
        sk.connect((ip, port))

    def login(self):
        pass
