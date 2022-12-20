# Lab Wireshark DNS
**实验内容**： 理解DNS  
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
```
nslookup -type=MX yahoo.com dns0.cl.cam.ac.uk
网络原因，没找到
```
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
![image](https://user-images.githubusercontent.com/58134113/208655200-8d3cbee9-f617-4735-a17c-f963b168e0e2.png)


- 检查DNS响应报文。提供了多少个“answer”？这些answer都包含什么？   
  **answer**：3个 answer, 包含如下：  
  ![image](https://user-images.githubusercontent.com/58134113/208655310-84724285-47ab-4759-859d-ae7be25b8d9f.png)
- 考虑主机发送的后续TCP SYN数据包。SYN数据包的目标IP地址是否对应于DNS响应报文中提供的任何IP地址？  
  **answer**：SYN数据包的目标地址为104.16.45.99，对应DNS响应报文中提供的任何IP地址
![image](https://user-images.githubusercontent.com/58134113/208656104-b503c662-3ef0-4f7d-a3e2-193214547b49.png)
- 此网页包含图像。在检索每个图像之前，主机是否发出新的DNS查询？  
  **answer**：没有发出新的DNS查询  

3、打开Wireshark，使用nslookup查询www.mit.edu
cmd命令：  
![image](https://user-images.githubusercontent.com/58134113/208657215-261da83b-8c54-478b-8114-c797d1dd8de8.png)

抓包截图：
![image](https://user-images.githubusercontent.com/58134113/208657185-ee6ef81b-5b07-40a1-b451-68c0f45ccb43.png)

4、回答问题  
- DNS查询报文的目标端口是什么？DNS响应报文的源端口是什么？   
  **answer**：均为53号端口  
- DNS查询报文发送到哪个IP地址？这是默认本地DNS服务器的IP地址吗？  
  **answer**: 发送到192.168.1.2，使用ipconfig确定本地DNS服务器的IP地址也为192.168.1.2  
![image](https://user-images.githubusercontent.com/58134113/208653755-4838db26-34a4-4fe1-8c23-50558cf3d85a.png)   
- 检查DNS查询报文。DNS查询的“type”是什么？查询消息是否包含任何“answer”？   
  **answer**：type=A，不包含任何"answer"  
 ![image](https://user-images.githubusercontent.com/58134113/208657949-99fd63eb-510f-4c48-95b2-f026842aa2ca.png)
- 检查DNS响应报文。提供了多少个“answer”？这些answer都包含什么？   
  **answer**：1个 answer, 包含如下：   
  ![image](https://user-images.githubusercontent.com/58134113/208658217-b37cc0f2-e9f0-4f6d-93b9-43464c3c621d.png)
- 实验截图？  
![image](https://user-images.githubusercontent.com/58134113/208658426-2e51495d-fd9c-4f40-bb68-e06fc20e5a17.png)


5、打开Wireshark, cmd输入：nslookup –type=NS mit.edu  
cmd截图：  
![image](https://user-images.githubusercontent.com/58134113/208658926-70ea436a-af23-483c-83b7-b9791e043bda.png)

6、回答问题  
- DNS查询报文发送到哪个IP地址？这是默认本地DNS服务器的IP地址吗？  
  **answer**: 发送到192.168.1.2，是默认DNS服务器的IP地址  
- 检查DNS查询报文。DNS查询的“type”是什么？查询消息是否包含任何“answer”？   
  **answer**：type=NS，不包含任何"answer"   
  ![image](https://user-images.githubusercontent.com/58134113/208659368-4b212d46-476e-490d-9505-6e072dd14583.png)
- 检查DNS响应报文，提供了哪些MIT nameserver？此响应报文是否还提供了MIT名称者的IP地址？  
   **answer**： MIT nameserver 如图：  
  ![image](https://user-images.githubusercontent.com/58134113/208659925-2cf3454c-072e-424e-b80e-e198167c3a55.png)  
   响应报文提供了MIT名称者的IP地址  
 ![image](https://user-images.githubusercontent.com/58134113/208660085-23f05e03-62b9-4b1f-809a-a085f1cd9080.png)
 - 实验截图？  
 ![image](https://user-images.githubusercontent.com/58134113/208660244-6541c2f7-62f6-462d-8bb5-2ae2706e91d7.png)

7、 打开Wireshark, cmd输入，nslookup www.aiit.or.kr bitsy.mit.edu  
cmd截图：  
![image](https://user-images.githubusercontent.com/58134113/208661140-a5a9f500-d525-4abb-aa1b-0a5ae0eca595.png)

8、回答问题  
- DNS查询报文发送到哪个IP地址？这是默认本地DNS服务器的IP地址吗？如果没有，IP地址对应于什么？  
  **answer**：DNS查询消息先发送到默认本地DNS服务器192.168.2.1(默认本地DNS服务器的IP地址)，查询bitsy.mit.edu的IP地址，查询消息再发送到IP地址18.0.72.3(bitsy.mit.edu的IP地址)  
  ![image](https://user-images.githubusercontent.com/58134113/208661377-930c9866-47de-4a08-8f04-d19c10b84136.png)
- 检查DNS查询报文。DNS查询的“type”是什么？查询消息是否包含任何“answer”？   
  **answer**：type=A，不包含任何"answer"   
![image](https://user-images.githubusercontent.com/58134113/208661998-8f19e94c-22de-4f8c-95ad-6fc3b3cb8f5f.png)
- 检查DNS响应报文。提供了多少个“answer”？这些answer都包含什么？   
  **answer**：网络原因，没有收到，请求超时
- 实验截图？  
![image](https://user-images.githubusercontent.com/58134113/208662889-f51deb79-62f8-4ba5-aca1-c5e73e8b6ff6.png)





