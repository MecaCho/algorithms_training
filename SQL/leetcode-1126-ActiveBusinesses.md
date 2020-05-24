



# 1126. Active Businesses


```

1126. 查询活跃业务
SQL架构
事件表：Events

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| business_id   | int     |
| event_type    | varchar |
| occurences    | int     | 
+---------------+---------+
此表的主键是 (business_id, event_type)。
表中的每一行记录了某种类型的事件在某些业务中多次发生的信息。
 

写一段 SQL 来查询所有活跃的业务。

如果一个业务的某个事件类型的发生次数大于此事件类型在所有业务中的平均发生次数，并且该业务至少有两个这样的事件类型，那么该业务就可被看做是活跃业务。

查询结果格式如下所示：

Events table:
+-------------+------------+------------+
| business_id | event_type | occurences |
+-------------+------------+------------+
| 1           | reviews    | 7          |
| 3           | reviews    | 3          |
| 1           | ads        | 11         |
| 2           | ads        | 7          |
| 3           | ads        | 6          |
| 1           | page views | 3          |
| 2           | page views | 12         |
+-------------+------------+------------+

结果表
+-------------+
| business_id |
+-------------+
| 1           |
+-------------+ 
'reviews'、 'ads' 和 'page views' 的总平均发生次数分别是 (7+3)/2=5, (11+7+6)/3=8, (3+12)/2=7.5。
id 为 1 的业务有 7 个 'reviews' 事件（大于 5）和 11 个 'ads' 事件（大于 8），所以它是活跃业务。

1126. Active Businesses
SQL架构
Table: Events

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| business_id   | int     |
| event_type    | varchar |
| occurences    | int     | 
+---------------+---------+
(business_id, event_type) is the primary key of this table.
Each row in the table logs the info that an event of some type occured at some business for a number of times.
 

Write an SQL query to find all active businesses.

An active business is a business that has more than one event type with occurences greater than the average occurences of that event type among all businesses.

The query result format is in the following example:

Events table:
+-------------+------------+------------+
| business_id | event_type | occurences |
+-------------+------------+------------+
| 1           | reviews    | 7          |
| 3           | reviews    | 3          |
| 1           | ads        | 11         |
| 2           | ads        | 7          |
| 3           | ads        | 6          |
| 1           | page views | 3          |
| 2           | page views | 12         |
+-------------+------------+------------+

Result table:
+-------------+
| business_id |
+-------------+
| 1           |
+-------------+ 
Average for 'reviews', 'ads' and 'page views' are (7+3)/2=5, (11+7+6)/3=8, (3+12)/2=7.5 respectively.
Business with id 1 has 7 'reviews' events (more than 5) and 11 'ads' events (more than 8) so it is an active business.

```

# Write your MySQL query statement below

```
# Write your MySQL query statement below


SELECT business_id
FROM Events AS e
JOIN (
    SELECT event_type, AVG(occurences) AS eventAvg
    FROM Events
    GROUP BY event_type
) AS e1 
ON e.event_type = e1.event_type
WHERE e.occurences > e1.eventAvg
GROUP BY business_id
HAVING COUNT(*) >= 2;

```


# solutions

```
方法一：JOIN 和 GROUP BY
思路
首先根据题目，必须要知道所有业务中的平均发生次数。所以需要计算每个业务的平均值，可以使用 AVG 函数和 GROUP BY 计算每个 event_type 的平均值。

Mysql
SELECT event_type, AVG(occurences) AS eventAvg
FROM Events
GROUP BY event_type
拿到平均值后使用 JOIN 将新的数据和老数据根据 event_type 联合在一起。判断老数据的 occurences 是否大于平均值。

Mysql
SELECT business_id
FROM Events AS e
JOIN (
    SELECT event_type, AVG(occurences) AS eventAvg
    FROM Events
    GROUP BY event_type
) AS e1 
ON e.event_type = e1.event_type
WHERE e.occurences > e1.eventAvg
题目最后还要求至少有两个这样的事件类型，所以需要再用一次 GROUP BY 将每一个业务聚合并判断事件类型的数量。

代码
Mysql
SELECT business_id
FROM Events AS e
JOIN (
    SELECT event_type, AVG(occurences) AS eventAvg
    FROM Events
    GROUP BY event_type
) AS e1 
ON e.event_type = e1.event_type
WHERE e.occurences > e1.eventAvg
GROUP BY business_id
HAVING COUNT(*) >= 2

```