

# why Interface

writing generic algorithm （泛型编程）

hiding implementation detail （隐藏具体实现）

providing interception points

# interface 源码分析

# interface 底层结构

根据 interface 是否包含有 method，底层实现上用两种 struct 来表示：iface 和 eface。
eface表示不含 method 的 interface 结构，或者叫 empty interface。
对于 Golang 中的大部分数据类型都可以抽象出来 _type 结构，同时针对不同的类型还会有一些其他信息。
