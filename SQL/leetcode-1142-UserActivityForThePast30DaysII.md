
```
1142. 过去30天的用户活动 II
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
该表没有主键，它可能有重复的行。
activity_type列是一种类型的ENUM（“ open_session”，“ end_session”，“ scroll_down”，“ send_message”）。
该表显示了社交媒体网站的用户活动。
请注意，每个会话完全属于一个用户。
 

编写SQL查询以查找截至2019年7月27日（含）的30天内每个用户的平均会话数，四舍五入到小数点后两位。我们只统计那些会话期间用户至少进行一项活动的有效会话。

 

查询结果格式如下例所示：

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
| 3       | 5          | 2019-07-21    | open_session  |
| 3       | 5          | 2019-07-21    | scroll_down   |
| 3       | 5          | 2019-07-21    | end_session   |
| 4       | 3          | 2019-06-25    | open_session  |
| 4       | 3          | 2019-06-25    | end_session   |
+---------+------------+---------------+---------------+

Result table:
+---------------------------+ 
| average_sessions_per_user |
+---------------------------+ 
| 1.33                      |
+---------------------------+ 
User 1 和 2 在过去30天内各自进行了1次会话，而用户3进行了2次会话，因此平均值为（1 +1 + 2）/ 3 = 1.33。

1142. User Activity for the Past 30 Days II
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
 

Write an SQL query to find the average number of sessions per user for a period of 30 days ending 2019-07-27 inclusively, rounded to 2 decimal places. The sessions we want to count for a user are those with at least one activity in that time period.

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
| 3       | 5          | 2019-07-21    | open_session  |
| 3       | 5          | 2019-07-21    | scroll_down   |
| 3       | 5          | 2019-07-21    | end_session   |
| 4       | 3          | 2019-06-25    | open_session  |
| 4       | 3          | 2019-06-25    | end_session   |
+---------+------------+---------------+---------------+

Result table:
+---------------------------+ 
| average_sessions_per_user |
+---------------------------+ 
| 1.33                      |
+---------------------------+ 
User 1 and 2 each had 1 session in the past 30 days while user 3 had 2 sessions so the average is (1 + 1 + 2) / 3 = 1.33.
```


# Write your MySQL query statement below

```
select IFNULL(round(count(distinct session_id)/count(distinct user_id), 2), 0) as average_sessions_per_user   from Activity where activity_date between '2019-06-28' and '2019-07-27';

```

# tips

```
预备知识
本题使用到的 mysql 函数的说明：

ROUND(x, d)： 四舍五入保留 x 的 d 位小数。
IFNULL(x1, x2) ：如果 x1 为 NULL， 返回 x2。
方法一：COUNT 和 DATEDIFF
思路

本题的重点就是要理解每个用户的平均会话数。用户即为 user_id，无论什么时候永远不会变。会话是对应的 session_id，用户的 session_id 会在特定的情况下改变，比如 end_session 后再 open_session。所以我们只需要统计总的会话数和总的用户数，相除就是平均数，即：

COUNT(session_id) / COUNT(user_id)
这个数字还需要加工处理：

由于表里面可能有重复的数据，所以需要使用 DISTINCT 去重。
使用 ROUND() 保留两位有效数字。
使用 IFNULL 处理返回结果为 null 的情况。
只需要查找截至 2019-07-27 日（含）的 30 天内的数据，有两种办法（注意是截至不是截止）：
计算出第一天，使用 BETWEEN ：WHERE activity_date BETWEEN '2019-06-28' AND '2019-07-27'。
使用 datediff() 函数，计算当天与最后一天的差值：WHERE datediff('2019-07-27',activity_date) < 30。
代码

Mysql
SELECT IFNULL(ROUND(COUNT(DISTINCT session_id) / COUNT(DISTINCT user_id), 2), 0) AS average_sessions_per_user
FROM Activity
WHERE DATEDIFF('2019-07-27', activity_date) < 30
-- WHERE activity_date BETWEEN '2019-06-28' AND '2019-07-27'

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/user-activity-for-the-past-30-days-ii/solution/guo-qu-30tian-de-yong-hu-huo-dong-ii-by-leetcode-s/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

```