
# TLS/SSL协议的工作原理

TLS 设计目的    

• 身份验证 
• 保密性
• 完整性

## TLS/SSL 发展

SSL3.0(1995)

TLS1.0(1999)

TLS1.0(2006)

TLS1.0(2008)

TLS1.0(2018)

## TLS 协议    

Record 记录协议     
• 对称加密    

Handshake 握手协议    

• 验证通讯双方的身份

• 交换加解密的安全套件 

• 协商加密参数

## TLS 安全密码套件解读

TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256

密钥交换算法
身份验证算法 
对称加密算法、强度、工作模式
签名hash算法

## 对称加密的工作原理(1):XOR 与填充

### 对称加密

### AES 对称加密在网络中的应用

### 对称加密与 XOR 异或运算

对称加密的核心

### 填充 padding    

Block cipher 分组加密:将明文分成多个等长的 Block 模块，对每个模块分别加解密
目的:当最后一个明文 Block 模块长度不足时，需要填充

填充方法：    
• 位填充:以 bit 位为单位来填充
    • ... | 1011 1001 1101 0100 0010 0111 0000 0000 |
• 字节填充:以字节为单位为填充
    • 补零:...|DDDDDDDDDDDDDDDD|DDDDDDDD00000000|
    • ANSIX9.23:...|DDDDDDDDDDDDDDDD|DDDDDDDD00000004|
    • ISO10126:...|DDDDDDDDDDDDDDDD|DDDDDDDD81A62304|
    • PKCS7(RFC5652):...|DDDDDDDDDDDDDDDD|DDDDDDDD04040404|


# 对称加密的工作原理(2):工作模式

分组工作模式 block cipher mode of operation
• 允许使用同一个分组密码密钥对多于一块的数据进行加密，并保证其安全性

## ECB(Electronic codebook)模式    

• 直接将明文分解为多个块，对每个块独立 加密
• 问题:无法隐藏数据特征

## CBC(Cipher-block chaining)模式

• 每个明文块先与前一个密文块进行异或后，再进行加密     
• 问题:加密过程串行化

## CTR(Counter)模式        
• 通过递增一个加密计数器以产生连续的密钥流     
• 问题:不能提供密文消息完整性校验    

## 验证完整性:hash 函数

## 验证完整性:MAC(Message Authentication Code)

GCM
• Galois/Counter Mode • CTR+GMAC

# 详解AES对称加密算法

AES(Advanced Encryption Standard)加密算法    
• 为比利时密码学家 Joan Daemen 和 Vincent Rijmen 所设计，又称 Rijndael 加密算法 
• 常用填充算法:PKCS7
• 常用分组工作模式:GCM   

AES 的三种密钥长度    
• AES分组长度是 128 位(16 字节)

## AES 的加密步骤    

1. 把明文按照 128bit(16 字节)拆分成若干个明文块，每个明文块是 4*4 矩阵     
2. 按照选择的填充方式来填充最后一个明文块   
3. 每一个明文块利用 AES 加密器和密钥，加密成密文块    
4. 拼接所有的密文块，成为最终的密文结果

## 

# TODO

# 非对称密码与 RSA 算法

非对称密码
• 每个参与方都有一对密钥 
• 公钥
• 向对方公开 
• 私钥
• 仅自己使用

非对称加解密的过程
• 加密
• 使用对方的公钥加密消息
• 解密
• 使用自己的私钥解密消息

## RSA 算法    

• 1977 年由罗纳德·李维斯特(Ron Rivest)、阿迪·萨莫尔(Adi Shamir)和伦纳德·阿德曼 (Leonard Adleman)一起提出，因此名为 RSA 算法

## RSA 算法中公私钥的产生    

1. 随机选择两个不相等的质数 p 和 q
2. 计算p和q的乘积n(明文小于n)
3. 计算 n 的欧拉函数 v=φ(n)
4. 随机选择一个整数 k
• 1<k<v，且k与v互质
5. 计算k对于v的模反元素d
6. 公钥:(k,n)
7. 私钥: (d,n)

## RSA 算法加解密流程    
• 加密:c ≡ mk (mod n) • m 是明文，c 是密文
• 解密:m ≡ cd (mod n)
• 举例:对明文数字 123 加解密
• 公钥(3,319)加密
• 1233mod319=140
• 对140密文用私钥(187,319)解密 • 140187mod319=123
• 私钥(187,319)加密
• 123187mod319=161
• 公钥(3,319)解密
• 1613mod319=123

# 基于 openssl 实战验证 RSA

## 使用 openssl 基于 RSA 算法生成公私钥(1)

生成私钥(公私钥格式参见 RFC3447)     
• openssl genrsa -out private.pem

使用 openssl 基于 RSA 算法生成公私钥(2)    
• 从私钥中提取出公钥    
• openssl rsa -in private.pem -pubout -out public.pem

使用 openssl 基于 RSA 算法生成公私钥(3)    
• 查看 ASN.1 格式的私钥    
• openssl asn1parse -i -in private.pem    

使用 openssl 基于 RSA 算法生成公私钥(4)
• 查看 ASN.1 格式的公钥
• openssl asn1parse -i -in public.pem (X.590)
• openssl asn1parse -i -in public.pem -strparse 19

使用 RSA 公私钥加解密
• 加密文件
• openssl rsautl -encrypt -in hello.txt -inkey public.pem -pubin -out hello.en
• 解密文件
• openssl rsautl -decrypt -in hello.en -inkey private.pem -out hello.de


# 非对称密码应用:PKI 证书体系

非对称密码应用:数字签名   
 
基于私钥加密，只能使用公钥解密:起到身份认证的使用    
公钥的管理:Public Key Infrastructure(PKI)公钥基础设施
• 由 Certificate Authority(CA)数字证书认证机构将用户个人身份与公开密钥关联在一起
• 公钥数字证书组成
    CA信息、公钥用户信息、公钥、权威机构的签字、有效期
• PKI用户
    • 向 CA 注册公钥的用户
    • 希望使用已注册公钥的用户
    
## 签发证书流程

## 签名与验签流程   

## 证书信任链

## PKI 公钥基础设施

## 证书类型

## 验证证书链


# 非对称密码应用:DH 密钥交换协议

RSA 密钥交换
• 由客户端生成对称加密的密钥
问题:没有前向保密性

## DH 密钥交换    
• 1976 年由 Bailey Whitfield Diffie 和 Martin Edward Hellman 首次发表，故称为 Diffie–Hellman key exchange，简称 DH
• 它可以让双方在完全没有对方任何预先信息的条件下通过不安全信道创建起一个密钥

## DH 密钥交换协议举例(1)    

• g、p、A、B 公开 • a,b 保密
• 生成共同密钥 K

DH 密钥交换协议举例(2)    

• 协定使用 p=23 以及 base g=5.
• 爱丽丝选择一个秘密整数 a=6, 计算A = ga mod p 并发送给鲍伯。
• A=56 mod23=8.
• 鲍伯选择一个秘密整数 b=15, 计算B = gb mod p 并发送给爱丽丝。
• B=515 mod23=19.
• 爱丽丝计算s=Ba modp
• 196 mod23=2.
• 鲍伯计算s=Ab modp • 815 mod23=2.

## DH 密钥交换协议的问题    

中间人伪造攻击    
• 向 Alice 假装自己是 Bob，进行一次 DH 密钥交换 
• 向 Bob 假装自己是 Alice，进行一次 DH 密钥交换

解决中间人伪造攻击 
• 身份验证！！！！！！

# ECC 椭圆曲线的原理

## ECC椭圆曲线的定义    

• 椭圆曲线的表达式:
• 例如:
• 始终关于 X 轴对称(y 平方的存在)

## ECC 曲线的特性:+运算    

• P+Q=R
• +运算的几何意义:R 为 P、Q 连续与曲线交点在 X 轴上的镜像 • P+P=R
• +运算满足交换律 a+b = b+a
• +运算满足结合律 (a+b)+c = a+(b+c)

+运算的代数计算方法
• 先计算出斜率 m，再计算出 R 点的坐标

ECC+运算举例
• 设曲线:y2=x3−7x+10
• 设 P=(1,2)，Q=(3,4)，计算出 R(-3,-2)
• P 在曲线上，因为 22=4=13-7*1+10
• Q 在曲线上，因为 42=16=33-3*7+10=27-21+10
• R 在曲线上，因为 -22=4=-33-7*(-3)+10=-27+21+10

ECC 的关键原理
• Q=K.P
• 已知 K 与 P，正向运算快速
• 已知 Q 与 P，计算 K 的逆向运算非常困难

# DH 协议升级:基于椭圆曲线的 ECDH 协议

ECDH 密钥交换协议
• DH 密钥交换协议使用椭圆曲线后的变种，称为 Elliptic Curve Diffie–Hellman key Exchange，缩写为 ECDH，优点是比 DH 计算速度快、同等安全条件下密钥更短
• ECC(Elliptic Curve Cryptography):椭圆曲线密码学
• 魏尔斯特拉斯椭圆函数(Weierstrass‘s elliptic functions):y2=x3+ax+b

ECC 的关键原理
• Q=K.P
• 已知 K 与 P，正向运算快速
• 已知 Q 与 P，计算 K 的逆向运算非常困难

ECDH 的步骤    

• 步骤    
1. Alice 选定大整数 Ka 作为私钥    
2. 基于选定曲线及曲线上的共享 P 点，Alice 计算出 Qa=Ka.P
3. Alice 将 Qa、选定曲线、共享 P 点传递点 Bob
4. Bob选定大整数Kb作为私钥，将计算了Qb=Kb.P，并将Qb传递给Alice
5. Alice 生成密钥 Qb.Ka = (X, Y)，其中 X 为对称加密的密钥
6. Bob 生成密钥 Qa.Kb = (X, Y)，其中 X 为对称加密的密钥
• Qb.Ka = Ka.(Kb.P) = Ka.Kb.P = Kb.(Ka.P) = Qa.Kb


X25519 曲线
• 椭圆曲线变种:Montgomery curve 蒙哥马利曲线 • By2 =x3 +Ax2 +x
• 如右图:A=7，B=3
• X25519:y2 = x3 + 486662x2 + x
• p 等于 2255 – 19，基点 G=9
• order N
• 2252 + 0x14def9dea2f79cd65812631a5cf5d3ed


# TLS1.2 与 TLS1.3 中的 ECDH 协议

TLS1.2 通讯过程
    验证身份
    达成安全套件共识
    传递密钥 
    加密通讯
    
## FREAK 攻击    

• 2015 年发现漏洞
• 90 年代引入
• 512 位以下 RSA 密钥可轻易破解

## openssl 1.1.1 版本对 TLS1.3 的支持情况    

• Ciphersuites 安全套件
• TLS13-AES-256-GCM-SHA384
• TLS13-CHACHA20-POLY1305-SHA256 • TLS13-AES-128-GCM-SHA256
• TLS13-AES-128-CCM-8-SHA256
• TLS13-AES-128-CCM-SHA256

## 测试 TLS 站点支持情况    
• https://www.ssllabs.com/ssltest/index.html


## TLS1.3 中的密钥交换

# 握手的优化:session 缓存、ticket 票据及 TLS1.3 的0-RTT

session 缓存:以服务器生成的 session ID 为依据

session ticket

TLS1.3 的 0RTT 握手

0-RTT 面临的重放攻击


# TLS 与量子通讯的原理

TLS 密码学回顾
• 通讯双方在身份验证的基础上，协商出一次性的、随机的密钥 • PKI 公钥基础设施
• TLS 中间件生成一次性的、随机的密钥参数
• DH 系列协议基于非对称加密技术协商出密钥
• 使用分组对称加密算法，基于有限长度的密钥将任意长度的明文加密传输 • 密钥位数
• 分组工作模式

克劳德·艾尔伍德·香农:信息论
• 证明 one-time-pad(OTP)的绝对安全性 • 密钥是随机生成的
• 密钥的长度大于等于明文长度
• 相同的密钥只能使用一次
• 如何传递密钥?

QKD 与光偏振原理
• 量子密钥分发 quantum key distribution，简称 QKD
• 量子力学:任何对量子系统的测量都会对系统产生干扰
• QKD:如果有第三方试图窃听密码，则通信的双方便会察觉

# 量子通讯BB84协议的执行流程

BB84 协议
• 由 Charles Bennett 与 Gilles Brassard 在 1984 年发表

BB84 协议示意图
• 50%*50% = 25%的错误率

QKD 密钥纠错与隐私增强





