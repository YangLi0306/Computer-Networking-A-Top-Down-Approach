# Lab Wireshark DNS
**实验内容**： 学习使用nslookup，ipconfig工具，理解DNS
**实验文档**： Wireshark_DNS_v8.0.pdf  

### 一、nslookup  
nslookup工具允许运行该工具的主机向任何指定的DNS服务器查询DNS记录。  
**实验步骤：**  
1、运行nslookup以获取一个亚洲的Web服务器的IP地址。该服务器的IP地址是什么？  
以微博为例：  
```
nslookup weibo.com
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
nslookup -type=NS cam.ac.uk
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

### 二、ipconfig  
查看主机最近缓存的DNS记录：  
```
ipconfig /displaydns
```
刷新主机DNS缓存：
```
ipconfig /flushdns
```
未完待续！！！








