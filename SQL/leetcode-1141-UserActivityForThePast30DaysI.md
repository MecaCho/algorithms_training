
# 1141. User Activity for the Past 30 Days I

```
1141. 查询近30天活跃用户数
SQL架构
活动记录表：Activity

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| user_id       | int     |
| session_id    | int     |
| activity_date | date    |
| activity_type | enum    |
+---------------+---------+
该表是用户在社交网站的活动记录。
该表没有主键，可能包含重复数据。
activity_type 字段为以下四种值 ('open_session', 'end_session', 'scroll_down', 'send_message')。
每个 session_id 只属于一个用户。
 

请写SQL查询出截至 2019-07-27（包含2019-07-27），近 30天的每日活跃用户数（当天只要有一条活动记录，即为活跃用户）。

查询结果示例如下：

Activity table:
+---------+------------+---------------+---------------+
| user_id | session_id | activity_date | activity_type |
+---------+------------+---------------+---------------+
| 1       | 1          | 2019-07-20    | open_session  |
| 1       | 1          | 2019-07-20    | scroll_down   |
| 1       | 1          | 2019-07-20    | end_session   |
| 2       | 4          | 2019-07-20    | open_session  |
| 2       | 4          | 2019-07-21    | send_message  |
| 2       | 4          | 2019-07-21    | end_session   |
| 3       | 2          | 2019-07-21    | open_session  |
| 3       | 2          | 2019-07-21    | send_message  |
| 3       | 2          | 2019-07-21    | end_session   |
| 4       | 3          | 2019-06-25    | open_session  |
| 4       | 3          | 2019-06-25    | end_session   |
+---------+------------+---------------+---------------+

Result table:
+------------+--------------+ 
| day        | active_users |
+------------+--------------+ 
| 2019-07-20 | 2            |
| 2019-07-21 | 2            |
+------------+--------------+ 
非活跃用户的记录不需要展示。

1141. User Activity for the Past 30 Days I
SQL架构
Table: Activity

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| user_id       | int     |
| session_id    | int     |
| activity_date | date    |
| activity_type | enum    |
+---------------+---------+
There is no primary key for this table, it may have duplicate rows.
The activity_type column is an ENUM of type ('open_session', 'end_session', 'scroll_down', 'send_message').
The table shows the user activities for a social media website. 
Note that each session belongs to exactly one user.
 

Write an SQL query to find the daily active user count for a period of 30 days ending 2019-07-27 inclusively. A user was active on some day if he/she made at least one activity on that day.

The query result format is in the following example:

Activity table:
+---------+------------+---------------+---------------+
| user_id | session_id | activity_date | activity_type |
+---------+------------+---------------+---------------+
| 1       | 1          | 2019-07-20    | open_session  |
| 1       | 1          | 2019-07-20    | scroll_down   |
| 1       | 1          | 2019-07-20    | end_session   |
| 2       | 4          | 2019-07-20    | open_session  |
| 2       | 4          | 2019-07-21    | send_message  |
| 2       | 4          | 2019-07-21    | end_session   |
| 3       | 2          | 2019-07-21    | open_session  |
| 3       | 2          | 2019-07-21    | send_message  |
| 3       | 2          | 2019-07-21    | end_session   |
| 4       | 3          | 2019-06-25    | open_session  |
| 4       | 3          | 2019-06-25    | end_session   |
+---------+------------+---------------+---------------+

Result table:
+------------+--------------+ 
| day        | active_users |
+------------+--------------+ 
| 2019-07-20 | 2            |
| 2019-07-21 | 2            |
+------------+--------------+ 
Note that we do not care about days with zero active users.
```


# Write your MySQL query statement below

```

select activity_date as day, count(distinct user_id) as active_users from Activity where activity_date between '2019-06-28' and '2019-07-27' group by activity_date;
```

# tips

```
方法一：GROUP BY 和 DISTINCT
思路

使用 COUNT 函数计算用户的数量。因为该表没有主键，可能包含重复数据，所以需要在此基础上使用 DISTINCT 去重：COUNT(DISTINCT user_id）。
统计截至 2019-07-27，近 30 天的每日活跃用户，所以需要使用 WHERE 过滤数据，可以使用两种办法（注意是截至不是截止）：
计算出第一天，使用 BETWEEN ：WHERE activity_date BETWEEN '2019-06-28' AND '2019-07-27'。
使用 datediff() 函数，计算当天与最后一天的差值：WHERE datediff('2019-07-27',activity_date) < 30。
使用 GROUP BY 按天聚合。
代码

Mysql
SELECT activity_date AS day, COUNT(DISTINCT user_id) AS active_users
FROM Activity
WHERE datediff('2019-07-27',activity_date) < 30
-- WHERE activity_date BETWEEN '2019-06-28' AND '2019-07-27'
GROUP BY activity_date

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/user-activity-for-the-past-30-days-i/solution/cha-xun-jin-30tian-huo-yue-yong-hu-shu-by-leetcode/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
```