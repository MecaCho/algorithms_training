

# LDAP

## 什么是LDAP     

LDAP是Lightweight Directory Access Protocol的缩写，顾名思义，
它是指轻量级目录访问协议（这个主要是相对另一目录访问协议X.500而言的；LDAP略去了x.500中许多不太常用的功能，
且以TCP/IP协议为基础）。

优点包括：

1、可以在任何计算机平台上运行； 

2、通过简单的“推”或“拉”的方式即可复制部分或全部数据，比常见的关系数据库简单很多；

3、主要是面向数据的查询服务，速度比关系数据库快很多；

4、可以使用ACI（类似ACL，访问控制列表）控制对数据的读、写管理，并且是在LDAP服务器内部实现的，
不用担心应用程序Bug问题（相对Web架构来说）；

5、使用类似DNS树的目录树结构，方便多级服务器的连接和管理；

## 什么情况下使用

LDAP中的数据（成为entry，条目），一般是按照地理位置和组织关系进行组织的，
常用于存放需要从不同地点读取，但是不需要经常更新的数据。
大多数的LDAP服务器都为读进行了优化，在读的性能对比上，LDAP服务器会比关系数据库快一个数量级，
但LDAP不适合存储需要经常改变的数据。
所以，LDAP和关系数据库是有区别的。
但也有后台使用关系数据库，中间架设LDAP服务器作为应用接口的情况，以加快用户获取信息的速度。
好像常见的企业级邮件服务器就是这种。

## LDAP的结构    

LDAP中目录是按照树型结构组织的，目录由条目（entry）组成，条目相当于关系数据库中的表；
而条目是包含区别名（DN，Distiguished Name）的属性（Attribute）集合，
而DN相当于关系数据库中的关键字（Primary Key），是区别的标识；
属性就由类型（Type）和多个值（Values）组成，相当于关系数据库中的域是由域名和数据类型组成，
只是不同在于其中的值不像关系数据库中为了降低数据冗余性必须不相关。

LDAP目录最顶层即根部称作“基准DN”，形如”dc=mydomain,dc=org”或者”o= mydomain.org”，
前一种方式更为灵活也是Windows AD中使用的方式。在根目录的下面有很多的文件和目录，
为了把这些大量的数据从逻辑上分开，LDAP像其它的目录服务协议一样使用OU （Organization Unit），
可以用来表示公司内部机构，如部门等，也可以用来表示设备、人员等。同时OU还可以有子OU，用来表示更为细致的分类。

LDAP中每一条记录都有一个唯一的区别于其它记录的名字DN（Distinguished Name）,
其处在“叶子”位置的部分称作RDN；如dn:cn=tom,ou=animals,dc=mydomain,dc=org中tom即为 
RDN；RDN在一个OU中必须是唯一的。

参考；http://hugnew.com/archives/199

# RBAC

以角色为基础的访问控制（Role-based access control，RBAC），是资讯安全领域中，
一种较新且广为使用的访问控制机制，其不同于强制访问控制以及自由选定访问控制、直接赋予使用者权限，
而是将权限赋予角色。
1996年，莱威·桑度（Ravi Sandhu）等人在前人的理论基础上，提出以角色为基础的访问控制模型，
故该模型又被称为RBAC96。
之后，美国国家标准局重新定义了以角色为基础的访问控制模型，并将之纳为一种标准，称之为NIST RBAC。

以角色为基础的访问控制模型是一套较强制访问控制以及自由选定访问控制更为中性且更具灵活性的访问控制技术。

一个主体可对应多个角色。    
一个角色可对应多个主体。    
一个角色可拥有多个权限。    
一种权限可被分配给许多个角色。    
一个角色可以有专属于自己的权限。    

# Habor

Habor是由VMWare公司开源的容器镜像仓库。
事实上，Habor是在Docker Registry上进行了相应的企业级扩展，从而获得了更加广泛的应用，
这些新的企业级特性包括：管理用户界面，基于角色的访问控制 ，AD/LDAP集成以及审计日志等。

容器的核心在于镜象的概念，由于可以将应用打包成镜像，并快速的启动和停止，因此容器成为新的炙手可热的基础设施CAAS，
并为敏捷和持续交付包括DevOps提供底层的支持。

而Habor和Docker Registry所提供的容器镜像仓库，就是容器镜像的存储和分发服务。
之所以会有这样的服务存在，是由于以下三个原因：

- 提供分层传输机制，优化网络传输
Docker镜像是是分层的，而如果每次传输都使用全量文件（所以用FTP的方式并不适合），显然不经济。
必须提供识别分层传输的机制，以层的UUID为标识，确定传输的对象。

- 提供WEB界面，优化用户体验
只用镜像的名字来进行上传下载显然很不方便，需要有一个用户界面可以支持登陆、搜索功能，包括区分公有、私有镜像。

- 支持水平扩展集群
当有用户对镜像的上传下载操作集中在某服务器，需要对相应的访问压力作分解。

# Jenkins

12个可以替代jenkins的CI/CD工具

Jenkins是一个开源的持续集成平台，是DevOps生命周期中的一个重要工具。
但是，与当前的用户界面趋势相比，它的界面已经过时，用户界面也不够友好。
此外，Jenkin配置可能比较复杂，而且它还有许多其他缺点。

Buddy（官网：https://buddy.works）是一款面向web开发人员的智能CI/CD工具，旨在降低进入DevOps的门槛。它使用交付管道来构建、测试和部署软件。这些管道是由100多个现成的动作创建的，这些动作可以以任何方式进行安排——就像您构建一个用砖砌成的房子一样。

CruiseControl(官网：http://cruisecontrol.sourceforge.net)既是CI工具又是可扩展框架。它用于构建自定义的连续构建过程。它有许多用于各种源代码控制、构建技术(包括电子邮件和即时消息)的插件。

Integrity（官网：http://integrity.github.io）是一个持续集成的服务器，它只与GitHub一起工作。在这个CI工具中，每当用户提交代码时，它都会构建并运行代码。它还生成报告并向用户提供通知。

GoCD（官网：https://www.gocd.org）是一个开源的持续集成服务器。它可以方便地建模和可视化复杂的工作流。这个CI工具允许持续交付，并为构建CD管道提供了直观的界面。

IBM UrbanCode Deploy（官网：https://www.ibm.com/ms-en/marketplace/application-release-automation）是一个CI应用程序。它将健壮的可见性、可跟踪性和审计功能合并到一个包中。

AutoRABIT（官网：http://www.autorabit.com/tag/autorabit-download/）是一个端到端的连续交付套件，可以加速开发过程。它简化了整个发布过程。它帮助任何规模的组织实现持续集成。

Circle CI（官网：https://circleci.com/）是一个灵活的CI工具，可以在任何环境下运行，比如跨平台的移动应用程序、Python API服务器或Docker集群。这个工具减少了bug并提高了应用程序的质量。

buildkite agent（官网：https://buildkite.com/）是一个可靠的、跨平台的构建运行程序。这个CI工具使得在您的基础设施上运行自动化构建变得很容易。它主要用于运行构建作业，报告作业的状态代码和输出日志。

TeamCity（官网：https://www.jetbrains.com/teamcity/）是一个持续集成服务器，它支持许多强大的功能。

Bamboo（官网： https://www.atlassian.com/software/bamboo）是一个持续集成构建服务器，可以在一个地方执行自动构建、测试和发布。它与JIRA软件和Bitbucket无缝配合。Bamboo支持许多语言和技术，如CodeDeply、Ducker、Git、SVN、Mercurial、AWS和Amazon S3 bucket。

Strider（官网：https://github.com/Strider-CD/strider）是一个开源工具。它是用Node.JS / JavaScript写的。它使用MongoDB作为备份存储。因此，MongoDB和Node.js对于安装这个CI是必不可少的。该工具为修改数据库模式和注册HTTP路由的不同插件提供支持。

GitLab CI（官网：https://about.gitlab.com/installation/）是GitLab的一部分。它是一个web应用程序，具有将其状态存储在数据库中的API。除了提供GitLab的所有特性之外，它还管理项目并提供友好的用户界面。





