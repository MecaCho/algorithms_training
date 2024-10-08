# encoding=utf8

'''
134. Gas Station
There are N gas stations along a circular route, where the amount of gas at station i is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.

Return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1.

Note:

If there exists a solution, it is guaranteed to be unique.
Both input arrays are non-empty and have the same length.
Each element in the input arrays is a non-negative integer.
Example 1:

Input: 
gas  = [1,2,3,4,5]
cost = [3,4,5,1,2]

Output: 3

Explanation:
Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 4. Your tank = 4 - 1 + 5 = 8
Travel to station 0. Your tank = 8 - 2 + 1 = 7
Travel to station 1. Your tank = 7 - 3 + 2 = 6
Travel to station 2. Your tank = 6 - 4 + 3 = 5
Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
Therefore, return 3 as the starting index.
Example 2:

Input: 
gas  = [2,3,4]
cost = [3,4,3]

Output: -1

Explanation:
You can't start at station 0 or 1, as there is not enough gas to travel to the next station.
Let's start at station 2 and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 0. Your tank = 4 - 3 + 2 = 3
Travel to station 1. Your tank = 3 - 3 + 3 = 3
You cannot travel back to station 2, as it requires 4 unit of gas but you only have 3.
Therefore, you can't travel around the circuit once no matter where you start.

加油站
在一条环路上有 N 个加油站，其中第 i 个加油站有汽油 gas[i] 升。

你有一辆油箱容量无限的的汽车，从第 i 个加油站开往第 i+1 个加油站需要消耗汽油 cost[i] 升。你从其中的一个加油站出发，开始时油箱为空。

如果你可以绕环路行驶一周，则返回出发时加油站的编号，否则返回 -1。

说明: 

如果题目有解，该答案即为唯一答案。
输入数组均为非空数组，且长度相同。
输入数组中的元素均为非负数。
示例 1:

输入: 
gas  = [1,2,3,4,5]
cost = [3,4,5,1,2]

输出: 3

解释:
从 3 号加油站(索引为 3 处)出发，可获得 4 升汽油。此时油箱有 = 0 + 4 = 4 升汽油
开往 4 号加油站，此时油箱有 4 - 1 + 5 = 8 升汽油
开往 0 号加油站，此时油箱有 8 - 2 + 1 = 7 升汽油
开往 1 号加油站，此时油箱有 7 - 3 + 2 = 6 升汽油
开往 2 号加油站，此时油箱有 6 - 4 + 3 = 5 升汽油
开往 3 号加油站，你需要消耗 5 升汽油，正好足够你返回到 3 号加油站。
因此，3 可为起始索引。
示例 2:

输入: 
gas  = [2,3,4]
cost = [3,4,3]

输出: -1

解释:
你不能从 0 号或 1 号加油站出发，因为没有足够的汽油可以让你行驶到下一个加油站。
我们从 2 号加油站出发，可以获得 4 升汽油。 此时油箱有 = 0 + 4 = 4 升汽油
开往 0 号加油站，此时油箱有 4 - 3 + 2 = 3 升汽油
开往 1 号加油站，此时油箱有 3 - 3 + 3 = 3 升汽油
你无法返回 2 号加油站，因为返程需要消耗 4 升汽油，但是你的油箱只有 3 升汽油。
因此，无论怎样，你都不可能绕环路行驶一周。

'''

class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """

        def cycle_check(start):
            length = len(gas)
            gas_has = 0
            remian = 0
            seq = 0
            for i in range(length):
                seq = (start + i) % length
                if gas_has + gas[seq] < cost[seq]:
                    return False

                remain = gas[seq] - cost[seq]
                gas_has += remain
                # print(gas_has, seq, "seq;", gas_has + gas[seq], cost[seq])

            # if gas_has + gas[seq+1] - cost[seq+1] >= 0:
            return True

        asserts = []
        begins = []
        for i in range(len(gas)):
            remain = gas[i] - cost[i]
            asserts.append(remain)
            if remain >= 0:
                begins.append(i)
        for start in begins:
            # print(start)
            if cycle_check(start):
                return start
        return -1


class Solution20201118(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        length = len(gas)
        for i in range(length):
            sum_gas, sum_cost, cnt = 0,0,0
            while cnt < length:
                j = (i + cnt) % length
                sum_gas += gas[j]
                sum_cost += cost[j]
                if sum_cost <= sum_gas:
                    cnt += 1
                else:
                    break
            if cnt == length:
                return i
            else:
                i += cnt + 1

        return -1

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        i = 0
        while i < n:
            sum_gas = sum_cost = 0
            cnt = 0
            while cnt < n:
                j = (i+cnt) % n
                sum_gas += gas[j]
                sum_cost += cost[j]
                if sum_cost > sum_gas:
                    break
                cnt += 1
            if cnt == n:
                return i
            else:
                i += cnt + 1
        return -1


if __name__ == '__main__':
    demo = Solution()
    # [4,5,2,6,5,3]
# [3,2,7,3,2,9]
    # gas = [1, 2, 3, 4, 5]
    # cost = [3, 4, 5, 1, 2]
    # gas = [5, 1, 2, 3, 4]
    # cost = [4, 4, 1, 5, 1]

    gas =  [4,5,2, 6, 5, 3]
    cost = [3,2,7, 3, 2, 9]
    print(demo.canCompleteCircuit(gas, cost))


# solution

'''
方法一：一次遍历
思路与算法

最容易想到的解法是：从头到尾遍历每个加油站，并检查以该加油站为起点，最终能否行驶一周。我们可以通过减小被检查的加油站数目，来降低总的时间复杂度。

假设我们此前发现，从加油站 xx 出发，每经过一个加油站就加一次油（包括起始加油站），最后一个可以到达的加油站是 yy（不妨设 x<yx<y）。这就说明：

\sum_{i=x}^{y}\textit{gas}[i] < \sum_{i=x}^{y}\textit{cost}[i] \\ \sum_{i=x}^{j}gas[i] \ge \sum_{i=x}^{j}cost[i] ~ \text{(For all $j \in [x, y)$) }
i=x
∑
y
​	
 gas[i]< 
i=x
∑
y
​	
 cost[i]
i=x
∑
j
​	
 gas[i]≥ 
i=x
∑
j
​	
 cost[i] (For all j∈[x,y)) 

第一个式子表明无法到达加油站 yy 的下一个加油站，第二个式子表明可以到达 yy 以及 yy 之前的所有加油站。

现在，考虑任意一个位于 x,yx,y 之间的加油站 zz（包括 xx 和 yy），我们现在考察从该加油站出发，能否到达加油站 yy 的下一个加油站，也就是要判断 \sum_{i=z}^{y}\textit{gas}[i]∑ 
i=z
y
​	
 gas[i] 与 \sum_{i=z}^{y}\textit{cost}[i]∑ 
i=z
y
​	
 cost[i] 之间的大小关系。

根据上面的式子，我们得到：

\begin{aligned} \sum_{i=z}^{y}\textit{gas}[i]&=\sum_{i=x}^{y}\textit{gas}[i]-\sum_{i=x}^{z-1}\textit{gas}[i] \\ &< \sum_{i=x}^{y}\textit{cost}[i]-\sum_{i=x}^{z-1}\textit{gas}[i] \\ &< \sum_{i=x}^{y}\textit{cost}[i]-\sum_{i=x}^{z-1}cost[i] \\ &= \sum_{i=z}^{y}\textit{cost}[i] \end{aligned}
i=z
∑
y
​	
 gas[i]
​	
  
= 
i=x
∑
y
​	
 gas[i]− 
i=x
∑
z−1
​	
 gas[i]
< 
i=x
∑
y
​	
 cost[i]− 
i=x
∑
z−1
​	
 gas[i]
< 
i=x
∑
y
​	
 cost[i]− 
i=x
∑
z−1
​	
 cost[i]
= 
i=z
∑
y
​	
 cost[i]
​	
 

其中不等式的第二步、第三步分别利用了上面的第一个、第二个不等式。

从上面的推导中，能够得出结论：从 x,yx,y 之间的任何一个加油站出发，都无法到达加油站 yy 的下一个加油站。

在发现了这一个性质后，算法就很清楚了：我们首先检查第 00 个加油站，并试图判断能否环绕一周；如果不能，就从第一个无法到达的加油站开始继续检查。

代码

C++JavaGolangCJavaScript

func canCompleteCircuit(gas []int, cost []int) int {
    for i, n := 0, len(gas); i < n; {
        sumOfGas, sumOfCost, cnt := 0, 0, 0
        for cnt < n {
            j := (i + cnt) % n
            sumOfGas += gas[j]
            sumOfCost += cost[j]
            if sumOfCost > sumOfGas {
                break
            }
            cnt++
        }
        if cnt == n {
            return i
        } else {
            i += cnt + 1
        }
    }
    return -1
}
复杂度分析

时间复杂度：O(N)O(N)，其中 NN 为数组的长度。我们对数组进行了单次遍历。

空间复杂度：O(1)O(1)。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/gas-station/solution/jia-you-zhan-by-leetcode-solution/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
