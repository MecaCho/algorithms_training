
# 调用链监控业务需求

从单块到微服务

应用监控缺失造成的坑：
线上发布了服务，怎么知道一切正常? 大量报错，到底哪里产生的，谁才是根因? 人工配置错误，通宵排错，劳民伤财!
应用程序有性能问题，怎么尽早发现问题? 数据库问题，在出问题之前能洞察吗?
“网络问题”成为“最好借口”，运维如何反击?
任何可能出问题的地方都会出错!!!(康威定律) 微服务需要应用监控!!!
      

# 调用链监控原理

Google Dapper论文
参考链接 http://research.google.com/p ubs/archive/36356.pdf

Dapper Deployment
Dapper UI

核心概念

概念
含义
Trace
一次分布式调用的链路踪迹
Span
一个方法(局部或远程)调用踪迹
Annotation
附着在Span上的日志信息
Sampling
采样率 

Zipkin：
 https://zipkin.io/
 
Open Tracing：
http://opentracing.io


# 调用链监控产品和比较

  


