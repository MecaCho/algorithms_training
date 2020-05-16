
# 1132. 报告的记录 II

```
1132. 报告的记录 II
SQL架构
动作表： Actions

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| user_id       | int     |
| post_id       | int     |
| action_date   | date    |
| action        | enum    |
| extra         | varchar |
+---------------+---------+
这张表没有主键，并有可能存在重复的行。
action 列的类型是 ENUM，可能的值为 ('view', 'like', 'reaction', 'comment', 'report', 'share')。
extra 列拥有一些可选信息，例如：报告理由（a reason for report）或反应类型（a type of reaction）等。
移除表： Removals

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| post_id       | int     |
| remove_date   | date    | 
+---------------+---------+
这张表的主键是 post_id。
这张表的每一行表示一个被移除的帖子，原因可能是由于被举报或被管理员审查。
 

编写一段 SQL 来查找：在被报告为垃圾广告的帖子中，被移除的帖子的每日平均占比，四舍五入到小数点后 2 位。

查询结果的格式如下：

Actions table:
+---------+---------+-------------+--------+--------+
| user_id | post_id | action_date | action | extra  |
+---------+---------+-------------+--------+--------+
| 1       | 1       | 2019-07-01  | view   | null   |
| 1       | 1       | 2019-07-01  | like   | null   |
| 1       | 1       | 2019-07-01  | share  | null   |
| 2       | 2       | 2019-07-04  | view   | null   |
| 2       | 2       | 2019-07-04  | report | spam   |
| 3       | 4       | 2019-07-04  | view   | null   |
| 3       | 4       | 2019-07-04  | report | spam   |
| 4       | 3       | 2019-07-02  | view   | null   |
| 4       | 3       | 2019-07-02  | report | spam   |
| 5       | 2       | 2019-07-03  | view   | null   |
| 5       | 2       | 2019-07-03  | report | racism |
| 5       | 5       | 2019-07-03  | view   | null   |
| 5       | 5       | 2019-07-03  | report | racism |
+---------+---------+-------------+--------+--------+

Removals table:
+---------+-------------+
| post_id | remove_date |
+---------+-------------+
| 2       | 2019-07-20  |
| 3       | 2019-07-18  |
+---------+-------------+

Result table:
+-----------------------+
| average_daily_percent |
+-----------------------+
| 75.00                 |
+-----------------------+
2019-07-04 的垃圾广告移除率是 50%，因为有两张帖子被报告为垃圾广告，但只有一个得到移除。
2019-07-02 的垃圾广告移除率是 100%，因为有一张帖子被举报为垃圾广告并得到移除。
其余几天没有收到垃圾广告的举报，因此平均值为：(50 + 100) / 2 = 75%
注意，输出仅需要一个平均值即可，我们并不关注移除操作的日期。

1132. Reported Posts II
SQL架构
Table: Actions

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| user_id       | int     |
| post_id       | int     |
| action_date   | date    |
| action        | enum    |
| extra         | varchar |
+---------------+---------+
There is no primary key for this table, it may have duplicate rows.
The action column is an ENUM type of ('view', 'like', 'reaction', 'comment', 'report', 'share').
The extra column has optional information about the action such as a reason for report or a type of reaction. 
Table: Removals

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| post_id       | int     |
| remove_date   | date    | 
+---------------+---------+
post_id is the primary key of this table.
Each row in this table indicates that some post was removed as a result of being reported or as a result of an admin review.
 

Write an SQL query to find the average for daily percentage of posts that got removed after being reported as spam, rounded to 2 decimal places.

The query result format is in the following example:

Actions table:
+---------+---------+-------------+--------+--------+
| user_id | post_id | action_date | action | extra  |
+---------+---------+-------------+--------+--------+
| 1       | 1       | 2019-07-01  | view   | null   |
| 1       | 1       | 2019-07-01  | like   | null   |
| 1       | 1       | 2019-07-01  | share  | null   |
| 2       | 2       | 2019-07-04  | view   | null   |
| 2       | 2       | 2019-07-04  | report | spam   |
| 3       | 4       | 2019-07-04  | view   | null   |
| 3       | 4       | 2019-07-04  | report | spam   |
| 4       | 3       | 2019-07-02  | view   | null   |
| 4       | 3       | 2019-07-02  | report | spam   |
| 5       | 2       | 2019-07-03  | view   | null   |
| 5       | 2       | 2019-07-03  | report | racism |
| 5       | 5       | 2019-07-03  | view   | null   |
| 5       | 5       | 2019-07-03  | report | racism |
+---------+---------+-------------+--------+--------+

Removals table:
+---------+-------------+
| post_id | remove_date |
+---------+-------------+
| 2       | 2019-07-20  |
| 3       | 2019-07-18  |
+---------+-------------+

Result table:
+-----------------------+
| average_daily_percent |
+-----------------------+
| 75.00                 |
+-----------------------+
The percentage for 2019-07-04 is 50% because only one post of two spam reported posts was removed.
The percentage for 2019-07-02 is 100% because one post was reported as spam and it was removed.
The other days had no spam reports so the average is (50 + 100) / 2 = 75%
Note that the output is only one number and that we do not care about the remove dates.

```

# Write your MySQL query statement below


```
-- select count(post_id), action_date from Actions where action='report' group by action_date;

-- SELECT ROUND(AVG(proportion) * 100, 2) AS average_daily_percent  
-- FROM (
--     SELECT actions.action_date, COUNT(DISTINCT removals.post_id)/COUNT(DISTINCT actions.post_id) AS proportion
--     FROM actions
--     LEFT JOIN removals
--     ON actions.post_id = removals.post_id
--     WHERE extra = 'spam' 
--     GROUP BY actions.action_date
-- ) a

select round(avg(proportion)*100, 2) as average_daily_percent from (select a.action_date, count(distinct r.post_id) / count(distinct a.post_id) as proportion from Actions a left join Removals r on a.post_id=r.post_id where extra='spam' group by a.action_date) a;

```

# tips

```
预备知识
本题使用到的 mysql 函数的说明：

ROUND(x, d)： 四舍五入保留 x 的 d 位小数。
AVG()： 计算平均值 。
IFNULL(x1, x2) ：如果 x1 为 NULL， 返回 x2。
方法一：LEFT JOIN 、 GROUP BY 和 FROM 子查询
思路
主要思想：先计算出每一天被移除的帖子的占比，最后求平均值。

既然要求占比，肯定要求出分子和分母。根据题意可以知道 removals 表中的数据是分子，actions 表中的数据是分母。两个表根据 post_id 可以对应起来。所以可以使用 LEFT JOIN 将两个表结合起来。因为题目要的是每天的数据，所以还需要使用 GROUP BY 将相同日期的数据聚合。最后统计分子和分母的值相除得出结果。

这里还有两个需要注意的点：

因为表中可能存在重复的行，所以有可能同一天有相同的 post_id，但是只需要统计一次，所以要用 DISTINCT 去重。

因为 actions 表是真正需要查询的数据，所以需要使用左连接。

Mysql
SELECT actions.action_date, COUNT(DISTINCT removals.post_id)/COUNT(DISTINCT actions.post_id) AS proportion
FROM actions
LEFT JOIN removals
ON actions.post_id = removals.post_id
WHERE extra = 'spam' 
GROUP BY actions.action_date
拿到每一天的占比后，只需要用 FROM 子查询，将所有的结果求平均值并且四舍五入保留两位有效数字即可。

代码
mysql
SELECT ROUND(AVG(proportion) * 100, 2) AS average_daily_percent  
FROM (
    SELECT actions.action_date, COUNT(DISTINCT removals.post_id)/COUNT(DISTINCT actions.post_id) AS proportion
    FROM actions
    LEFT JOIN removals
    ON actions.post_id = removals.post_id
    WHERE extra = 'spam' 
    GROUP BY actions.action_date
) a
方法二：LEFT JOIN 和 GROUP BY
思路
主要思想：方法一是直接求出占比的集合，此方法是先求出分子和分母各自的集合，再进行计算并求平均值。
先求出分子的集合：

mysql
SELECT action_date, COUNT(DISTINCT post_id) AS cnt
FROM actions
WHERE extra = 'spam' AND post_id IN (SELECT post_id FROM Removals)
GROUP BY action_date
再求出分母的集合：

mysql
SELECT action_date, COUNT(DISTINCT post_id) AS cnt
FROM actions
WHERE extra = 'spam'
GROUP BY action_date
使用 LEFT JOIN 将两个结果根据日期结合计算平均值。

代码
mysql
SELECT ROUND(AVG(IFNULL(remove.cnt, 0)/total.cnt) * 100, 2) AS average_daily_percent
FROM (
    SELECT action_date, COUNT(DISTINCT post_id) AS cnt
    FROM actions
    WHERE extra = 'spam'
    GROUP BY action_date
) total
LEFT JOIN (
    SELECT action_date, COUNT(DISTINCT post_id) AS cnt
    FROM actions
    WHERE extra = 'spam' AND post_id IN (SELECT post_id FROM Removals)
    GROUP BY action_date
) remove 
ON total.action_date = remove.action_date

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/reported-posts-ii/solution/bao-gao-de-ji-lu-ii-by-leetcode-solution/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
```