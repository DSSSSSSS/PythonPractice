import socket
import time
sk = socket.socket()
print(__name__)

class user():
    def __init__(self, username, passwd):
        self.username = username
        self.passwd = passwd

    def __str__(self):
        return str(self.username)+" "+str(self.passwd)
class login():
    def __init__(self, user: user):
        self.user = user

    def setIP(self, ip="127.0.0.1", port=8090):
        sk.connect((ip, port))

    def login(self):
        sk.send(("login"+" "+str(self.user)).encode("utf-8"))
        return sk.recv(1024)

def main():
    print("start login")
    user1= user("Bob","123")
    l =login(user1)
    l.setIP()
    print(l.login())
    time.sleep(10)

if __name__ == '__main__':
    main()