
# SQL 分类：

SQL 语句主要可以划分为以下 3 个类别。

- DDL（Data Definition Languages）语句：      
数据定义语言，这些语句定义了不同的数据段、数据库、表、列、索引等数据库对象的定义。
常用的语句关键字主要包括 create、drop、alter等。

- DML（Data Manipulation Language）语句：
数据操纵语句，用于添加、删除、更新和查询数据库记录，并检查数据完整性，
常用的语句关键字主要包括 insert、delete、udpate 和select 等。(增添改查）

- DCL（Data Control Language）语句：    
数据控制语句，用于控制不同数据段直接的许可和访问级别的语句。
这些语句定义了数据库、表、字段、用户的访问权限和安全级别。主要的语句关键字包括 grant、revoke 等。


# drop、delete与truncate

drop table

1)属于DDL
2)不可回滚
3)不可带where
4)表内容和结构删除
5)删除速度快

truncate table

1)属于DDL
2)不可回滚
3)不可带where
4)表内容删除
5)删除速度快

delete from

1)属于DML
2)可回滚
3)可带where
4)表结构在，表内容要看where执行的情况
5)删除速度慢,需要逐行删除


# 超键、候选键、主键、外键分别是什么？


- 超键：    
在关系中能唯一标识元组的属性集称为关系模式的超键。一个属性可以为作为一个超键，多个属性组合在一起也可以作为一个超键。超键包含候选键和主键。
- 候选键(候选码)：     
是最小超键，即没有冗余元素的超键。
- 主键(主码)：     
数据库表中对储存数据对象予以唯一和完整标识的数据列或属性的组合。一个数据列只能有一个主键，且主键的取值不能缺失，即不能为空值（Null）。
- 外键：      
在一个表中存在的另一个表的主键称此表的外键。

# SQL 约束有哪几种？

NOT NULL: 用于控制字段的内容一定不能为空（NULL）。     
UNIQUE: 控件字段内容不能重复，一个表允许有多个 Unique 约束。    
PRIMARY KEY: 也是用于控件字段内容不能重复，但它在一个表只允许出现一个。    
FOREIGN KEY: 用于预防破坏表之间连接的动作，也能防止非法数据插入外键列，因为它必须是它指向的那个表中的值之一。
CHECK: 用于控制字段的值范围。

# 数据库运行于哪种状态下可以防止数据的丢失？

在archivelog mode(归档模式)只要其归档日志文件不丢失，就可以有效地防止数据丢失。


# mysql有关权限的表都有哪几个

MySQL服务器通过权限表来控制用户对数据库的访问，权限表存放在mysql数据库里，由mysql_install_db脚本初始化。
这些权限表分别user，db，table_priv，columns_priv和host。下面分别介绍一下这些表的结构和内容：

user权限表：记录允许连接到服务器的用户帐号信息，里面的权限是全局级的。    
db权限表：记录各个帐号在各个数据库上的操作权限。    
table_priv权限表：记录数据表级的操作权限。    
columns_priv权限表：记录数据列级的操作权限。    
host权限表：配合db权限表对给定主机上数据库级操作权限作更细致的控制。这个权限表不受GRANT和REVOKE语句的影响。


# union和unionall的区别是什么？    

union就是将两个SELECT语句查询的结果集合并(两个SELECT可以是同一个表，也可以是不同表)，如果需要排序，在第二个SELECT语句后加ORDER BY语句，会对所有结果进行排序。

union默认是会去除重复的数据的，会对结果集做去重处理，union all不会做去重处理。

所以union效率慢一些，如果能确定结果不会重复或者需要不去重的结果，那么应该使用union all，效率会高一些。


# Join的工作流程是怎么样的，怎么进行优化？    

join的大概使用是怎么样的？
full outer join 会包含两个表不满足条件的行

left outer join 会包含左边的表不满足条件的行

right outer join 会包含右边的表不满足条件的行

inner join 就是只包含满足条件的行

cross join 从表A循环取出每一条记录去表B匹配，cross join 后面不能跟on，只能跟where




```
insert into application (id, name, project_id, env_type,env_id, created_at, upgrade_his) select 40000165, t2.name, t2.project_id, "PERF",30000091, t2.created_at, "" from application t2 where id=40000138;

```

bin_log    

```
show variables like '%log_bin%';
show binary logs;
show master status;

mysqlbinlog: /usr/bin/mysqlbinlog mysql-bin.000007
```