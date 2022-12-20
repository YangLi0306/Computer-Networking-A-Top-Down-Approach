# Lab Wireshark DNS
**实验内容**： 学习使用nslookup，ipconfig工具，理解DNS
**实验文档**： Wireshark_DNS_v8.0.pdf  

### 一、nslookup  
nslookup工具允许运行该工具的主机向任何指定的DNS服务器查询DNS记录。  
**实验步骤：**  
1、运行nslookup以获取一个亚洲的Web服务器的IP地址。该服务器的IP地址是什么？  
以微博为例：  
```
> nslookup weibo.com
服务器:  192.168.2.1
Address:  192.168.2.1

非权威应答:
名称:    weibo.com
Addresses:  2400:89c0:1053:3::55
          2400:89c0:1053:3::54
          49.7.37.76
          49.7.37.77
```
服务器的IP地址如上Addresses后的4个地址  
2、运行nslookup以确定欧洲大学的权威DNS服务器。  
以剑桥大学为例：  
```
> nslookup -type=NS cam.ac.uk
服务器:  192.168.2.1
Address:  192.168.2.1

非权威应答:
cam.ac.uk       nameserver = auth0.dns.cam.ac.uk
cam.ac.uk       nameserver = dns0.cl.cam.ac.uk
cam.ac.uk       nameserver = dns0.eng.cam.ac.uk
cam.ac.uk       nameserver = ns2.ic.ac.uk
cam.ac.uk       nameserver = ns3.mythic-beasts.com
cam.ac.uk       nameserver = ns1.mythic-beasts.com
```
3、运行nslookup，使用问题2中一个已获得的DNS服务器，来查询Yahoo!邮箱的邮件服务器。它的IP地址是什么？  

### 二、ipconfig  
查看主机最近缓存的DNS记录：  
```
ipconfig /displaydns
```
刷新主机DNS缓存：
```
ipconfig /flushdns
```

### 三、使用Wireshark追踪DNS
**实验步骤：**  
1、首先刷新DNS解析缓存，清空浏览器缓存，打开Wireshark，访问http://www.ietf.org   
抓包截图：  
![image](https://user-images.githubusercontent.com/58134113/208651440-8cda6a91-42a8-4492-a052-2b0a956525b9.png)
![image](https://user-images.githubusercontent.com/58134113/208652060-04130bf3-0e50-410d-8bd6-b005ad9ac2c0.png)

2、回答问题  
- 找到DNS查询和响应报文，判断通过UDP或TCP发送？   
  **answer**：通过UDP  
- DNS查询报文的目标端口是什么？DNS响应报文的源端口是什么？   
  **answer**： 均为53号端口
- DNS查询报文发送到哪个IP地址？使用ipconfig确定本地DNS服务器的IP地址。这两个IP地址相同吗？   
  **answer**： 发送到192.168.1.2，使用ipconfig确定本地DNS服务器的IP地址也为192.168.1.2
![image](https://user-images.githubusercontent.com/58134113/208653755-4838db26-34a4-4fe1-8c23-50558cf3d85a.png)

- 检查DNS查询报文。DNS查询的“type”是什么？查询消息是否包含任何“answer”？   
  **answer**：type=A，不包含任何"answer"
![Uploading image.png…]()

- 检查DNS响应报文。提供了多少个“answer”？这些answer都包含什么？   
  **answer**：







