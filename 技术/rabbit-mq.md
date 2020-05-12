
# 什么时候该使用MQ？

MQ是一个互联网架构中常见的解耦利器。

什么时候不使用MQ？
上游实时关注执行结果，通常采用RPC。
 
什么时候使用MQ？
（1）数据驱动的任务依赖；
（2）上游不关心多下游执行结果；
（3）异步返回执行时间长；

# Kafka、RocketMQ、RabbitMQ都不能保证消息不重不丢（Exactly Once）

消息可靠性的服务水平：

- At most once：至多一次，允许丢消息
- At least once：至少一次，不允许丢消息，可以重复
- Exactly once：恰好一次，不允许丢也不重复
