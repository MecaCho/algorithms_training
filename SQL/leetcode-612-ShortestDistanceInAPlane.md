
# 612. Shortest Distance in a Plane

```
612. 平面上的最近距离
SQL架构
表 point_2d 保存了所有点（多于 2 个点）的坐标 (x,y) ，这些点在平面上两两不重合。

 

写一个查询语句找到两点之间的最近距离，保留 2 位小数。

 

| x  | y  |
|----|----|
| -1 | -1 |
| 0  | 0  |
| -1 | -2 |
 

最近距离在点 (-1,-1) 和(-1,2) 之间，距离为 1.00 。所以输出应该为：

 

| shortest |
|----------|
| 1.00     |
 

注意：任意点之间的最远距离小于 10000 。

612. Shortest Distance in a Plane
SQL架构
Table point_2d holds the coordinates (x,y) of some unique points (more than two) in a plane.
 

Write a query to find the shortest distance between these points rounded to 2 decimals.
 

| x  | y  |
|----|----|
| -1 | -1 |
| 0  | 0  |
| -1 | -2 |
 

The shortest distance is 1.00 from point (-1,-1) to (-1,2). So the output should be:
 

| shortest |
|----------|
| 1.00     |
 

Note: The longest distance among all the points are less than 10000.
```

# Write your MySQL query statement below

```
# Write your MySQL query statement below

select round(sqrt(min(pow(p1.x-p2.x, 2) + pow(p1.y - p2.y, 2))), 2) as shortest from point_2d p1 join point_2d p2 on p1.x != p2.x or p1.y != p2.y;

```