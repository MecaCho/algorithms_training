

# gRPC有什么好处以及在什么场景下需要用gRPC

gRPC和restful API都提供了一套通信机制，用于server/client模型通信，而且它们都使用http作为底层的传输协议(严格地说, gRPC使用的http2.0，而restful api则不一定)。不过gRPC还是有些特有的优势，如下：

- gRPC可以通过protobuf来定义接口，从而可以有更加严格的接口约束条件。    
- 通过protobuf可以将数据序列化为二进制编码，这会大幅减少需要传输的数据量，从而大幅提高性能。    
- gRPC可以方便地支持流式通信(理论上通过http2.0就可以使用streaming模式, 
    但是通常web服务的restful api似乎很少这么用，通常的流式数据应用如视频流，
    一般都会使用专门的协议如HLS，RTMP等，这些就不是我们通常web服务了，而是有专门的服务器应用。）


# Protobuf是什么

Protobuf是Protocol Buffers的简称，它是Google公司开发的一种数据描述语言，并于2008年对外开源。Protobuf刚开源时的定位类似于XML、JSON等数据描述语言，通过附带工具生成代码并实现将结构化数据序列化的功能。但是我们更关注的是Protobuf作为接口规范的描述语言，可以作为设计安全的跨语言PRC接口的基础工具。

Protobuf有如下优点：

- 足够简单
- 序列化后体积很小:消息大小只需要XML的1/10 ~ 1/3
- 解析速度快:解析速度比XML快20 ~ 100倍
- 多语言支持
- 更好的兼容性,Protobuf设计的一个原则就是要能够很好的支持向下或向上兼容

