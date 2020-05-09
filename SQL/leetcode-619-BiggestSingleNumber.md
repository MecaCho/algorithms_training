

# 619. Biggest Single Number

```
619. 只出现一次的最大数字
SQL架构
表 my_numbers 的 num 字段包含很多数字，其中包括很多重复的数字。

你能写一个 SQL 查询语句，找到只出现过一次的数字中，最大的一个数字吗？

+---+
|num|
+---+
| 8 |
| 8 |
| 3 |
| 3 |
| 1 |
| 4 |
| 5 |
| 6 | 
对于上面给出的样例数据，你的查询语句应该返回如下结果：

+---+
|num|
+---+
| 6 |
注意：

如果没有只出现一次的数字，输出 null 。

619. Biggest Single Number
SQL架构
Table my_numbers contains many numbers in column num including duplicated ones.
Can you write a SQL query to find the biggest number, which only appears once.

+---+
|num|
+---+
| 8 |
| 8 |
| 3 |
| 3 |
| 1 |
| 4 |
| 5 |
| 6 | 
For the sample data above, your query should return the following result:
+---+
|num|
+---+
| 6 |
Note:
If there is no such number, just output null.
```


# Write your MySQL query statement below

```
select max(num) as num from
(select num as num from my_numbers group by num having count(num)=1) as t;

```

# tips

```
方法：使用子查询 和 MAX() 函数【通过】
算法

使用子查询找出仅出现一次的数字。

MySQL
SELECT
    num
FROM
    `number`
GROUP BY num
HAVING COUNT(num) = 1;
然后使用 MAX() 函数找出其中最大的一个。

MySQL
SELECT
    MAX(num) AS num
FROM
    (SELECT
        num
    FROM
        number
    GROUP BY num
    HAVING COUNT(num) = 1) AS t
;

```