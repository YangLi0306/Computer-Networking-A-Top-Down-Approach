# UDP套接字编程
**实验环境：** Windows 10，Python3.8  
**实验内容：** 客户端向服务端发送一段字符串，服务端将所有字母转化为大写，并返回给客户端，客户端输出大写字符串。

**UDPClient.py：** 

```python
from socket import *

serverName = '127.0.0.1'
serverPort = 12000
# 创建套接字，SOCK.DGRAM表示UDP
clientSocket = socket(AF_INET, SOCK_DGRAM)
# 输入要发送的报文，保存在message中
message = input('Input lowercase sentence:')
# encode：字符转字节
clientSocket.sendto(message.encode(), (serverName, serverPort))
# 接收来自服务端数据
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)

print(modifiedMessage.decode())

clientSocket.close()
```

**UDPServer.py：**

```python
from socket import *

serverPort = 12000

serverSocket = socket(AF_INET, SOCK_DGRAM)

serverSocket.bind(('', serverPort))
print("The server is ready to receive")

while True:
    # clientAddress包含客户端IP地址和端口号
    message, clientAddress = serverSocket.recvfrom(2048)
    modifiedMessage = message.decode().upper()
    # 向客户端发送数据
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)
```

**步骤：**  
1、运行UDPServer.py:
![image](https://user-images.githubusercontent.com/58134113/208595432-3573dc2e-778a-4610-94b9-557e9b57202e.png)

2、运行UDPClient.py，输入要发送的字符串 computer network:  
![image](https://user-images.githubusercontent.com/58134113/208596432-7ed379e0-526f-4f43-9edc-24e7efba0450.png)

3、客户端输出返回的大写字符串：
![image](https://user-images.githubusercontent.com/58134113/208596181-71d62e2e-9dc7-46b6-9eef-5af5444af637.png)

