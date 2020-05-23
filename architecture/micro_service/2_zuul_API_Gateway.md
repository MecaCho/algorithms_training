
# Zuul网关和基本应用场景

API网关是如何演化出来的?

API网关基本功能

单点入口
路由转发
限流熔断
日志监控
安全认证

# Netflix Zuul网关

 
Netflix于2012年初开源
• https://github.com/Netflix/zuul
• Zuul is an edge service that provides dynamic routing, monitoring,
resiliency, security, and more
• 目前Github 5.3k星
    亮点:可动态发布的过滤器机制
• Zuul在英文中是怪兽的意思，寓意看门神兽 • 2014年被Pivotal集成入Spring Cloud体系

Netflix前总架构师Adrian Cockcroft评价：
“One of our most powerful mechanisms and somewhat overlooked NetflixOSS projects is the Zuul gateway service. ”


##  Netflix架构体系和Zuul

ELB

## Netflix使用情况2017

处理大部分 netflix.com的流量
支持超过1000种设备类型
• 支持超过几百种协议和设备版 本的组合

每天处理百亿+请求

超过50+前置ELB

支持3个AWS区域 (regions)

部署超过20+生产 Zuul集群

## 国内公司落地案例

携程：
部署生产实例150+(分集群)
覆盖无线、H5、分销联盟、支 付业务等场景
日流量超50亿

拍拍贷：
部署实例40+(分集群)
覆盖无线、H5、第三方开放平台、 联盟商等场景
日流量超5亿


# Zuul网关高级应用场景


