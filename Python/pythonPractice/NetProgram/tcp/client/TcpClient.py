import socket
import threading
import time
import random
ip = "139.199.213.83"


def sendInfo(s,ip):
    while True:
        print(s.recv(1024).decode('utf-8'))
   


def recvInfo(s,ip):
    for i in range(1000):
        s.send(bytes(str(i),encoding="utf-8"))
        time.sleep(1)
    s.send('exit')
    s.close()

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 建立连接:
    s.connect((ip, 19999))
    # 接收欢迎消息:
    #print(s.recv(1024).decode('utf-8'))
    threading.Thread(target=sendInfo, args=(s,ip)).start()
    threading.Thread(target=recvInfo, args=(s,ip)).start()
    time.sleep(10000)

if __name__ == '__main__':
    main()
