 # Lab Wireshark HTTP
**实验内容：** 使用Wireshark，探讨HTTP协议  
**实验文档：** [Wireshark_HTTP_v8.0.pdf](http://www-net.cs.umass.edu/wireshark-labs/Wireshark_HTTP_v8.0.pdf)  

### 一、基本HTTP GET/response交互
**实验步骤：**   
1、打开Wireshark，访问http://gaia.cs.umass.edu/wireshark-labs/HTTP-wireshark-file1.html  
  抓包截图：  
![image](https://user-images.githubusercontent.com/58134113/208278382-a8b5588a-1e72-4f1c-8d02-beba2aff0055.png)

2、查看HTTP Get报文和响应报文信息，回答问题  

![image](https://user-images.githubusercontent.com/58134113/208278717-f7115be6-8a05-455d-af47-09f16333f341.png)

- 浏览器和服务器的HTTP版本，1.0还是1.1？   
  **answer**：HTTP 1.1  
- 您的浏览器表示服务器可以接受哪些语言（如果有的话）？  
  **answer**：Accept-Language: zh-CN  
- 浏览器的IP地址和gaia.cs.umass.edu的IP地址？  
  **answer**：浏览器IP地址：192.168.1.110，gaia.cs.umass.eduIP地址：128.119.245.12  
- 从服务器返回到浏览器的状态码是什么？  
  **answer**：200 OK  
- HTML文件上次在服务器上修改的时间是什么时候？  
  **answer**：Sat, 17 Dec 2022 06:59:01 GMT\r\n
- 有多少字节的内容被返回到您的浏览器？  
  **answer**：128 bytes
- 通过检查数据包内容窗口中的原始数据，您是否看到数据包列表窗口中没有显示的数据头？如果是，请说出一个。  
  **answer**：没有

### 二、HTTP条件GET/响应交互
**实验步骤：**    
1、打开Wireshark，访问一次http://gaia.cs.umass.edu/wireshark-labs/HTTP-wireshark-file2.html，再刷新一次，请求第二次
  抓包截图：  
  ![image](https://user-images.githubusercontent.com/58134113/208279006-3e150ed7-8531-4b8c-b476-5f21540ba42e.png)
  
2、查看报文，回答问题  
  第一次请求：  
![image](https://user-images.githubusercontent.com/58134113/208279060-1b7f7fd1-06f0-49fd-bdd2-ab076ce43ed5.png)
  第二次请求：  
![image](https://user-images.githubusercontent.com/58134113/208279066-a956e592-c331-4dfd-9692-5efa37656c26.png)

- 检查从浏览器到服务器的第一个HTTP GET请求的内容。您在HTTP GET中看到“IF-MODIFIED-SINCE”行吗？  
  **answer**：没有看到“IF-MODIFIED-SINCE”  
- 检查服务器响应的内容。服务器是否显式返回文件的内容？你怎么知道？  
  **answer**：服务器返回text/html，在实体中可以看到   
- 检查从浏览器到服务器的第二个HTTPGET请求的内容。您是否在HTTP GET中看到“IF-MODIFIED-SINCE:”行？如果是，“If-MODIFIED-SINCE:”标题后面有什么信息？  
  **answer**：看到“IF-MODIFIED-SINCE:”，后面内容是Sat, 17 Dec 2022 06:59:01 GMT  
- 服务器响应第二次HTTP GET返回的HTTP状态码和短语是什么？服务器是否显式返回文件的内容？解释？  
  **answer**：状态码：304，短语是：304 Not Modified，服务器没有显式返回文件的内容，因为文件后来没有被修改
  
### 三、检索长文档
**实验步骤：**
1、打开Wireshark，访问http://gaia.cs.umass.edu/wireshark-labs/HTTP-wireshark-file3.html   
  抓包截图：  
![image](https://user-images.githubusercontent.com/58134113/208286846-b7a4dc45-ecde-497c-aa24-4351a47717c5.png)

2、查看并回答问题
- 您的浏览器发送了多少HTTP GET请求报文？跟踪中的哪个数据包编号包含权力法案的Get消息？  
  **answer**：发送了1个HTTP GET请求报文，编号299
- 跟踪中的哪个数据包编号包含与HTTP GET请求响应相关联的状态码和短语？  
  **answer**：编号328包含与HTTP GET请求响应相关联的状态码和短语
- 回复中的状态码和短语是什么？  
  **answer**：状态码：200，短语：OK
- 需要多少包含TCP段的数据才能承载单个HTTP响应的权利法案文本？  
  **answer**：使用了3个TCP段，剩余的数据放在响应报文中
  
### 四、带有嵌入对象的HTML文档
 **实验步骤：**
1、打开Wireshark，访问http://gaia.cs.umass.edu/wireshark-labs/HTTP-wireshark-file4.html   
  抓包截图：  
![image](https://user-images.githubusercontent.com/58134113/208287242-39c44383-397c-4304-863c-622172c5450e.png)

2、查看并回答问题
- 您的浏览器发送了多少HTTP GET请求报文？这些GET请求发送到了哪些Internet地址？  
  **answer**: 发送了3个HTTP GET请求报文，请求地址为：128.119.245.12，178.79.137.164
- 你能分辨出你的浏览器是串行下载这两张图片，还是从这两个网站并行下载？解释？  
  **answer**: 串行下载，第一个图片接收到之后才发送第二个图片的请求报文  
 
 ### 五、HTTP认证
 **实验步骤：**
 1、打开Wireshark，访问http://gaia.cs.umass.edu/wireshark-labs/protected_pages/HTTP-wireshark-file5.html  
   抓包截图：  
 ![image](https://user-images.githubusercontent.com/58134113/208287792-9c8b5a71-8683-4632-9af8-d6cdedb55397.png)
 
 2、 查看并回答问题  
 - 服务器对来自浏览器的初始HTTP GET消息的响应（状态码和短语）是什么？  
   **answer**：状态码：401，短语：Unauthorized
 - 当您的浏览器第二次发送HTTP GET消息时，HTTP GET消息中包含哪些新字段？  
   **answer**：Authorization: Basic d2lyZXNoYXJrLXN0dWRlbnRzOm5ldHdvcms=

  
