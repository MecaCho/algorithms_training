
# 1204. Last Person to Fit in the Elevator

```
1204. 最后一个能进入电梯的人
SQL架构
表: Queue

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| person_id   | int     |
| person_name | varchar |
| weight      | int     |
| turn        | int     |
+-------------+---------+
person_id 是这个表的主键。
该表展示了所有等待电梯的人的信息。
表中 person_id 和 turn 列将包含从 1 到 n 的所有数字，其中 n 是表中的行数。
 

电梯最大载重量为 1000。

写一条 SQL 查询语句查找最后一个能进入电梯且不超过重量限制的 person_name 。题目确保队列中第一位的人可以进入电梯 。

查询结果如下所示 :

Queue 表
+-----------+-------------------+--------+------+
| person_id | person_name       | weight | turn |
+-----------+-------------------+--------+------+
| 5         | George Washington | 250    | 1    |
| 3         | John Adams        | 350    | 2    |
| 6         | Thomas Jefferson  | 400    | 3    |
| 2         | Will Johnliams    | 200    | 4    |
| 4         | Thomas Jefferson  | 175    | 5    |
| 1         | James Elephant    | 500    | 6    |
+-----------+-------------------+--------+------+

Result 表
+-------------------+
| person_name       |
+-------------------+
| Thomas Jefferson  |
+-------------------+

为了简化，Queue 表按 trun 列由小到大排序。
上例中 George Washington(id 5), John Adams(id 3) 和 Thomas Jefferson(id 6) 将可以进入电梯,因为他们的体重和为 250 + 350 + 400 = 1000。
Thomas Jefferson(id 6) 是最后一个体重合适并进入电梯的人。

1204. Last Person to Fit in the Elevator
SQL架构
Table: Queue

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| person_id   | int     |
| person_name | varchar |
| weight      | int     |
| turn        | int     |
+-------------+---------+
person_id is the primary key column for this table.
This table has the information about all people waiting for an elevator.
The person_id and turn columns will contain all numbers from 1 to n, where n is the number of rows in the table.
 

The maximum weight the elevator can hold is 1000.

Write an SQL query to find the person_name of the last person who will fit in the elevator without exceeding the weight limit. It is guaranteed that the person who is first in the queue can fit in the elevator.

The query result format is in the following example:

Queue table
+-----------+-------------------+--------+------+
| person_id | person_name       | weight | turn |
+-----------+-------------------+--------+------+
| 5         | George Washington | 250    | 1    |
| 3         | John Adams        | 350    | 2    |
| 6         | Thomas Jefferson  | 400    | 3    |
| 2         | Will Johnliams    | 200    | 4    |
| 4         | Thomas Jefferson  | 175    | 5    |
| 1         | James Elephant    | 500    | 6    |
+-----------+-------------------+--------+------+

Result table
+-------------------+
| person_name       |
+-------------------+
| Thomas Jefferson  |
+-------------------+

Queue table is ordered by turn in the example for simplicity.
In the example George Washington(id 5), John Adams(id 3) and Thomas Jefferson(id 6) will enter the elevator as their weight sum is 250 + 350 + 400 = 1000.
Thomas Jefferson(id 6) is the last person to fit in the elevator because he has the last turn in these three people.

```






```
# Write your MySQL query statement below

SELECT a.person_name
FROM Queue a, Queue b
WHERE a.turn >= b.turn
GROUP BY a.person_id HAVING SUM(b.weight) <= 1000
ORDER BY a.turn DESC
LIMIT 1;


```

```
select person_name
from Queue q1
where (select sum(weight) from Queue where turn <= q1.turn) <= 1000
order by turn desc limit 1

```

# solutions

```
方法一：自连接
思路

我们需要根据 turn 排序， 并累加 weight，找到最后一个使得总和小于等于 1000 的 person_name。

参照题目中的例子：

true = 1, weight = 250, sum = 250
true = 2, weight = 350, sum = 600
true = 3, weight = 400, sum = 1000
我们只需要计算出每个人进去后的总和，找到总和小于等于 1000 的最后一个人即可。

我们可以使用自连接的方法计算直到当前人的重量的总和，即：

Mysql
SELECT * FROM Queue a, Queue b
将 b 表中的每一条数据和 a 表的每一条数据连接。假设 Queue 表有 3 条记录，那么自连接后将会有 9 条数据，分别为 (a1 b1),(a1 b2),(a1 b3),(a2 b1),(a2 b2),(a2 b3),(a3 b1),(a3 b2),(a3 b3) 。

接下来对连接后的数据进行处理，我们使用 a 表的 person_id 表示自身，b 表中的数据表示为包括自己在内的所有人。使用 GROUP BY a.person_id 处理每个人的数据。因为要计算每个人的 weight 加上之前所有人的 weight，使用查询条件 a.turn >= b.turn 找到所有在他之前以及他自己的重量。再使用 SUM 计算总和并过滤掉大于 1000 的数据。

拿到所有满足条件的数据后，只需要再对 a.turn 倒序取第一条即可。

代码

Mysql
SELECT a.person_name
FROM Queue a, Queue b
WHERE a.turn >= b.turn
GROUP BY a.person_id HAVING SUM(b.weight) <= 1000
ORDER BY a.turn DESC
LIMIT 1
方法二：自定义变量
思路

根据上面的思路，我们还可以使用自定义变量。

将每一条记录的 weight 按照 turn 的顺序和自定义变量相加并生成新的记录。生成临时表并处理。

Mysql
SELECT person_name, @pre := @pre + weight AS weight
FROM Queue, (SELECT @pre := 0) tmp
ORDER BY turn
代码

Mysql
SELECT a.person_name
FROM (
	SELECT person_name, @pre := @pre + weight AS weight
	FROM Queue, (SELECT @pre := 0) tmp
	ORDER BY turn
) a
WHERE a.weight <= 1000
ORDER BY a.weight DESC
LIMIT 1

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/last-person-to-fit-in-the-elevator/solution/zui-hou-yi-ge-neng-jin-ru-dian-ti-de-ren-by-leetco/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
```