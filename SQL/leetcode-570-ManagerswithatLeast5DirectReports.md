

# 570. Managers with at Least 5 Direct Reports


```
570. 至少有5名直接下属的经理
SQL架构
Employee 表包含所有员工和他们的经理。每个员工都有一个 Id，并且还有一列是经理的 Id。

+------+----------+-----------+----------+
|Id    |Name 	  |Department |ManagerId |
+------+----------+-----------+----------+
|101   |John 	  |A 	      |null      |
|102   |Dan 	  |A 	      |101       |
|103   |James 	  |A 	      |101       |
|104   |Amy 	  |A 	      |101       |
|105   |Anne 	  |A 	      |101       |
|106   |Ron 	  |B 	      |101       |
+------+----------+-----------+----------+
给定 Employee 表，请编写一个SQL查询来查找至少有5名直接下属的经理。对于上表，您的SQL查询应该返回：

+-------+
| Name  |
+-------+
| John  |
+-------+
注意:
没有人是自己的下属。


570. Managers with at Least 5 Direct Reports
SQL架构
The Employee table holds all employees including their managers. Every employee has an Id, and there is also a column for the manager Id.

+------+----------+-----------+----------+
|Id    |Name 	  |Department |ManagerId |
+------+----------+-----------+----------+
|101   |John 	  |A 	      |null      |
|102   |Dan 	  |A 	      |101       |
|103   |James 	  |A 	      |101       |
|104   |Amy 	  |A 	      |101       |
|105   |Anne 	  |A 	      |101       |
|106   |Ron 	  |B 	      |101       |
+------+----------+-----------+----------+
Given the Employee table, write a SQL query that finds out managers with at least 5 direct report. For the above table, your SQL query should return:

+-------+
| Name  |
+-------+
| John  |
+-------+
Note:
No one would report to himself.
```

# Write your MySQL query statement below

```
# Write your MySQL query statement below
select Name from Employee where Id in (
    select ManagerId from Employee group by ManagerId having count(Id)>=5
);

-- SELECT
--     Name
-- FROM
--     Employee AS t1 JOIN
--     (SELECT
--         ManagerId
--     FROM
--         Employee
--     GROUP BY ManagerId
--     HAVING COUNT(ManagerId) >= 5) AS t2
--     ON t1.Id = t2.ManagerId
-- ;

```