
# 608. Tree Node

```

608. 树节点
SQL架构
给定一个表 tree，id 是树节点的编号， p_id 是它父节点的 id 。

+----+------+
| id | p_id |
+----+------+
| 1  | null |
| 2  | 1    |
| 3  | 1    |
| 4  | 2    |
| 5  | 2    |
+----+------+
树中每个节点属于以下三种类型之一：

叶子：如果这个节点没有任何孩子节点。
根：如果这个节点是整棵树的根，即没有父节点。
内部节点：如果这个节点既不是叶子节点也不是根节点。
 

写一个查询语句，输出所有节点的编号和节点的类型，并将结果按照节点编号排序。上面样例的结果为：

 

+----+------+
| id | Type |
+----+------+
| 1  | Root |
| 2  | Inner|
| 3  | Leaf |
| 4  | Leaf |
| 5  | Leaf |
+----+------+
 

解释

节点 '1' 是根节点，因为它的父节点是 NULL ，同时它有孩子节点 '2' 和 '3' 。
节点 '2' 是内部节点，因为它有父节点 '1' ，也有孩子节点 '4' 和 '5' 。
节点 '3', '4' 和 '5' 都是叶子节点，因为它们都有父节点同时没有孩子节点。
样例中树的形态如下：
 

			  1
			/   \
                      2       3
                    /   \
                  4       5
 

注意

如果树中只有一个节点，你只需要输出它的根属性。


608. Tree Node
SQL架构
Given a table tree, id is identifier of the tree node and p_id is its parent node's id.

+----+------+
| id | p_id |
+----+------+
| 1  | null |
| 2  | 1    |
| 3  | 1    |
| 4  | 2    |
| 5  | 2    |
+----+------+
Each node in the tree can be one of three types:
Leaf: if the node is a leaf node.
Root: if the node is the root of the tree.
Inner: If the node is neither a leaf node nor a root node.
 

Write a query to print the node id and the type of the node. Sort your output by the node id. The result for the above sample is:
 

+----+------+
| id | Type |
+----+------+
| 1  | Root |
| 2  | Inner|
| 3  | Leaf |
| 4  | Leaf |
| 5  | Leaf |
+----+------+
 

Explanation

 

Node '1' is root node, because its parent node is NULL and it has child node '2' and '3'.
Node '2' is inner node, because it has parent node '1' and child node '4' and '5'.
Node '3', '4' and '5' is Leaf node, because they have parent node and they don't have child node.

And here is the image of the sample tree as below:
 

			  1
			/   \
                      2       3
                    /   \
                  4       5
Note

If there is only one node on the tree, you only need to output its root attributes.
```


# Write your MySQL query statement below

```
# Write your MySQL query statement below
select id, "Root" Type from tree where p_id is null union select id, "Leaf" Type from tree where id not in (select distinct p_id from tree where p_id is not null) AND p_id IS NOT NULL union SELECT
    id, 'Inner' AS Type
FROM
    tree
WHERE
    id IN (SELECT DISTINCT
            p_id
        FROM
            tree
        WHERE
            p_id IS NOT NULL)
        AND p_id IS NOT NULL order by id;

```


# solution

```
方法 1：使用 UNION [Accepted]
想法

我们可以按照下面的定义，求出每一条记录的节点类型。

Root: 没有父节点
Inner: 它是某些节点的父节点，且有非空的父节点
Leaf: 除了上述两种情况以外的节点
算法

将上述定义转化，我们可以得到下面的代码。

根节点是没有父节点的节点。

sql
SELECT
    id, 'Root' AS Type
FROM
    tree
WHERE
    p_id IS NULL
叶子节点是没有孩子节点的节点，且它有父亲节点。

sql
SELECT
    id, 'Leaf' AS Type
FROM
    tree
WHERE
    id NOT IN (SELECT DISTINCT
            p_id
        FROM
            tree
        WHERE
            p_id IS NOT NULL)
        AND p_id IS NOT NULL
内部节点是有孩子节点和父节点的节点。

sql
SELECT
    id, 'Inner' AS Type
FROM
    tree
WHERE
    id IN (SELECT DISTINCT
            p_id
        FROM
            tree
        WHERE
            p_id IS NOT NULL)
        AND p_id IS NOT NULL
所以本题的一种解法是将这些情况用 UNION 合并起来。

sql
SELECT
    id, 'Root' AS Type
FROM
    tree
WHERE
    p_id IS NULL

UNION

SELECT
    id, 'Leaf' AS Type
FROM
    tree
WHERE
    id NOT IN (SELECT DISTINCT
            p_id
        FROM
            tree
        WHERE
            p_id IS NOT NULL)
        AND p_id IS NOT NULL

UNION

SELECT
    id, 'Inner' AS Type
FROM
    tree
WHERE
    id IN (SELECT DISTINCT
            p_id
        FROM
            tree
        WHERE
            p_id IS NOT NULL)
        AND p_id IS NOT NULL
ORDER BY id;
方法 II：使用流控制语句 CASE [Accepted]
算法

与上面解法类似，本解法使用流控制语句，流控制语句对基于不同输入产生不同输出非常有效。本方法中，我们使用 CASE 语句。

sql
SELECT
    id AS `Id`,
    CASE
        WHEN tree.id = (SELECT atree.id FROM tree atree WHERE atree.p_id IS NULL)
          THEN 'Root'
        WHEN tree.id IN (SELECT atree.p_id FROM tree atree)
          THEN 'Inner'
        ELSE 'Leaf'
    END AS Type
FROM
    tree
ORDER BY `Id`
;
MySQL 除了 CASE 语句以外还提供了不同的流控制语句。你可以尝试将上面的方法用 IF 重写。

方法 III；使用 IF 函数 [Accepted]
算法

我们还可以使用 IF 函数来避免复杂的流控制语句。

sql
SELECT
    atree.id,
    IF(ISNULL(atree.p_id),
        'Root',
        IF(atree.id IN (SELECT p_id FROM tree), 'Inner','Leaf')) Type
FROM
    tree atree
ORDER BY atree.id

作者：LeetCode
链接：https://leetcode-cn.com/problems/tree-node/solution/shu-jie-dian-by-leetcode/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
```
