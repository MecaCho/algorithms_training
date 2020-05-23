
## 四种主要监控方式

	    Metrics 	Logging	  Tracing
CapEx	 Medium	    Low	       High
OpEx	 Low	    High	   Medium
Reaction	High	Medium	    Low
Investigation	Low	Medium	    High



https://peter.bourgon.org/go-for-industrial-programming/

## Metrics监控分层

 系统层---应用层----业务层
 
## Metrics监控架构模式


# BusDevOps和测量驱动开发MDD

《凤凰项目》

## DevOps~CALMS模型

• Culture

• Automation

• Lean

• Measurement 

• Sharing

## DevOps理念:要提升必先测量

If you can not measure it , you can not impore it -----Lord Kelvin

## DevOps实践:研发自助监控

You build it, you run it,
you monitor it.

## 精益创业反馈环

《精益创业》

## 现状

运维人员只专注系统监控(日志，负载度量)， 没有应用监控能力和上下文    
开发人员只管实现功能，没有DevOps和度 量意识    
应用监控空白，对应用状态无感知，主要靠 蒙    
业务对关键应用指标无感知，很多功能开发 了也无人用    


# Metrics Driven Development(MDD)

“... is a practice where metrics are used to drive the entire application development”
是一种实践，主张整个应用开发由度量指标驱动    

• InfoQ/2012
• https://www.infoq.com/articles/metrics-driven-development


## MDD核心原理

开发功能前先定义度量指标(Bus/Dev/Ops)
•Define metrics before development
开发人员自助埋点
•Instrumentation-as-Code
真实性的唯一来源
•Single Source of Truth
关键指标的共同视角
•Shared view of key metrics
使用度量进行决策
•Use metrics when making decisions
开发持续维护指标
•Maintain and follow metrics

## MDD好处

 产品经理
-获取生产实时数据 -数据驱动决策 -BusDevOps意识

研发伙伴
-实时感知生产状态 -聚焦改进点 -BusDevOps意识

运维伙伴
-实时感知生产状态 -快速定位问题 -BusDevOps意识
 

# Prometheus简介

## 什么是Prometheus    

•开源监控工具 

•时间序列数据库TSDB，golang实现 

•Soundcloud研发，源于谷歌borgmon 

•多维度(标签)，拉模式(Pull-based) 

•白盒&黑盒监控都支持，DevOps友好 

•Metrics & Alert，不是
loggging/tracing

•社区生态丰富(多语言，各种exporters)

•单机性能 
    消费百万级时间序列
    上千个targets 

https://prometheus.io/

##  时间序列(Time Series)

 https://db-engines.com/en/ranking_trend/time+series+dbms
 

## Prometheus架构设计

promethues 2.0存储设计是Time Sharding机制，默认2小时一个时间块，
视频里头讲的满了应该指2小时时间间隔到了，这种方式通过时间范围查询定位比较快的，
具体可以参考：https://coreos.com/blog/prometheus-2.0-storage-layer-optimization

### Prometheus 2.0存储设计

https://coreos.com/blog/prometheus-2.0- storage-layer-optimization


## Prometheus基本概念

Metrics种类    
• Counter(计数器)
    始终增加
    http请求数，下单数
    
• Gauge(测量仪)
    当前值的一次快照(snapshot)测量，可增可减 
    磁盘使用率，当前同时在线用户数
    
• Histogram(直方图)
    通过分桶(bucket)方式统计样本分布
    
• Summary(汇总)
    根据样本统计出百分位
    客户端计算

## Scrape metric

## Exporters

OS – Node Exporter • Linux, Windows
• Database
• Mysql, Postgres, CouchDB...
• Messaging
• Kafka, RabbitMQ, NATS...
• Logging
• ElasticSearch, Fluentd, Telegraf...
• Key-Value
• Redis, Memcached...
• WebServer
• Apache, Nginx...
• Proxy
• Haproxy, Varnish...
• DNS
• BIND, PowerDNS, Unbound
• BlackBox

  虚拟机
物理机
  Node Exporter
/metrics
Node Exporter
/metrics
   Redis Redis

https://prometheus.io/docs/instrumenting/exporters/

HTTP错误百分比    

sum(rate(http_requests_total{status="500"}[5m])) by (path) / sum(rate(http_requests_total[5m])) by (path)
{path=“/status”}
{path=“/”} {path=“/api/v1/topics/:topic”} {path=“/api/v1/topics}
0.0039 0.0011 0.087 0.0342

- Alert Definition

4小时内磁盘是否会满?
ALERT DiskWillFullIn4Hours
IF predict_linear(node_filesystem_free[1h], 4*3600) < 0

- Alertmanager
    
Target
Target
Prometheus
Alertmanager

Deduplicaes 去重

Groups 分组

Routes 路由

# 总结





