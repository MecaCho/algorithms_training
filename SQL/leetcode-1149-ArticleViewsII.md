
# 1149. Article Views II

```

题目描述
评论 (23)
题解(12)
提交记录
1149. 文章浏览 II
SQL架构
Table: Views

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| article_id    | int     |
| author_id     | int     |
| viewer_id     | int     |
| view_date     | date    |
+---------------+---------+
此表无主键，因此可能会存在重复行。此表的每一行都表示某人在某天浏览了某位作者的某篇文章。 请注意，同一人的 author_id 和 viewer_id 是相同的。
 

编写一条 SQL 查询来找出在同一天阅读至少两篇文章的人，结果按照 id 升序排序。

查询结果的格式如下：

Views table:
+------------+-----------+-----------+------------+
| article_id | author_id | viewer_id | view_date  |
+------------+-----------+-----------+------------+
| 1          | 3         | 5         | 2019-08-01 |
| 3          | 4         | 5         | 2019-08-01 |
| 1          | 3         | 6         | 2019-08-02 |
| 2          | 7         | 7         | 2019-08-01 |
| 2          | 7         | 6         | 2019-08-02 |
| 4          | 7         | 1         | 2019-07-22 |
| 3          | 4         | 4         | 2019-07-21 |
| 3          | 4         | 4         | 2019-07-21 |
+------------+-----------+-----------+------------+

Result table:
+------+
| id   |
+------+
| 5    |
| 6    |
+------+


1149. Article Views II
SQL架构
Table: Views

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| article_id    | int     |
| author_id     | int     |
| viewer_id     | int     |
| view_date     | date    |
+---------------+---------+
There is no primary key for this table, it may have duplicate rows.
Each row of this table indicates that some viewer viewed an article (written by some author) on some date. 
Note that equal author_id and viewer_id indicate the same person.
 

Write an SQL query to find all the people who viewed more than one article on the same date, sorted in ascending order by their id.

The query result format is in the following example:

Views table:
+------------+-----------+-----------+------------+
| article_id | author_id | viewer_id | view_date  |
+------------+-----------+-----------+------------+
| 1          | 3         | 5         | 2019-08-01 |
| 3          | 4         | 5         | 2019-08-01 |
| 1          | 3         | 6         | 2019-08-02 |
| 2          | 7         | 7         | 2019-08-01 |
| 2          | 7         | 6         | 2019-08-02 |
| 4          | 7         | 1         | 2019-07-22 |
| 3          | 4         | 4         | 2019-07-21 |
| 3          | 4         | 4         | 2019-07-21 |
+------------+-----------+-----------+------------+

Result table:
+------+
| id   |
+------+
| 5    |
| 6    |
+------+

```

```
# Write your MySQL query statement below
select distinct viewer_id id from Views GROUP BY view_date, viewer_id HAVING COUNT(DISTINCT article_id) >= 2 order by viewer_id;
-- select viewer_id id from Views where count(distinct article_id) > 2;
```

```
方法一：GROUP BY 和 DISTINCT
算法

根据题目一步一步的拆分成子任务：

首先题目要求是同一天，所以需要根据时间聚合记录，使用 GROUP BY 聚合。
GROUP BY view_date
其次是至少阅读两篇文章的人。通过这句话我们可以知道还需要根据人来聚合，计算每个人阅读的文章数。在 GROUP BY 的基础上使用 HAVING 过滤条件。因为表中可能有重复的数据，所以还要对 article_id 做去重处理。
GROUP BY viewer_id
HAVING COUNT(DISTINCT article_id) >= 2
然后将结果按照 id 升序排序，这个只需要使用 ORDER BY 对结果进行排序。
最后将上面三步联合起来就是我们需要的数据。但是结果依然有可能重复，所以需要再对结果去重。
代码

Mysql
SELECT DISTINCT viewer_id AS id
FROM Views
GROUP BY view_date, viewer_id
HAVING COUNT(DISTINCT article_id) >= 2
ORDER BY viewer_id

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/article-views-ii/solution/wen-zhang-liu-lan-ii-by-leetcode-solution/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
```