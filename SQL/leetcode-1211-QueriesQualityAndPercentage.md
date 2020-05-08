

# 1211. Queries Quality and Percentage

```
1211. 查询结果的质量和占比
SQL架构
查询表 Queries： 

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| query_name  | varchar |
| result      | varchar |
| position    | int     |
| rating      | int     |
+-------------+---------+
此表没有主键，并可能有重复的行。
此表包含了一些从数据库中收集的查询信息。
“位置”（position）列的值为 1 到 500 。
“评分”（rating）列的值为 1 到 5 。评分小于 3 的查询被定义为质量很差的查询。
 

将查询结果的质量 quality 定义为：

各查询结果的评分与其位置之间比率的平均值。

将劣质查询百分比 poor_query_percentage 为：

评分小于 3 的查询结果占全部查询结果的百分比。

编写一组 SQL 来查找每次查询的名称(query_name)、质量(quality) 和 劣质查询百分比(poor_query_percentage)。

质量(quality) 和劣质查询百分比(poor_query_percentage) 都应四舍五入到小数点后两位。

查询结果格式如下所示：

Queries table:
+------------+-------------------+----------+--------+
| query_name | result            | position | rating |
+------------+-------------------+----------+--------+
| Dog        | Golden Retriever  | 1        | 5      |
| Dog        | German Shepherd   | 2        | 5      |
| Dog        | Mule              | 200      | 1      |
| Cat        | Shirazi           | 5        | 2      |
| Cat        | Siamese           | 3        | 3      |
| Cat        | Sphynx            | 7        | 4      |
+------------+-------------------+----------+--------+

Result table:
+------------+---------+-----------------------+
| query_name | quality | poor_query_percentage |
+------------+---------+-----------------------+
| Dog        | 2.50    | 33.33                 |
| Cat        | 0.66    | 33.33                 |
+------------+---------+-----------------------+

Dog 查询结果的质量为 ((5 / 1) + (5 / 2) + (1 / 200)) / 3 = 2.50
Dog 查询结果的劣质查询百分比为 (1 / 3) * 100 = 33.33

Cat 查询结果的质量为 ((2 / 5) + (3 / 3) + (4 / 7)) / 3 = 0.66
Cat 查询结果的劣质查询百分比为 (1 / 3) * 100 = 33.33


1211. Queries Quality and Percentage
SQL架构
Table: Queries

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| query_name  | varchar |
| result      | varchar |
| position    | int     |
| rating      | int     |
+-------------+---------+
There is no primary key for this table, it may have duplicate rows.
This table contains information collected from some queries on a database.
The position column has a value from 1 to 500.
The rating column has a value from 1 to 5. Query with rating less than 3 is a poor query.
 

We define query quality as:

The average of the ratio between query rating and its position.

We also define poor query percentage as:

The percentage of all queries with rating less than 3.

Write an SQL query to find each query_name, the quality and poor_query_percentage.

Both quality and poor_query_percentage should be rounded to 2 decimal places.

The query result format is in the following example:

Queries table:
+------------+-------------------+----------+--------+
| query_name | result            | position | rating |
+------------+-------------------+----------+--------+
| Dog        | Golden Retriever  | 1        | 5      |
| Dog        | German Shepherd   | 2        | 5      |
| Dog        | Mule              | 200      | 1      |
| Cat        | Shirazi           | 5        | 2      |
| Cat        | Siamese           | 3        | 3      |
| Cat        | Sphynx            | 7        | 4      |
+------------+-------------------+----------+--------+

Result table:
+------------+---------+-----------------------+
| query_name | quality | poor_query_percentage |
+------------+---------+-----------------------+
| Dog        | 2.50    | 33.33                 |
| Cat        | 0.66    | 33.33                 |
+------------+---------+-----------------------+

Dog queries quality is ((5 / 1) + (5 / 2) + (1 / 200)) / 3 = 2.50
Dog queries poor_ query_percentage is (1 / 3) * 100 = 33.33

Cat queries quality equals ((2 / 5) + (3 / 3) + (4 / 7)) / 3 = 0.66
Cat queries poor_ query_percentage is (1 / 3) * 100 = 33.33
```

# Write your MySQL query statement below

```

select query_name, ROUND(AVG(rating/position), 2) quality, ROUND(SUM(IF(rating < 3, 1, 0)) / COUNT(*) * 100, 2) poor_query_percentage from Queries group by query_name;

```

# solution 

```
方法一：GROUP BY
思路

本题主要考察在 MySQL 内做简单的计算操作，比如求平均值，求和等。在解题前先回顾一下相关的函数。

SUM()：返回某列的和。
AVG()：返回某列的平均值。
COUNT() ：返回某列的行数。
MAX() ：返回某列的最大值。
MIN() ：返回某列的最小值。

根据题意我们需要计算的是每个名称的数据，可以使用 GROUP BY 对名称（query_name）进行聚合，然后再处理数据。

计算质量 quality：
各查询结果的评分与其位置之间比率的平均值。

评分与其位置之前的比率为 rating/position， 平均值为：

AVG(rating/position)
计算劣质查询百分比 poor_query_percentage：
评分小于 3 的查询结果占全部查询结果的百分比。

评分小于 3 的数量可以使用 SUM 和 IF，如果 rating 小于 3，那么数量加 1。全部查询结果可以直接使用 COUNT()。因为要求的是百分比，所以分子需要乘 100。

SUM(IF(rating < 3, 1, 0)) * 100 / COUNT(*)
最后不要忘记使用 ROUND() 函数将结果四舍五入到小数点后两位。

代码

Mysql
SELECT 
    query_name, 
    ROUND(AVG(rating/position), 2) quality,
    ROUND(SUM(IF(rating < 3, 1, 0)) * 100 / COUNT(*), 2) poor_query_percentage
FROM Queries
GROUP BY query_name

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/queries-quality-and-percentage/solution/cha-xun-jie-guo-de-zhi-liang-he-zhan-bi-by-leetcod/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
```