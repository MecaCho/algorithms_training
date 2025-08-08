# encoding=utf8

'''
808. Soup Servings

There are two types of soup: type A and type B. Initially, we have n ml of each type of soup. There are four kinds of operations:

Serve 100 ml of soup A and 0 ml of soup B,
Serve 75 ml of soup A and 25 ml of soup B,
Serve 50 ml of soup A and 50 ml of soup B, and
Serve 25 ml of soup A and 75 ml of soup B.
When we serve some soup, we give it to someone, and we no longer have it. Each turn, we will choose from the four operations with an equal probability 0.25. If the remaining volume of soup is not enough to complete the operation, we will serve as much as possible. We stop once we no longer have some quantity of both types of soup.

Note that we do not have an operation where all 100 ml's of soup B are used first.

Return the probability that soup A will be empty first, plus half the probability that A and B become empty at the same time. Answers within 10-5 of the actual answer will be accepted.

 

Example 1:

Input: n = 50
Output: 0.62500
Explanation: If we choose the first two operations, A will become empty first.
For the third operation, A and B will become empty at the same time.
For the fourth operation, B will become empty first.
So the total probability of A becoming empty first plus half the probability that A and B become empty at the same time, is 0.25 * (1 + 1 + 0.5 + 0) = 0.625.
Example 2:

Input: n = 100
Output: 0.71875
 

Constraints:

0 <= n <= 109

808. 分汤

你有两种汤，A 和 B，每种初始为 n 毫升。在每一轮中，会随机选择以下四种服务操作中的一种，每种操作的概率为 0.25，且与之前的所有轮次 无关：

从汤 A 取 100 毫升，从汤 B 取 0 毫升
从汤 A 取 75 毫升，从汤 B 取 25 毫升
从汤 A 取 50 毫升，从汤 B 取 50 毫升
从汤 A 取 25 毫升，从汤 B 取 75 毫升
注意：

不存在先分配 100 ml 汤B 的操作。
汤 A 和 B 在每次操作中同时被倒入。
如果一次操作要求你倒出比剩余的汤更多的量，请倒出该汤剩余的所有部分。
操作过程在任何回合中任一汤被用完后立即停止。

返回汤 A 在 B 前耗尽的概率，加上两种汤在 同一回合 耗尽概率的一半。返回值在正确答案 10-5 的范围内将被认为是正确的。

 

示例 1:

输入：n = 50
输出：0.62500
解释：
如果我们选择前两个操作，A 首先将变为空。
对于第三个操作，A 和 B 会同时变为空。
对于第四个操作，B 首先将变为空。
所以 A 变为空的总概率加上 A 和 B 同时变为空的概率的一半是 0.25 *(1 + 1 + 0.5 + 0)= 0.625。
示例 2:

输入：n = 100
输出：0.71875
解释：
如果我们选择第一个操作，A 首先将变为空。
如果我们选择第二个操作，A 将在执行操作 [1, 2, 3] 时变为空，然后 A 和 B 在执行操作 4 时同时变空。
如果我们选择第三个操作，A 将在执行操作 [1, 2] 时变为空，然后 A 和 B 在执行操作 3 时同时变空。
如果我们选择第四个操作，A 将在执行操作 1 时变为空，然后 A 和 B 在执行操作 2 时同时变空。
所以 A 变为空的总概率加上 A 和 B 同时变为空的概率的一半是 0.71875。
 

提示:

0 <= n <= 109
'''
