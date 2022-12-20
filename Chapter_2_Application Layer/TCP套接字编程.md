# TCP套接字编程
**实验环境：** Windows 10，Python3.8  
**实验内容：** 客户端向服务端发送一段句子，服务端将所有字母转化为大写，并返回给客户端，客户端输出大写句子。

**TCPClient.py：** 

```python
from socket import *

serverName = '127.0.0.1'
serverPort = 12000
# 创建套接字，SOCK.STREAM表示TCP
clientSocket = socket(AF_INET, SOCK_STREAM)
# 创建TCP连接
clientSocket.connect((serverName, serverPort))

# 输入要发送的句子
sentence = input('Input lowercase sentence:')
# 发送给服务端
clientSocket.send(sentence.encode())
# 接收来自服务端数据
modifiedSentence = clientSocket.recv(1024)

print('From Server: ', modifiedSentence.decode())

clientSocket.close()
```

**TCPServer.py：**

```python
from socket import *

serverPort = 12000

serverSocket = socket(AF_INET, SOCK_STREAM)

serverSocket.bind(('', serverPort))
# 服务器聆听来自客户的TCP连接请求。其中参数定义了请求连接的最大数(至少为1)
serverSocket.listen(1)

print("The server is ready to receive")

while True:
    # 创建新套接字，为特定用户专用
    connectionSocket, addr = serverSocket.accept()
    sentence = connectionSocket.recv(1024).decode()
    capitalizedSentence = sentence.upper()
    connectionSocket.send(capitalizedSentence.encode())
    connectionSocket.close()

```

**步骤：**  
1、运行TCPServer.py:
![image](https://user-images.githubusercontent.com/58134113/208599209-f59dbb4d-6f99-4865-998f-5450398e43d5.png)

2、运行TCPClient.py，输入要发送的句子:  
![image](https://user-images.githubusercontent.com/58134113/208599361-580e2a3f-0b08-438a-8728-cb1bc06417b4.png)

3、客户端输出返回的大写句子：
![image](https://user-images.githubusercontent.com/58134113/208599606-18b88a37-a3c0-4b29-9a9a-b4e5c0cff4e7.png)


