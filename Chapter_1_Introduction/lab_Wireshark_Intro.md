 # Lab Wireshark Intro
**实验内容：** 学习熟悉使用Wireshark， 访问一个Web站点，捕获并检查在你的Web浏览器和Web服务器之间交换的协议报文。
**实验文档：** Wireshark_Intro_v8.0.pdf

**实验步骤：**  
1、首先打开Wireshark捕获数据包，然后访问http://gaia.cs.umass.edu/wireshark-labs/INTRO-wireshark-file1.html ；  
2、使用Wireshark的过滤功能，输入"http"，得到下图；
![image](https://user-images.githubusercontent.com/58134113/208224441-ae144a50-bfef-4f6e-8a2f-904010382403.png)
3、回答实验中的问题；  
- 列出上述步骤中出现在未过滤的分组列表窗口的协议列中的3种不同的协议？  
  **answer**: HTTP协议，TCP协议，DNS协议  
  
- 从HTTP GET消息发送到HTTP OK回复需要多长时间？  
  **answer**：GET时间为：Dec 17, 2022 11:56:07.736196，HTTP OK时间为：Dec 17, 2022 11:56:07.993217，所以从HTTP GET消息发送到HTTP OK回复需要0.257021秒
  
- gaia.cs.umass.edu(也称为www.net.cs.umass.edu)的Internet地址是什么？您的计算机的Internet地址是什么？  
  **answer**：gaia.cs.umass.edu地址为：128.119.245.12，我的计算机地址为：192.168.1.111
  
- 打印第二个问题中提到的两个HTTP消息(GET和OK)  
  **answer**：  
  HTTP GET：
  ![image](https://user-images.githubusercontent.com/58134113/208225506-f5485966-8cf9-40c6-8aad-bd794ab0ccdc.png)
  HTTP OK：  
  ![image](https://user-images.githubusercontent.com/58134113/208225530-7ca79323-8741-4c0e-b619-bf74c10d665a.png)

  

