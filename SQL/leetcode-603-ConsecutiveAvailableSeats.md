# 603. Consecutive Available Seats

```
SQL架构
Several friends at a cinema ticket office would like to reserve consecutive available seats.
Can you help to query all the consecutive available seats order by the seat_id using the following cinema table?
| seat_id | free |
|---------|------|
| 1       | 1    |
| 2       | 0    |
| 3       | 1    |
| 4       | 1    |
| 5       | 1    |
 

Your query should return the following result for the sample case above.
 

| seat_id |
|---------|
| 3       |
| 4       |
| 5       |
Note:
The seat_id is an auto increment int, and free is bool ('1' means free, and '0' means occupied.).
Consecutive available seats are more than 2(inclusive) seats consecutively available.

603. 连续空余座位
SQL架构
几个朋友来到电影院的售票处，准备预约连续空余座位。

你能利用表 cinema ，帮他们写一个查询语句，获取所有空余座位，并将它们按照 seat_id 排序后返回吗？

| seat_id | free |
|---------|------|
| 1       | 1    |
| 2       | 0    |
| 3       | 1    |
| 4       | 1    |
| 5       | 1    |
 

对于如上样例，你的查询语句应该返回如下结果。

 

| seat_id |
|---------|
| 3       |
| 4       |
| 5       |
注意：

seat_id 字段是一个自增的整数，free 字段是布尔类型（'1' 表示空余， '0' 表示已被占据）。
连续空余座位的定义是大于等于 2 个连续空余的座位。
```

# Write your MySQL query statement below

```
select distinct c1.seat_id from cinema c1,cinema c2 where abs(c1.seat_id-c2.seat_id)=1 and c1.free=1 and c2.free=1 order by seat_id;
-- select distinct a.seat_id
-- from cinema a join cinema b
--   on abs(a.seat_id - b.seat_id) = 1
--   and a.free = true and b.free = true
-- order by a.seat_id
-- ;

```
