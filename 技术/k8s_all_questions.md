

1.k8s和docker swarm的不同？

Features	Kubernetes	Docker Swarm
Installation & Cluster Config	Setup is very complicated, but once installed cluster is robust.	Installation is very simple, but the cluster is not robust.
GUI	GUI is the Kubernetes Dashboard.	There is no GUI.
Scalability	Highly scalable and scales fast.	Highly scalable and scales 5x faster than Kubernetes.
Auto-scaling	Kubernetes can do auto-scaling.	Docker swarm cannot do auto-scaling.
Load Balancing	Manual intervention needed for load balancing traffic between different containers and pods.	Docker swarm does auto load balancing of traffic between containers in the cluster.
Rolling Updates & Rollbacks	Can deploy rolling updates and does automatic rollbacks.	Can deploy rolling updates, but not automatic rollback.
DATA Volumes	Can share storage volumes only with the other containers in the same pod.	Can share storage volumes with any other container.
Logging & Monitoring	In-built tools for logging and monitoring.	3rd party tools like ELK stack should be used for logging and monitoring.

Docker Swarm设置起来更方便，但没有强大的集群，而Kubernetes的设置起来更复杂，但是保证了强大的集群的好处
Docker Swarm不能自动缩放（Kubernetes也可以）； 但是，Docker扩展比Kubernetes快五倍
Docker Swarm没有GUI。 Kubernetes具有仪表板形式的GUI
Docker Swarm会对集群中容器之间的流量进行自动负载均衡，而Kubernetes需要手动干预以实现此类流量的负载均衡
Docker需要像ELK堆栈这样的第三方工具来进行日志记录和监控， 而Kubernetes拥有针对该工具的集成工具
Docker Swarm可以轻松地与任何容器共享存储卷，而Kubernetes只能与同一容器中的容器共享存储卷
Docker可以部署滚动更新，但不能部署自动回滚。 Kubernetes可以部署滚动更新以及自动回滚

2.什么是k8s?

3.k8s和Docker的联系？

It’s a known fact that Docker provides the lifecycle management of containers and a Docker image builds the runtime containers. But, since these individual containers have to communicate, Kubernetes is used.  So, Docker builds the containers and these containers communicate with each other via Kubernetes. So, containers running on multiple hosts can be manually linked and orchestrated using Kubernetes.

4.在虚拟机和容器内部署一个应用的区别？

5.什么是容器编排？

6. Kubernetes体系结构的主要组成部分是什么？   

有两个主要组件：主节点和工作节点。 这些组件中的每一个都有单独的组件。

7. Kubernetes中的节点是什么？   

节点是计算硬件的最小基本单元。 它代表集群中的一台机器，可以是数据中心中的物理机，也可以是云提供商提供的虚拟机。 每台机器都可以替代Kubernetes集群中的任何其他机器。 Kubernetes中的主节点控制具有容器的节点。

8.节点状态包含什么？    

节点状态的主要组成部分是地址，条件，容量和信息。

9. Kubernetes主节点上运行什么进程？    

Kube-api服务器进程在主节点上运行，用于扩展更多实例的部署。

10. Kubernetes中的Pod是什么？   

窗格是包装一个或多个容器的高级结构。 这是因为容器不是直接在Kubernetes中运行的。 
同一容器中的容器共享一个本地网络和相同资源，从而使它们可以轻松地与同一容器中的其他容器进行通信，
就像它们在同一台计算机上一样，同时保持一定程度的隔离。

11. kube-scheduler的工作是什么？    

kube调度程序将节点分配给新创建的Pod。

12. Kubernetes中的容器集群是什么？    

容器集群是一组作为节点的机器元素。 群集启动特定的路由，以便在节点上运行的容器可以相互通信。 在Kubernetes中，容器引擎（不是Kubernetes API的服务器）为API服务器提供托管。

13.什么是Google Container Engine？   

Google容器引擎是专为Docker容器和集群量身定制的开源管理平台，旨在为在Google公共云服务中运行的集群提供支持。

14.什么是守护程序集？   

守护程序集是一组在主机上只能运行一次的Pod。 它们用于网络等主机层属性或用于监视网络，您可能不需要在主机上多次运行它们。

15. Kubernetes中的“堆”是什么？    

Heapster是针对Kublet收集的数据的性能监视和指标收集系统。 该聚合器是本地支持的，并且像Kubernetes集群中的任何其他Pod一样运行，这使它可以发现和查询集群中所有节点的使用情况数据。

16. Kubernetes中的命名空间是什么？    

命名空间用于在多个用户之间划分群集资源。 它们适用于许多用户分散在项目或团队中并提供一定范围资源的环境。

17.命名Kubernetes起始的初始名称空间吗？    

default
Kube–sys
kube–

18.什么是Kubernetes控制器管理器？    
控制器管理器是一个守护程序，用于嵌入核心控制循环，垃圾回收和命名空间创建。 即使它们被编译为作为单个进程运行，它也允许在主节点上运行多个进程。

19.控制器管理者有哪些类型？    
可以在主节点上运行的主要控制器管理器是端点控制器，服务帐户控制器，命名空间控制器，节点控制器，令牌控制器和复制控制器。

20.什么是etcd？
Kubernetes使用etcd作为其所有数据（包括元数据和配置数据）的分布式键值存储，并允许Kubernetes集群中的节点读取和写入数据。 尽管etcd是为CoreOS专门构建的，但由于它是开源的，因此它也可以在多种操作系统（例如Linux，BSB和OS X）上运行。 Etcd表示集群在特定时间的状态，并且是用于Kubernetes集群的状态管理和集群协调的规范中心。

21. Kubernetes内有哪些不同的服务？    
不同类型的Kubernetes服务包括：

集群IP服务
节点端口服务
外部名称创建服务和
负载均衡器服务

22.什么是ClusterIP？    

ClusterIP是默认的Kubernetes服务，它提供集群内部的其他应用程序可以访问的集群内部服务（无外部访问权限）。

23.什么是NodePort？    

NodePort服务是将外部流量直接获取到服务的最基本方法。 它在所有节点上打开特定端口，并将发送到该端口的所有流量转发到服务。

24. Kubernetes中的LoadBalancer是什么？    

LoadBalancer服务用于将服务公开到Internet。 例如，网络负载平衡器创建一个IP地址，该IP地址会将所有流量转发到您的服务。

25.什么是无头服务？    

无头服务用于与服务发现机制进行交互，而无需与ClusterIP绑定，因此使您可以直接访问Pod，而不必通过代理访问它们。 当既不需要负载平衡又不需要单个服务IP时，此功能很有用。

26.什么是Kubelet？    
kubelet是一个服务代理，通过通过Kubernetes API服务器监视容器规范来控制和维护一组容器。 它通过确保一组给定的容器都按预期运行，从而保留了pod的生命周期。 kubelet在每个节点上运行，并启用主节点和从节点之间的通信。

27.什么是Kubectl？    

Kubectl是一个CLI（命令行界面），用于对Kubernetes集群运行命令。 因此，它通过Kubernetes组件上的不同创建和管理命令来控制Kubernetes集群管理器

28.举例说明建议的Kubernetes安全措施。    

Kubernetes标准安全措施的示例包括定义资源配额，支持审核，限制对etcd的访问，对环境的定期安全更新，网络分段，严格资源策略的定义，持续扫描安全漏洞以及使用来自授权存储库的映像。

29.什么是Kube-proxy？    

Kube-proxy是负载平衡器和网络代理的实现，用于支持其他网络操作的服务抽象。 Kube-proxy负责根据IP和传入请求的端口号将流量定向到正确的容器。

30.如何获得Kubernetes负载均衡器的静态IP？    

由于Kubernetes Master可以分配新的静态IP地址，因此可以通过更改DNS记录来为Kubernetes负载平衡器获得静态IP。

