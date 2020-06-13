
# HTTP1

## HTTP/1.1 发明以来发生了哪些变化?    

• 从几 KB 大小的消息，到几 MB 大小的消息    
• 每个页面小于 10 个资源，到每页面 100 多个资源    
• 从文本为主的内容，到富媒体(如图片、声音、视频)为主的内容     
• 对页面内容实时性高要求的应用越来越多    

## HTTP/1.1 的高延迟问题    

• 高延迟带来页面加载速度的降低    
• 随着带宽的增加，延迟并没有显著下降    
• 并发连接有限    
• 同一连接同时只能在完成一个 HTTP 事务(请求/响应)才能处理下一个事务    

## 高延迟 VS 高带宽    
• 单连接上的串行请求    
• 无状态导致的高传输量(低网络效率)   

## 无状态特性带来的巨大 HTTP 头部    

• 重复传输的体积巨大的 HTTP 头部

## HTTP/1.1 为了解决性能问题做过的努力    

• Spriting 合并多张小图为一张大图供浏览器 JS 切割使用 ----不能区别对待    
• Inlining 内联，将图片嵌入到 CSS 或者 HTML 文件中，减少网络请求次数    
• Concatenation 拼接，将多个体积较小的 JavaScript 使用 webpack 等工具打包成 1 个体积更大的 JavaScript 文件
    1 个文件的改动导致用户重新下载多个文件    
• Sharding 分片，将同一页面的资源分散到不同域名下，提升连接上限    

## HTTP/1.1 不支持服务器推送消息

# HTTP2

## HTTP/2 有哪些特性?

## 解决 HTTP/1 性能问题的 HTTP/2    

 SPDY(2012-2016)        
 
- SPDY 协议    

因为HTTP/1.x的问题，我们会引入雪碧图、将小图内联、使用多个域名等等的方式来提高性能。
不过这些优化都绕开了协议，直到2009年，谷歌公开了自行研发的 SPDY 协议，主要解决HTTP/1.1效率不高的问题。
谷歌推出SPDY，才算是正式改造HTTP协议本身。降低延迟，压缩header等等，SPDY的实践证明了这些优化的效果，
也最终带来HTTP/2的诞生。

SPDY 协议在Chrome浏览器上证明可行以后，就被当作 HTTP/2 的基础，主要特性都在 HTTP/2 之中得到继承。

HTTP2(RFC7540，2015.5)    
• 在应用层上修改，基于并充分挖掘 TCP 协议性能    
• 客户端向 server 发送 request 这种基本模型不会变。    
• 老的 scheme 不会变，没有 http2://。    
• 使用 http/1.x 的客户端和服务器可以无缝的通过代理方式 转接到 http/2 上。    
• 不识别 http/2 的代理服务器可以将请求降级到 http/1.x   

## 主流浏览器对 HTTP/2 的支持程度

## HTTP/2 的应用状况      
 
截止 2019.5.17 号，互联网上使用 HTTP/2 协议的站点已经达到 37.2%
快速推广的原因    
• 未改变 HTTP/1.1 的语义
• 基于 TCP，仅在应用层变动

## HTTP/2 的强大之处    
• https://http2.akamai.com/demo
http2.akamai.com/demo

# HTTP/2 主要特性

传输数据量的大幅减少 
    
• 以二进制方式传输     
• 标头压缩   
  
多路复用及相关功能   
  
• 消息优先级    
• 服务器消息推送     
• 并行推送    

# 如何使用 Wireshark 解密 TLS/SSL 报文?

Chrome 浏览器检测 HTTP/2 插件    
• HTTP/2 and SPDY indicator
• https://chrome.google.com/webstore/detail/http2-and-spdy- indicator/mpbpobfflnpcgagjijhmgnchggcjblin

在 HTTP/2 应用层协议之下的 TLS 层    

## TLS1.2 的加密算法    

• 常见加密套件
• 对称加密算法:AES_128_GCM
   每次建立连接后，加密密钥都不一样
• 密钥生成算法:ECDHE
    客户端与服务器通过交换部分信息，各自独立生成最终一致的密钥
    
    
## Wireshark 如何解密 TLS 消息?   
 
原理:获得 TLS 握手阶段生成的密钥    
• 通过 Chrome 浏览器 DEBUG 日志中的握手信息生成密钥

步骤    
• 配置 Chrome 输出 DEBUG 日志
• 配置环境变量 SSLKEYLOGFILE
• 在 Wireshark 中配置解析 DEBUG 日志
• 编辑->首选项->Protocols->TLS/SSL 

• (Pre)-Master-Secret log filename

## 二进制格式与可见性    

• TLS/SSL 降低了可见性门槛    
• 代理服务器没有私钥不能看到内容


# 如何从 http://升级到 HTTP/2 协议?

## HTTP/2 是不是必须基于 TLS/SSL 协议?

• IETF 标准不要求必须基于TLS/SSL协议
• 浏览器要求必须基于TLS/SSL协议
• 在 TLS 层 ALPN (Application Layer Protocol Negotiation)扩展做协商，只认 HTTP/1.x 的代理服务器不会干扰 HTTP/2
• shema:http://和 https:// 默认基于 80 和 443 端口
• h2:基于 TLS 协议运行的 HTTP/2 被称为 h2
• h2c:直接在 TCP 协议之上运行的 HTTP/2 被称为 h2c


## h2 与 h2c

## H2C:不使用 TLS 协议进行协议升级(1)

• 客户端测试工具:curl(7.46.0版本) 
     curl http://nghttp/2.org –http/2 -v

## H2C:客户端发送的 Magic 帧  
  
Preface(ASCII 编码，12字节)
何时发送?    
• 接收到服务器发送来的 101 Switching Protocols
• TLS 握手成功后

Preface 内容    
• 0x505249202a20485454502f322e300d0a0d0a534d0d0a0d0a
• PRI * HTTP/2.0\r\n\r\nSM\r\n\r\n
• 发送完毕后，应紧跟 SETTING 帧

## 统一的连接过程

# TODO

# HTTP/2 与 gRPC 框架

## gRPC 测试    

官网:https://grpc.io/
基于 Python 语言搭建测试环境    
    https://grpc.io/docs/quickstart/python/
    测试程序
• git clone -b v1.21.0 https://github.com/grpc/grpc
• cd grpc/examples/python/helloworld
• 服务器:python greeter_ser ver.py
• 客户端:python greeter_client.py

注意
• 欲抓取环回报文，请安装时勾选【install Npcap in Winpcap API-Compatible Mode 】
• 如果 Npcap Loopback Adapter 未抓取到环回报文，请尝试其他接口
• 若 50051 端口未被识别为 http/2，请手动设置“解码为 HTTP/2”


#  HTTP/2 的问题及 HTTP/3 的意义

TCP 以及 TCP+TLS 建链握手过多的问题

## 多路复用与 TCP 的队头阻塞问题

• 资源的有序到达

## TCP的问题       
 
• 由操作系统内核实现，更新缓慢

# QUIC

QUIC 协议在哪一层?

使 Chrome 支持 QUIC
• chrome://flags/#enable-quic

IETF QUIC 协议草案        
• IETF draft 20: https://tools.ietf.org/html/draft-ietf-quic-http-20 
• https://datatracker.ietf.org/doc/draft-ietf-quic-transport/

QUIC 协议组的 Milestones

HTTP3 的连接迁移    

• 允许客户端更换 IP 地址、端口后，仍然可以复用前连接

解决了队头阻塞问题的 HTTP3    

• UDP 报文:先天没有队列概念

# 七层负载均衡


