# Lab Wireshark UDP
**实验内容**： 学习UDP 
**实验文档**： [Wireshark_UDP_v8.0.pdf](http://www-net.cs.umass.edu/wireshark-labs/Wireshark_UDP_v8.0.pdf)

**实验步骤：**  
1、使用Wireshark捕获数据包

2、回答下列问题 
- 从跟踪中选择一个UDP数据包。根据此数据包，确定UDP标头中有多少字段，说出这些字段的名称。  
  **answer**：Sources Port, Destination Port, Length, Checksum  
  ![image](https://user-images.githubusercontent.com/58134113/209455003-cedcc541-227f-4a0a-a16e-498d1cc8b560.png)  

- 通过查阅Wireshark数据包内容字段中显示的信息，确定每个UDP报头字段的长度（以字节为单位）。  
  **answer**：8 bytes  
- 长度字段中的值是什么的长度？。使用捕获的UDP数据包验证您的声明。  
  **answer**：长度字段中的值是指的是 UDP首部+负载的字节数，如下图长度123为UDP首部的8字节和负载115字节之和。  
  ![image](https://user-images.githubusercontent.com/58134113/209455055-9f0720d1-e928-41e2-9a16-d05a9ab133c7.png)  

- UDP负载中可包含的最大字节数是多少？  
  **answer**: 最大字节数：2<sup>16</sup> - 8，Length占2字节，所能表示的最大数为2<sup>16</sup>，因为UDP首部固定8字节，所以UDP负载为长度最大值减去首部8字节。  
- 最大可能的源端口号是多少？  
  **answer**：端口号2字节，16比特，所以最大可能源端口号为2<sup>16</sup> - 1   
- UDP 的协议号是什么？ 以十六进制和十进制表示法给出答案。 要回答这个问题，您需要查看包含此 UDP 段的 IP 数据报的 Protocol 字段。  
  **answer**：UDP协议号：17(十进制)，0x11(十六进制)  
  ![image](https://user-images.githubusercontent.com/58134113/209455162-8290d3a5-b8e3-4eca-b185-af67b0e28733.png)  

- 检查一对UDP数据包，其中主机发送第一个UDP数据包并且第二个UDP数据包包括对第一个UDP包的答复。描述两个数据包中端口号之间的关系。  
  **answer**: 第一个数据包的源端口号是第二个数据包的目标端口号， 第二个数据包的源端口号是第一个数据包的目标端口号
  第一个UDP数据包：  
![image](https://user-images.githubusercontent.com/58134113/209455192-defa9d6c-f5ac-4805-aba3-3e7156c6e4ec.png)  
  第二个UDP数据包（对第一个的答复）：  
![image](https://user-images.githubusercontent.com/58134113/209455199-3fb4a78c-af56-4ae6-a57a-2badd569e5af.png)



