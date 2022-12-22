# -*- coding = utf-8 -*-
# @Time: 2022/12/22 14:14
# @File: MailClient.py
# @Software: PyCharm
import base64
from socket import *

msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"
# Choose a mail server (e.g. Google mail server) and call it mailserver
# Fill in start
mailServer = 'smtp.163.com'
mailPort = 25
Username = base64.b64encode(b'**************@163.com').decode()  #163邮箱
Password = base64.b64encode(b'PC***********E').decode() # 163邮箱授权码
#Fill in end

fromAddress = '**************@163.com' #发送方邮箱
toAddress = '***********@qq.com' # 接收方邮箱

# Create socket called clientSocket and establish a TCP connection with mailserver
# Fill in start
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailServer, mailPort))
# Fill in end

recv = clientSocket.recv(1024).decode()
print(recv, end='')
if recv[:3] != '220':
    print('220 reply not received from server.')
# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode())
recv = clientSocket.recv(1024).decode()
print(recv, end='')
if recv[:3] != '250':
    print('250 reply not received from server.')
# send AUTH LOGIN command and print server response.

loginCommand = 'AUTH LOGIN\r\n'
clientSocket.send(loginCommand.encode())
recv = clientSocket.recv(1024).decode()
print(recv, end='')
if recv[:3] != '334':
    print('AUTH LOGIN Wrong! 334 reply not received from server')

clientSocket.sendall((Username+ '\r\n').encode())
recv = clientSocket.recv(1024).decode()
print(recv, end='')
if recv[:3] != '334':
    print('Username Wrong! 334 reply not received from server')

clientSocket.sendall((Password+ '\r\n').encode())
recv = clientSocket.recv(1024).decode()
print(recv, end='')
if recv[:3] != '235':
    print('Password Wrong! 235 reply not received from server')

# Send MAIL FROM command and print server response.
# Fill in start
MailFromCommand = 'MAIL FROM: <' + fromAddress + '> \r\n'
clientSocket.sendall(MailFromCommand.encode())
recv = clientSocket.recv(1024).decode()
print(recv, end='')
if recv[:3] != '250':
    print('Mail From Wrong! 250 reply not received from server')
# Fill in end

# Send RCPT TO command and print server response.
# Fill in start
RcptToCommand = 'RCPT TO: <' + toAddress + '> \r\n'
clientSocket.sendall(RcptToCommand.encode())
recv = clientSocket.recv(1024).decode()
print(recv, end='')
if recv[:3] != '250':
    print('RCPT TO Wrong! 250 reply not received from server.')
# Fill in end

# Send DATA command and print server response.
# Fill in start
DataCommand = 'DATA\r\n'
clientSocket.sendall(DataCommand.encode())
recv = clientSocket.recv(1024).decode()
print(recv, end= " ")
if recv[:3] != '354':
    print('DATA WRONG! 354 reply not received from server.')
# Fill in end

# Send message data.
# Fill in start
sendmsg = 'From: ' + fromAddress + '\r\n'
sendmsg += 'To: ' + toAddress + '\r\n'
sendmsg += 'Subject: ' + 'SMTP Lab' + '\r\n'
sendmsg += msg
clientSocket.sendall((sendmsg).encode())
# Fill in end

# Message ends with a single period.
# Fill in start
clientSocket.sendall(endmsg.encode())
recv = clientSocket.recv(1024).decode()
print(recv, end="")
if (recv[:3] != '250'):
	print('250 reply not received from server')
# Fill in end

# Send QUIT command and get server response.
# Fill in start
QUITCommand = 'QUIT\r\n'
clientSocket.sendall(QUITCommand.encode())
recv = clientSocket.recv(1024).decode()
print(recv, end= " ")
if recv[:3] != '221':
    print('QUIT WRONG! 221 reply not received from server.')
# Fill in end

clientSocket.close()
