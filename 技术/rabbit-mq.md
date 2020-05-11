

# Kafka、RocketMQ、RabbitMQ都不能保证消息不重不丢（Exactly Once）

消息可靠性的服务水平：

- At most once：至多一次，允许丢消息
- At least once：至少一次，不允许丢消息，可以重复
- Exactly once：恰好一次，不允许丢也不重复
