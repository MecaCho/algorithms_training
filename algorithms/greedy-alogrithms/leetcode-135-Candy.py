'''
135. 分发糖果
老师想给孩子们分发糖果，有 N 个孩子站成了一条直线，老师会根据每个孩子的表现，预先给他们评分。

你需要按照以下要求，帮助老师给这些孩子分发糖果：

每个孩子至少分配到 1 个糖果。
相邻的孩子中，评分高的孩子必须获得更多的糖果。
那么这样下来，老师至少需要准备多少颗糖果呢？

示例 1:

输入: [1,0,2]
输出: 5
解释: 你可以分别给这三个孩子分发 2、1、2 颗糖果。
示例 2:

输入: [1,2,2]
输出: 4
解释: 你可以分别给这三个孩子分发 1、2、1 颗糖果。
     第三个孩子只得到 1 颗糖果，这已满足上述两个条件。

135. Candy
There are N children standing in a line. Each child is assigned a rating value.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
What is the minimum candies you must give?

Example 1:

Input: [1,0,2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
Example 2:

Input: [1,2,2]
Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
             The third child gets 1 candy because it satisfies the above two conditions.
'''



class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        counts = [0] + [1 for i in range(len(ratings))]
        ratings = [float("inf")] + ratings + [float("inf")]
        for i in range(1, len(ratings ) -1):
            if ratings[i] > ratings[ i -1]:
                counts[i] += counts[ i -1]

            if ratings[i] > ratings[ i +1] and ratings[i] <= ratings[ i -1]:
                counts[i] += 1
        # print(counts)
        for j in range(len(ratings ) -2, 0, -1):
            if ratings[j] > ratings[ j +1] and counts[j] <= counts[ j +1]:
                counts[j] = counts[ j +1] + 1
        # print(counts)
        return sum(counts)