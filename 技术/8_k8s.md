
# 总体架构

Kubernetes 主要由以下几个核心组件组成：
etcd 保存了整个集群的状态；
kube-apiserver 提供了资源操作的唯一入口，并提供认证、授权、访问控制、API 注册和发现等机制；    
kube-controller-manager 负责维护集群的状态，比如故障检测、自动扩展、滚动更新等；    
kube-scheduler 负责资源的调度，按照预定的调度策略将 Pod 调度到相应的机器上；    
kubelet 负责维持容器的生命周期，同时也负责 Volume（CVI）和网络（CNI）的管理；    
Container runtime 负责镜像管理以及 Pod 和容器的真正运行（CRI），默认的容器运行时为 Docker；    
kube-proxy 负责为 Service 提供 cluster 内部的服务发现和负载均衡；    

# API Server

kube-apiserver 是 Kubernetes 最重要的核心组件之一，主要提供以下的功能：    
- 提供集群管理的 REST API 接口，包括认证授权、数据校验以及集群状态变更等    
- 提供其他模块之间的数据交互和通信的枢纽（其他模块通过 API Server 查询或修改数据，
只有 API Server 才直接操作 etcd）

# kube-scheduler

kube-scheduler 负责分配调度 Pod 到集群内的节点上，它监听 kube-apiserver，查询还未分配 Node 的 Pod，然后根据调度策略为这些 Pod 分配节点（更新 Pod 的 NodeName 字段）。

调度器需要充分考虑诸多的因素：    
- 公平调度    
- 资源高效利用
- QoS
- affinity 和 anti-affinity
- 数据本地化（data locality）
- 内部负载干扰（inter-workload interference）
- deadlines

# Controller Manager

Controller Manager 由 kube-controller-manager 和 cloud-controller-manager 组成，
是 Kubernetes 的大脑，它通过 apiserver 监控整个集群的状态，并确保集群处于预期的工作状态。

# Kubelet    

每个Node节点上都运行一个 Kubelet 服务进程，默认监听 10250 端口，接收并执行 Master 发来的指令，
管理 Pod 及 Pod 中的容器。每个 Kubelet 进程会在 API Server 上注册所在Node节点的信息，
定期向 Master 节点汇报该节点的资源使用情况，并通过 cAdvisor 监控节点和容器的资源。

## 节点管理      
 
节点管理主要是节点自注册和节点状态更新：
Kubelet 可以通过设置启动参数 
--register-node 来确定是否向 API Server 注册自己；
如果 Kubelet 没有选择自注册模式，则需要用户自己配置 Node 资源信息，
同时需要告知 Kubelet 集群上的 API Server 的位置；
Kubelet 在启动时通过 API Server 注册节点信息，并定时向 API Server 发送节点新消息，API Server 在接收到新消息后，将信息写入 etcd

