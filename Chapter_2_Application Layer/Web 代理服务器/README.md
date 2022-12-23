# Web 代理服务器
**实验文档：** [HTTP Web Proxy Server Lab](https://gaia.cs.umass.edu/kurose_ross/programming/Python_code_only/Web_Proxy_programming_only.pdf)  
**实验环境：** Python3.8, Windows 10, Ubuntu18.04

### Web Proxy Server Code
Web Proxy Server代码，实验文档中给出部分，按照要求补全，见[WebProxyServer.py](https://github.com/YangLi0306/Computer-Networking-A-Top-Down-Approach/blob/main/Chapter_2_Application%20Layer/Web%20%E4%BB%A3%E7%90%86%E6%9C%8D%E5%8A%A1%E5%99%A8/WebProxyServer.py)

### 结果展示
用Windows主机浏览器发出请求，用虚拟机Ubuntu 18.04作为代理服务器

首先，没有设置代理服务器，访问 http://gaia.cs.umass.edu/wireshark-labs/HTTP-wireshark-file1.html， 可以正常访问：
![image](https://user-images.githubusercontent.com/58134113/209283096-c5cad9c7-6b26-4d8c-a3cb-87176ce0c3d5.png)

然后设置代理，访问网站，无法访问：
![image](https://user-images.githubusercontent.com/58134113/209296896-5b744cf4-5d86-4c42-9ef6-c7bc88bb3d11.png)
![1](https://user-images.githubusercontent.com/58134113/209297047-1129023e-3ade-423d-9304-090bb3d59512.png)


在Ubuntu上运行代理服务器后，可以正常访问：  
![2](https://user-images.githubusercontent.com/58134113/209297126-0a2756a4-96b9-4913-865d-64351f1f5f0b.png)
![image](https://user-images.githubusercontent.com/58134113/209297243-931a99f1-7340-478c-88f6-2524e32c2dcf.png)

并且，代理服务器保存了该html页面：  
![4](https://user-images.githubusercontent.com/58134113/209297621-9a91cd31-f325-428b-8e90-00263f321bfc.png)


再次访问该html页面时，代理服务器中保存了该html，直接发送
![6](https://user-images.githubusercontent.com/58134113/209297511-891d3318-f747-4d99-a037-019534a2e4cd.png)


