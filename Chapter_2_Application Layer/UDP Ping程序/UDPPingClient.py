import time
from socket import *

serverName = '192.168.134.128'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_DGRAM)
# 设置最多等待时间1s
clientSocket.settimeout(1)

for i in range(1,11):
    sendTime = time.time()
    message = 'Ping ' + str(i) + ' '+time.asctime()
    # 发送Ping命令，并打印
    clientSocket.sendto(message.encode(), (serverName, serverPort))
    print('> ' + message)
    try:
        modifiedMessage, serverAddress = clientSocket.recvfrom(1024)
        RTT = time.time() - sendTime
        print("%s,  RTT = %.3fs" % (modifiedMessage.decode(), RTT))
    except Exception as e:
        print("Request timed out")


