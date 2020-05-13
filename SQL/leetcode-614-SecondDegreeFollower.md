
# 614. Second Degree Follower

```
614. 二级关注者
SQL架构
在 facebook 中，表 follow 会有 2 个字段： followee, follower ，分别表示被关注者和关注者。

请写一个 sql 查询语句，对每一个关注者，查询关注他的关注者的数目。

比方说：

+-------------+------------+
| followee    | follower   |
+-------------+------------+
|     A       |     B      |
|     B       |     C      |
|     B       |     D      |
|     D       |     E      |
+-------------+------------+
应该输出：

+-------------+------------+
| follower    | num        |
+-------------+------------+
|     B       |  2         |
|     D       |  1         |
+-------------+------------+
解释：

B 和 D 都在在 follower 字段中出现，作为被关注者，B 被 C 和 D 关注，D 被 E 关注。A 不在 follower 字段内，所以A不在输出列表中。

 

注意：

被关注者永远不会被他 / 她自己关注。
将结果按照字典序返回。


614. Second Degree Follower
SQL架构
In facebook, there is a follow table with two columns: followee, follower.

Please write a sql query to get the amount of each follower’s follower if he/she has one.

For example:

+-------------+------------+
| followee    | follower   |
+-------------+------------+
|     A       |     B      |
|     B       |     C      |
|     B       |     D      |
|     D       |     E      |
+-------------+------------+
should output:
+-------------+------------+
| follower    | num        |
+-------------+------------+
|     B       |  2         |
|     D       |  1         |
+-------------+------------+
Explaination:
Both B and D exist in the follower list, when as a followee, B's follower is C and D, and D's follower is E. A does not exist in follower list.
 

 

Note:
Followee would not follow himself/herself in all cases.
Please display the result in follower's alphabet order.
```


```
# Write your MySQL query statement below

select followee follower, count(distinct follower) num from follow where followee in (select distinct follower from follow) group by followee;
```