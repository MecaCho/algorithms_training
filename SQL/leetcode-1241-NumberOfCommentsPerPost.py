'''
1241. 每个帖子的评论数
SQL架构
表 Submissions 结构如下：

+---------------+----------+
| 列名           | 类型     |
+---------------+----------+
| sub_id        | int      |
| parent_id     | int      |
+---------------+----------+
上表没有主键, 所以可能会出现重复的行。
每行可以是一个帖子或对该帖子的评论。
如果是帖子的话，parent_id 就是 null。
对于评论来说，parent_id 就是表中对应帖子的 sub_id。


编写 SQL 语句以查找每个帖子的评论数。

结果表应包含帖子的 post_id 和对应的评论数 number_of_comments 并且按 post_id 升序排列。

Submissions 可能包含重复的评论。您应该计算每个帖子的唯一评论数。

Submissions 可能包含重复的帖子。您应该将它们视为一个帖子。

查询结果格式如下例所示：

Submissions table:
+---------+------------+
| sub_id  | parent_id  |
+---------+------------+
| 1       | Null       |
| 2       | Null       |
| 1       | Null       |
| 12      | Null       |
| 3       | 1          |
| 5       | 2          |
| 3       | 1          |
| 4       | 1          |
| 9       | 1          |
| 10      | 2          |
| 6       | 7          |
+---------+------------+

结果表：
+---------+--------------------+
| post_id | number_of_comments |
+---------+--------------------+
| 1       | 3                  |
| 2       | 2                  |
| 12      | 0                  |
+---------+--------------------+

表中 ID 为 1 的帖子有 ID 为 3、4 和 9 的三个评论。表中 ID 为 3 的评论重复出现了，所以我们只对它进行了一次计数。
表中 ID 为 2 的帖子有 ID 为 5 和 10 的两个评论。
ID 为 12 的帖子在表中没有评论。
表中 ID 为 6 的评论是对 ID 为 7 的已删除帖子的评论，因此我们将其忽略。

1241. Number of Comments per Post
SQL架构
Table: Submissions

+---------------+----------+
| Column Name   | Type     |
+---------------+----------+
| sub_id        | int      |
| parent_id     | int      |
+---------------+----------+
There is no primary key for this table, it may have duplicate rows.
Each row can be a post or comment on the post.
parent_id is null for posts.
parent_id for comments is sub_id for another post in the table.


Write an SQL query to find number of comments per each post.

Result table should contain post_id and its corresponding number_of_comments, and must be sorted by post_id in ascending order.

Submissions may contain duplicate comments. You should count the number of unique comments per post.

Submissions may contain duplicate posts. You should treat them as one post.

The query result format is in the following example:

Submissions table:
+---------+------------+
| sub_id  | parent_id  |
+---------+------------+
| 1       | Null       |
| 2       | Null       |
| 1       | Null       |
| 12      | Null       |
| 3       | 1          |
| 5       | 2          |
| 3       | 1          |
| 4       | 1          |
| 9       | 1          |
| 10      | 2          |
| 6       | 7          |
+---------+------------+

Result table:
+---------+--------------------+
| post_id | number_of_comments |
+---------+--------------------+
| 1       | 3                  |
| 2       | 2                  |
| 12      | 0                  |
+---------+--------------------+

The post with id 1 has three comments in the table with id 3, 4 and 9. The comment with id 3 is repeated in the table, we counted it only once.
The post with id 2 has two comments in the table with id 5 and 10.
The post with id 12 has no comments in the table.
The comment with id 6 is a comment on a deleted post with id 7 so we ignored it.
'''





'''
# Write your MySQL query statement below
-- select  s1 
-- select parent_id post_id, count(distinct sub_id) number_of_comments from Submissions s1 left join Submissions s2 on s1. where parent_id in (select distinct sub_id from Submissions where parent_id is null) group by parent_id;

select t.sub_id as post_id, ifnull(count(distinct s.sub_id),0) as number_of_comments from submissions s right join (select sub_id from submissions where parent_id is null) t on s.parent_id = t.sub_id group by t.sub_id;

'''

