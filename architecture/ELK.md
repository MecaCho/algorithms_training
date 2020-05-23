


# Elasticsearch

Elasticsearch 是一个实时的分布式搜索和分析引擎，它可以用于全文搜索，结构化搜索以及分析。它是一个建立在全文搜索引擎 Apache Lucene 基础上的搜索引擎，使用 Java 语言编写。目前，最新的版本是 2.1.0。

主要特点：

实时分析    
分布式实时文件存储，并将每一个字段都编入索引    
文档导向，所有的对象全部是文档    
高可用性，易扩展，支持集群（Cluster）、分片和复制（Shards 和 Replicas）。
接口友好，支持 JSON    

# Logstash     
Logstash 是一个具有实时渠道能力的数据收集引擎。
使用 JRuby 语言编写。其作者是世界著名的运维工程师乔丹西塞 (JordanSissel)。
目前最新的版本是 2.1.1。

主要特点

几乎可以访问任何数据    
可以和多种外部应用结合   
支持弹性扩展   

它由三个主要部分组成：
Shipper－发送日志数据    
Broker－收集数据，缺省内置 Redis    
Indexer－数据写入    

# Kibana
Kibana 是一款基于 Apache 开源协议，使用 JavaScript 语言编写，
为 Elasticsearch 提供分析和可视化的 Web 平台。
它可以在 Elasticsearch 的索引中查找，交互数据，并生成各种维度的表图。
目前最新的版本是 4.3，简称 Kibana 4。

