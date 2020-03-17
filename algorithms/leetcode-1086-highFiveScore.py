'''


1086. High Five
Given a list of scores of different students, return the average score of each student's top five scores in the order of each student's id.

Each entry items[i] has items[i][0] the student's id, and items[i][1] the student's score.  The average score is calculated using integer division.

 

Example 1:

Input: [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]
Output: [[1,87],[2,88]]
Explanation: 
The average of the student with id = 1 is 87.
The average of the student with id = 2 is 88.6. But with integer division their average converts to 88.
 

Note:

1 <= items.length <= 1000
items[i].length == 2
The IDs of the students is between 1 to 1000
The score of the students is between 1 to 100
For each student, there are at least 5 scores

1086. 前五科的均分
给你一个不同学生的分数列表，请按 学生的 id 顺序 返回每个学生 最高的五科 成绩的 平均分。

对于每条 items[i] 记录， items[i][0] 为学生的 id，items[i][1] 为学生的分数。平均分请采用整数除法计算。

 

示例：

输入：[[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]
输出：[[1,87],[2,88]]
解释：
id = 1 的学生平均分为 87。
id = 2 的学生平均分为 88.6。但由于整数除法的缘故，平均分会被转换为 88。
 

提示：

1 <= items.length <= 1000
items[i].length == 2
学生的 ID 在 1 到 1000 之间
学生的分数在 1 到 100 之间
每个学生至少有五个分数

'''



class Solution(object):
    def highFive(self, items):
        """
        :type items: List[List[int]]
        :rtype: List[List[int]]
        """
        from collections import defaultdict
        score_dict = defaultdict(list)
        for id, score in items:
            if len(score_dict[id]) < 5:
                score_dict[id].append(score)
            else:
                score_dict[id] = sorted(score_dict[id])
                if score > score_dict[id][0]:
                    score_dict[id][0] = score
        return [[k, sum(value) / 5] for k, value in score_dict.items()]
