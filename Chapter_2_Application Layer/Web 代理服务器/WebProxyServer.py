# -*- coding = utf-8 -*-
# @Time: 2022/12/23 11:47
# @Author: Li Yang
# @File: WebProxyServer.py
# @Software: PyCharm

from socket import *
import sys

# if len(sys.argv) <= 1:
#     print('Usage : "python ProxyServer.py server_ip"\n[server_ip : It is the IP Address Of Proxy Server')
#     sys.exit(2)

# Create a server socket, bind it to a port and start listening
tcpSerSock = socket(AF_INET, SOCK_STREAM)
# Fill in start.
tcpSerSock.bind(('', 6789))
tcpSerSock.listen(5)
# Fill in end.

while 1:
    # Strat receiving data from the client
    print('Ready to serve...')
    tcpCliSock, addr = tcpSerSock.accept()
    print('Received a connection from:', addr)
    message = tcpCliSock.recv(4096).decode()# Fill in start. # Fill in end.

    # Extract the filename from the given message
    filename = message.split()[1].partition("//")[2].replace('/','_')
    print('Filename: ', filename)
    fileExist = "false"

    try:
        # Check wether the file exist in the cache
        f = open(filename, "r")
        outputdata = f.readlines()
        fileExist = "true"
        print("File Exists!")
        # ProxyServer finds a cache hit and generates a response message
        tcpCliSock.send("HTTP/1.0 200 OK\r\n".encode())
        tcpCliSock.send("Content-Type:text/html\r\n".encode())
        # Fill in start.
        for i in range(0, len(outputdata)):
            tcpCliSock.send(outputdata[i].encode())
        # Fill in end.
        print('Read from cache')

    # Error handling for file not found in cache
    except IOError:
        if fileExist == "false":
            # Create a socket on the proxyserver
            c = socket(AF_INET, SOCK_STREAM)# Fill in start. # Fill in end.
            hostn = message.split()[1].partition("//")[2].partition("/")[0]
            print('Host name: ', hostn)
            try:
                # Connect to the socket to port 80
                # Fill in start.
                c.connect((hostn, 80))
                # Fill in end.

                # Read the response into buffer
                # Fill in start.
                c.sendall(message.encode())
                buff = c.recv(4096)
                tcpCliSock.sendall(buff)
                # Fill in end.

                # Create a new file in the cache for the requested file.
                # Also send the response in the buffer to client socket and the corresponding file in the cache
                tmpFile = open("./" + filename,"w")
                # Fill in start.
                tmpFile.writelines(buff.decode().replace('\r\n', '\n'))
                tmpFile.close()
                # Fill in end.
            except:
                print("Illegal request")
        else:
            # HTTP response message for file not found
            # Fill in start.
            tcpCliSock.send("HTTP/1.0 404 NOT FOUND\r\n".encode())
            tcpCliSock.send("\r\n".encode())
            # Fill in end.
    # Close the client and the server sockets
    tcpCliSock.close()

# Fill in start.
tcpSerSock.close()
# Fill in end.
