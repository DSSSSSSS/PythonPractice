import socket
import threading
import time
# 互联网协议包含了上百种协议标准，
# 但是最重要的两个协议是TCP和IP协议，所以，大家把互联网的协议简称TCP/IP协议

# TCP协议则是建立在IP协议之上的。
# TCP协议负责在两台计算机之间建立可靠连接，保证数据包按顺序到达。

# 源IP地址和目标IP地址，
# 源端口和目标端口
# ip用于确定计算机
# 端口用于确定进程


def recvInfo(sock, addr):
    while True:
        data = sock.recv(1024)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed.' % addr)


def sendInfo(sock, addr):
    while True:
        sock.send(b'Welcome!')
        time.sleep(1)



def tcplink(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    # sock.send(b'Welcome!')
    threading.Thread(target=sendInfo, args=(sock,addr)).start()
    threading.Thread(target=recvInfo, args=(sock,addr)).start()


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 监听端口:
    s.bind(('0.0.0.0', 19999))
    s.listen(5)
    print('Waiting for connection...')
    while True:
        # 接受一个新连接:
        sock, addr = s.accept()
        # 创建新线程来处理TCP连接:
        t = threading.Thread(target=tcplink, args=(sock, addr))
        t.start()


if __name__ == '__main__':
    main()
