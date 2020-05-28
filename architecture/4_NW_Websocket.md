
# websocket

WebSocket允许服务器和客户端进行全双工通信，传统的HTTP是单双工通信，它只能允许客户端向服务器发出请求，服务端被动返回数据，而不能主动向客户端传递数据。
WebSocket可以完全取代Ajax，用来向服务器传递字符串，二进制等多种类型的数据，而且还不存在跨域问题。

## 特点

# WebSocket 

WebSocket协议在2008年诞生，2011年成为国际标准。所有浏览器都已经支持了。

最大的特点：服务器可以主动向客户端推送信息，客户端也可以主动向服务器发送信息，是真正的双向平等对话，属于服务器推送技术的一种。

（1）建立在 TCP 协议之上，服务器端的实现比较容易。

（2）与 HTTP 协议有着良好的兼容性。默认端口也是80和443，并且握手阶段采用 HTTP 协议，因此握手时不容易屏蔽，能通过各种 HTTP 代理服务器。

（3）数据格式比较轻量，性能开销小，通信高效。

（4）可以发送文本，也可以发送二进制数据。

（5）没有同源限制，客户端可以与任意服务器通信。

（6）协议标识符是ws（如果加密，则为wss），服务器网址就是 URL。

## 传输流程

为了建立一个 WebSocket 连接，客户端浏览器首先要向服务器发起一个 HTTP 请求，
这个请求和通常的 HTTP 请求不同，包含了一些附加头信息，
其中附加头信息"Upgrade: WebSocket"表明这是一个申请协议升级的 HTTP 请求，
服务器端解析这些附加的头信息然后产生应答信息返回给客户端，
客户端和服务器端的 WebSocket 连接就建立起来了，双方就可以通过这个连接通道自由的传递信息，
并且这个连接会持续存在直到客户端或者服务器端的某一方主动的关闭连接。

## WebSocket的通信协议

WebSocket与TCP、HTTP的关系：WebSocket与http协议一样都是基于TCP的，所以他们都是可靠的协议，
Web开发者调用的WebSocket的send函数在browser的实现中最终都是通过TCP的系统接口进行传输的。

WebSocket和Http协议一样都属于应用层的协议：     
WebSocket在建立握手连接时，数据是通过http协议传输的，但是在建立连接之后，
真正的数据传输阶段是不需要http协议参与的。

## WebSocket的优点

a)、服务器与客户端之间交换的标头信息很小，大概只有2字节;

b)、客户端与服务器都可以主动传送数据给对方;

c)、不用频率创建TCP请求及销毁请求，减少网络带宽资源的占用，同时也节省服务器资源;

## WebSocket的数据传输    

WebScoket协议中，数据以帧序列的形式传输。
若服务器接收到客户端的未经掩码处理的数据帧时，必须主动关闭连接。
若客户端收到经过掩码处理过的数据帧时，必须主动关闭连接，即客户端收到的数据帧不能进行掩码处理。

## WebSocket和HTTP的比较    

相同点：

都属于应用层的协议。    
都使用Request/Response模型进行连接的建立。    
都可以在网络中传输数据。    

不同点：

ws使用HTTP来建立连接，但是定义了一系列新的header域，这些域在HTTP中并不会使用。    
ws连接建立之后，通信双方都可以在任何时刻向另一方发送数据。    
ws连接建立之后，数据的传输使用帧来传递，不再需要Request消息。   
ws的数据帧有序。    


## Ajax轮训

## Websockets

2011。12 RFC6455

• 双向通讯的优劣?
• 如何管理会话?
• 如何维持长连接?
• 兼容 HTTP 协议 • 端口复用
• 支持扩展
• 如 permessage-deflate 扩展

过滤：
ws
is running

管理会话？
如何维持长链接
兼容HTTP：协议升级

### websocket的约束

实时性与可伸缩：
网络效率与无状态：牺牲了简单性与可见性

### 长连接心跳保持

长连接的心跳保持
• HTTP 长连接只能基于简单的超时(常见为 65 秒)
 • WebSocket 连接基于 ping/pong 心跳机制维持
 
### 兼容 HTTP 协议    

• 默认使用 80 或者 443 端口 
• 协议升级
• 代理服务器可以简单支持

### 设计哲学:在 Web 约束下暴露 TCP 给上层    

• 元数据去哪了?
• 对比:HTTP 协议头部会存放元数据
• 由 WebSocket 上传输的应用层存放元数据
• 基于帧:不是基于流(HTTP、TCP)
• 每一帧要么承载字符数据，要么承载二进制数据
• 基于浏览器的同源策略模型(非浏览器无效) • 可以使用 Access-Control-Allow-Origin 等头部
• 基于 URI、子协议支持同主机同端口上的多个服务

### 消息与数据帧
    
- Message 消息     
• 1 条消息由 1 个或者多个帧组成，这些数据帧属于同一类型 • 代理服务器可能合并、拆分消息的数据帧

Frame 数据帧     
• 持续帧    
• 文本帧、二进制帧    

### 发送消息    

• 确保 WebSocket 会话处于 OPEN 状态
• 以帧来承载消息，一条消息可以拆分多个数据帧
• 客户端发送的帧必须基于掩码编码
• 一旦发送或者接收到关闭帧，连接处于 CLOSING 状态
• 一旦发送了关闭帧，且接收到关闭帧，连接处于 CLOSED 状态 • TCP 连接关闭后，WebSocket 连接才完全被关闭

### frame-masking-key 掩码   
     
• 客户端消息:MASK 为 1(包括控制帧)，传递 32 位无法预测的、随机的 Masking-key • 服务器端消息:MASK 为 0

掩码如何防止缓存污染攻击?
• 目的:防止恶意页面上的代码，可以经由浏览器构造出合法的 GET 请求，使得代理服务 器可以识别出请求并缓存响应
• 强制浏览器执行以下方法:
• 生成随机的 32 位 frame-masking-key，不能让 JS 代码猜出(否则可以反向构造)
• 对传输的包体按照 frame-masking-key 执行可对称解密的 XOR 异或操作，使代理服务器不识 别
• 消息编码算法:
• j = i MOD 4
• transformed-octet-i = original-octet-i XOR masking-key-octet-j

### 心跳帧    

• 心跳帧可以插在数据帧中传输 
ping帧    
• opcode=9
• 可以含有数据 
pong帧    
• opcode=A
• 必须与 ping 帧数据相同

### 如何关闭会话？

控制帧中的关闭帧:在 TCP 连接之上的双向关闭     

• 发送关闭帧后，不能再发送任何数据
• 接收到关闭帧后，不再接收任何到达的数据    

关闭帧格式    
• opcode=8
• 可以含有数据，但仅用于解释关

闭会话的原因    
• 前 2 字节为无符号整型
• 遵循 mask 掩码规则

TCP 连接意外中断

###  关闭帧的错误码    

错误码
含义
1000
正常关闭
1001
表示浏览器页面跳转或者服务器将要关机
1002
发现协议错误
1003
接收到不能处理的数据帧(例如某端不能处理二进制消息)
1004
预留
1005
预留(不能用在关闭帧里)，期望但没有接收到错误码
1006
预留(不能用在关闭帧里)，期望给出非正常关闭的错误码
1007
消息格式不符合 opcode(例如文本帧里消息没有用 UTF8 编码)
1008
接收到的消息不遵守某些策略(比 1003、1009 更一般的错误)
1009
消息超出能处理的最大长度
1010
客户端明确需要使用扩展，但服务器没有给出扩展的协商信息
1011
服务器遇到未知条件不能完成请求
1015
预留(不能用在关闭帧里)，表示 TLS 握手失败

# refs

www.websocket.org



