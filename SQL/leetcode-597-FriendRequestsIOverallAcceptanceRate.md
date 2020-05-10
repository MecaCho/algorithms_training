
# 597. Friend Requests I: Overall Acceptance Rate

```
597. 好友申请 I ：总体通过率
SQL架构
在 Facebook 或者 Twitter 这样的社交应用中，人们经常会发好友申请也会收到其他人的好友申请。现在给如下两个表：

 

表： friend_request

| sender_id | send_to_id |request_date|
|-----------|------------|------------|
| 1         | 2          | 2016_06-01 |
| 1         | 3          | 2016_06-01 |
| 1         | 4          | 2016_06-01 |
| 2         | 3          | 2016_06-02 |
| 3         | 4          | 2016-06-09 |
 

表： request_accepted

| requester_id | accepter_id |accept_date |
|--------------|-------------|------------|
| 1            | 2           | 2016_06-03 |
| 1            | 3           | 2016-06-08 |
| 2            | 3           | 2016-06-08 |
| 3            | 4           | 2016-06-09 |
| 3            | 4           | 2016-06-10 |
 

写一个查询语句，求出好友申请的通过率，用 2 位小数表示。通过率由接受好友申请的数目除以申请总数。

 

对于上面的样例数据，你的查询语句应该返回如下结果。

 

|accept_rate|
|-----------|
|       0.80|
 

注意:

通过的好友申请不一定都在表 friend_request 中。在这种情况下，你只需要统计总的被通过的申请数（不管它们在不在原来的申请中），并将它除以申请总数，得到通过率
一个好友申请发送者有可能会给接受者发几条好友申请，也有可能一个好友申请会被通过好几次。这种情况下，重复的好友申请只统计一次。
如果一个好友申请都没有，通过率为 0.00 。
 

解释： 总共有 5 个申请，其中 4 个是不重复且被通过的好友申请，所以成功率是 0.80 。

 

进阶:

你能写一个查询语句得到每个月的通过率吗？
你能求出每一天的累计通过率吗？

597. Friend Requests I: Overall Acceptance Rate
SQL架构
In social network like Facebook or Twitter, people send friend requests and accept others’ requests as well. Now given two tables as below:
 

Table: friend_request
| sender_id | send_to_id |request_date|
|-----------|------------|------------|
| 1         | 2          | 2016_06-01 |
| 1         | 3          | 2016_06-01 |
| 1         | 4          | 2016_06-01 |
| 2         | 3          | 2016_06-02 |
| 3         | 4          | 2016-06-09 |
 

Table: request_accepted
| requester_id | accepter_id |accept_date |
|--------------|-------------|------------|
| 1            | 2           | 2016_06-03 |
| 1            | 3           | 2016-06-08 |
| 2            | 3           | 2016-06-08 |
| 3            | 4           | 2016-06-09 |
| 3            | 4           | 2016-06-10 |
 

Write a query to find the overall acceptance rate of requests rounded to 2 decimals, which is the number of acceptance divide the number of requests.
 

For the sample data above, your query should return the following result.
 

|accept_rate|
|-----------|
|       0.80|
 

Note:
The accepted requests are not necessarily from the table friend_request. In this case, you just need to simply count the total accepted requests (no matter whether they are in the original requests), and divide it by the number of requests to get the acceptance rate.
It is possible that a sender sends multiple requests to the same receiver, and a request could be accepted more than once. In this case, the ‘duplicated’ requests or acceptances are only counted once.
If there is no requests at all, you should return 0.00 as the accept_rate.
 

Explanation: There are 4 unique accepted requests, and there are 5 requests in total. So the rate is 0.80.
 

Follow-up:
Can you write a query to return the accept rate but for every month?
How about the cumulative accept rate for every day?
```

# Write your MySQL query statement below

```

-- select
-- round(
--     ifnull(
--     (select count(*) from (select distinct requester_id, accepter_id from request_accepted) as A)
--     /
--     (select count(*) from (select distinct sender_id, send_to_id from friend_request) as B),
--     0)
-- , 2) as accept_rate;

select round(ifnull((select count(*) from (select distinct requester_id, accepter_id from request_accepted) a)/(select count(*) from (select distinct sender_id, send_to_id from friend_request) b),0), 2) as accept_rate;

```