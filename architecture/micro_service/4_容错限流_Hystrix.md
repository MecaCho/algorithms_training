
# 基本的容错模式

超时：主动超时

限流：限制最大并发数

熔断：错误数达到域值

降级：服务降级

隔离：隔离不同依赖调用

## 断路器模式

状态机：
关闭----打开----半开闭

## 舱壁隔离模式

Bulkhead Pattern
失败单元的隔离

# 容错理念

- 凡是依赖都可能失败
- 凡是资源都有限制（CPU/MEM/Threads/Queue）
- 网络不可靠
- 延迟是应用稳定性杀手

弹性理念（Resilience）
工程师需要弹性思维

# Netflix Hystrix

Netflix Hystrix背景介绍

• Hystrix源于Netflix API团队在2011年启动的弹性工程项目，目前(2013)它在 Netflix每天处理数百亿的线程隔离以及数千亿的信号量隔离调用
• http://www.infoq.com/cn/news/2013/01/netflix-hystrix-fault-tolerance
• Hystrix是基于Apache License 2.0协议的开源库，目前托管在github上，当前
 超过1.4万颗星
• https://github.com/Netflix/Hystrix
  • Netflix云端开源工具Hystrix曾助奥巴马竞选
• http://it.sohu.com/20121129/n358943361.shtml

Hystrix主要作者：

Ben Christensen
https://www.linkedin.com/in/benjchristensen


# Hystrix设计原理

 Hystrix工作流程(自适应反馈机)
 
 断路器内核
 
 
# Hystrix主要概念

Hystrix Command
Fail Fast
Fail Silent
Static Fallback
Fallback via Network
Primary + Secondary with Fallback
请求合并
请求缓存


# 信号量vs线程池隔离

线程和信号量隔离
线程隔离案例
防雪崩利器:熔断器Hystrix的原理与使用
https://segmentfault.com/a/1190000005988895

信号量隔离 

• 优点
• 轻量，无额外开销 
• 不足
• 不支持任务排队和主动超时
• 不支持异步调用 
• 适用
• 受信客户
• 高扇出(网关)
• 高频高速调用(cache)

线程池隔离 

• 优点
• 支持排队和超时
• 支持异步调用 
• 不足
• 线程调用会产生额外的开销 
• 适用
• 不受信客户 
• 有限扇出


