# 613. Shortest Distance in a Line

```bash

SQL架构
Table point holds the x coordinate of some points on x-axis in a plane, which are all integers.
 

Write a query to find the shortest distance between two points in these points.
 

| x   |
|-----|
| -1  |
| 0   |
| 2   |
 

The shortest distance is '1' obviously, which is from point '-1' to '0'. So the output is as below:
 

| shortest|
|---------|
| 1       |
 

Note: Every point is unique, which means there is no duplicates in table point.
 

Follow-up: What if all these points have an id and are arranged from the left most to the right most of x axis?

613. 直线上的最近距离
SQL架构
表 point 保存了一些点在 x 轴上的坐标，这些坐标都是整数。

 

写一个查询语句，找到这些点中最近两个点之间的距离。

 

| x   |
|-----|
| -1  |
| 0   |
| 2   |
 

最近距离显然是 '1' ，是点 '-1' 和 '0' 之间的距离。所以输出应该如下：

 

| shortest|
|---------|
| 1       |
 

注意：每个点都与其他点坐标不同，表 table 不会有重复坐标出现。

 

进阶：如果这些点在 x 轴上从左到右都有一个编号，输出结果时需要输出最近点对的编号呢？

```



# Write your MySQL query statement below
```bash
select min(abs(p1.x - p2.x)) shortest from point p1 join point p2 on p1.x <> p2.x;
```
