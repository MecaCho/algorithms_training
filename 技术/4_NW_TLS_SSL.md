
# TLS/SSL 协议的工作原理

TLS 设计目的    

• 身份验证 
• 保密性
• 完整性

## TLS/SSL 发展

## TLS 协议    

Record 记录协议     
• 对称加密    

Handshake 握手协议    

• 验证通讯双方的身份
• 交换加解密的安全套件 
• 协商加密参数

## TLS 安全密码套件解读

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
• 为比利时密码学家 Joan Daemen 和 Vincent Rijmen 所设计，又称 Rijndael 加密算法 • 常用填充算法:PKCS7
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
• 每个参与方都有一对密钥 • 公钥
• 向对方公开 • 私钥
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
    CA 信息、公钥用户信息、公钥、权威机构的签字、有效期
• PKI用户
    • 向 CA 注册公钥的用户
    • 希望使用已注册公钥的用户



