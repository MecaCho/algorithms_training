
# 1355. Activity Participants

```
1355. 活动参与者
SQL架构
表: Friends

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| name          | varchar |
| activity      | varchar |
+---------------+---------+
id 是朋友的 id 和该表的主键
name 是朋友的名字
activity 是朋友参加的活动的名字
表: Activities

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| name          | varchar |
+---------------+---------+
id 是该表的主键
name 是活动的名字
 

写一条 SQL 查询那些既没有最多，也没有最少参与者的活动的名字

可以以任何顺序返回结果，Activities 表的每项活动的参与者都来自 Friends 表

下面是查询结果格式的例子：

Friends 表:
+------+--------------+---------------+
| id   | name         | activity      |
+------+--------------+---------------+
| 1    | Jonathan D.  | Eating        |
| 2    | Jade W.      | Singing       |
| 3    | Victor J.    | Singing       |
| 4    | Elvis Q.     | Eating        |
| 5    | Daniel A.    | Eating        |
| 6    | Bob B.       | Horse Riding  |
+------+--------------+---------------+

Activities 表:
+------+--------------+
| id   | name         |
+------+--------------+
| 1    | Eating       |
| 2    | Singing      |
| 3    | Horse Riding |
+------+--------------+

Result 表:
+--------------+
| activity     |
+--------------+
| Singing      |
+--------------+

Eating 活动有三个人参加, 是最多人参加的活动 (Jonathan D. , Elvis Q. and Daniel A.)
Horse Riding 活动有一个人参加, 是最少人参加的活动 (Bob B.)
Singing 活动有两个人参加 (Victor J. and Jade W.)

1355. Activity Participants
SQL架构
Table: Friends

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| name          | varchar |
| activity      | varchar |
+---------------+---------+
id is the id of the friend and primary key for this table.
name is the name of the friend.
activity is the name of the activity which the friend takes part in.
Table: Activities

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| name          | varchar |
+---------------+---------+
id is the primary key for this table.
name is the name of the activity.
 

Write an SQL query to find the names of all the activities with neither maximum, nor minimum number of participants.

Return the result table in any order. Each activity in table Activities is performed by any person in the table Friends.

The query result format is in the following example:

Friends table:
+------+--------------+---------------+
| id   | name         | activity      |
+------+--------------+---------------+
| 1    | Jonathan D.  | Eating        |
| 2    | Jade W.      | Singing       |
| 3    | Victor J.    | Singing       |
| 4    | Elvis Q.     | Eating        |
| 5    | Daniel A.    | Eating        |
| 6    | Bob B.       | Horse Riding  |
+------+--------------+---------------+

Activities table:
+------+--------------+
| id   | name         |
+------+--------------+
| 1    | Eating       |
| 2    | Singing      |
| 3    | Horse Riding |
+------+--------------+

Result table:
+--------------+
| activity     |
+--------------+
| Singing      |
+--------------+

Eating activity is performed by 3 friends, maximum number of participants, (Jonathan D. , Elvis Q. and Daniel A.)
Horse Riding activity is performed by 1 friend, minimum number of participants, (Bob B.)
Singing is performed by 2 friends (Victor J. and Jade W.)
```

```
# Write your MySQL query statement below
select activity from Friends group by activity having count(*) > some(
select count(f.id) from Friends f group by activity) and count(*) < some(
select count(f.id) from Friends f group by activity);

```