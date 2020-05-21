
# KubeEdge

KubeEdge 是华为捐献给 CNCF 的第一个开源项目，也是全球首个基于 Kubernetes 扩展的，提供云边协同能力的开放式边缘计算平台

KubeEdge 的名字来源于 Kube + Edge，顾名思义就是依托 Kubernetes 的容器编排和调度能力，
实现云边协同、计算下沉、海量设备接入等

依托K8S的容器编排和调度能力,实现云边协同、计算下沉、海量设备的平滑接入。
KubeEdge架构上包含两部分,分别是云端和边缘侧。
云端负责应用和配置的下发,边缘侧则负责运行边缘应用和管理接入设备。

KubeEdge 重点要解决的问题是：

云边协同
资源异构
大规模
轻量化
一致的设备管理和接入体验

## 现状

由于边缘场景通信的不稳定性和严苛的资源消耗限制,导致原生的K8S组件无法直接运行在边缘节点上,例如:工业网关等。
而受限于K8S本身list/watch机制带来的disconnect问题,数据面和管理面断连后,无法做到本地自治。


## 架构

KubeEdge 架构上清晰地分为三层，分别是：云端、边缘和设备层，这是一个从云到边缘再到设备的完整开源边缘云平台

KubeEdge 的云端进程包含以下 2 个组件：

cloudhub 部署在云端，接收 edgehub 同步到云端的信息；        
edgecontroller 部署在云端，用于控制 Kubernetes API Server 
与边缘的节点、应用和配置的状态同步。   


KubeEdge 的边缘进程包含以下 5 个组件：      

edged 是个重新开发的轻量化 Kubelet，实现 Pod，Volume，Node 等 Kubernetes 资源对象的生命周期管理；
metamanager 负责本地元数据的持久化，是边缘节点自治能力的关键；    
edgehub 是多路复用的消息通道，提供可靠和高效的云边信息同步；     
devicetwin 用于抽象物理设备并在云端生成一个设备状态的映射；    
eventbus 订阅来自于 MQTT Broker 的设备数据。    


KubeEdge 是一种完全去中心化的部署模式，管理面部署在云端，
边缘节点无需太多资源就能运行 Kubernetes 的 agent，
云边通过消息协同。
从 Kubernetes 的角度看，边缘节点 + 云端才是一个完整的 Kubernetes 集群。
这种部署模型能够同时满足“设备边缘”和“基础设施边缘”场景的部署要求。

## 优势

- 云边协同

云边协同是 KubeEdge 的一大亮点。
KubeEdge 通过 Kubernetes 标准 API 在云端管理边缘节点、设备和工作负载的增删改查。
边缘节点的系统升级和应用程序更新都可以直接从云端下发，提升边缘的运维效率。
另外，KubeEdge 底层优化的多路复用消息通道相对于 Kubernetes 基于 HTTP 长连接的 list/watch 机制扩展性更好，允许海量边缘节点和设备的接入。KubeEdge 云端组件完全开源，用户可以在任何公有云 / 私有云上部署 KubeEdge 而不用担心厂商锁定，并且自由集成公有云的其他服务。K3S 并不提供云边协同的能力。

- 边缘节点离线自治

与 Kubernetes 集群的节点不同，边缘节点需要在完全断开连接的模式下自主工作，
并不会定期进行状态同步，只有在重连时才会与控制面通信。
此模式与 Kubernetes 管理面和工作节点通过心跳和 list/watch 保持状态更新的原始设计非常不同。

KubeEdge 通过消息总线和元数据本地存储实现了节点的离线自治。
用户期望的控制面配置和设备实时状态更新都通过消息同步到本地存储，
这样节点在离线情况下即使重启也不会丢失管理元数据，
并保持对本节点设备和应用的管理能力。


- 设备管理

KubeEdge 提供了可插拔式的设备统一管理框架，
允许用户在此框架上根据不同的协议或实际需求开发设备接入驱动。
当前已经支持和计划支持的协议有：MQTT，BlueTooth，OPC UA，Modbus 等，
随着越来越多社区合作伙伴的加入，KubeEdge 未来会支持更多的设备通信协议。
KubeEdge 通过 device twins/digital twins 实现设备状态的更新和同步，
并在云端提供 Kubernetes 的扩展 API 抽象设备对象，用户可以在云端使用 kubectl 操作 Kubernetes 资源对象的方式管理边缘设备。


- 轻量化

为了将 Kubernetes 部署在边缘，KubeEdge 和 K3S 都进行了轻量化的改造。
区别在于 K3S 的方向是基于社区版 Kubernetes 不断做减法（包括管理面和控制面），
而 KubeEdge 则是保留了 Kubernetes 管理面，重新开发了节点 agent。
KubeEdge 则完整地保留了 Kubernetes 管理面，没有修改过一行代码。

KubeEdge agent 二进制大小为 62MB，K3S 二进制大小为 36MB。


- 大规模

Kubernetes 原生的可扩展性受制于 list/watch 的长连接消耗，
生产环境能够稳定支持的节点规模是 1000 左右。

KubeEdge 作为华为云智能边缘服务 IEF 的内核，通过多路复用的消息通道优化了云边的通信的性能，
压测发现可以轻松支持 5000+ 节点。
而 K3S 的集群管理技术尚未开源，因为无法得知 K3S 管理大规模集群的能力。


Kubernetes 最初是为云数据中心而设计的，
很多边缘计算场景特殊的问题原生 Kubernetes 无法很好地解决， 
K3S 直接修改 Kubernetes 的代码甚至基础实现机制（例如，使用 SQLite 替换 etcd）的做法仍值得商榷。
关于什么能改，什么不能改以及怎么改？每个用户根据自己的实际需求有各自的观点，而且也很难达成一致。
另外， K3S 这种侵入式的修改能否持续跟进 Kubernetes 上游的发展也是一个未知数。


KubeEdge 是一个从云到边缘再到设备的完整边缘云平台，
它与 Kubernetes 的耦合仅仅是 100% 兼容 Kubernetes 原生 API

