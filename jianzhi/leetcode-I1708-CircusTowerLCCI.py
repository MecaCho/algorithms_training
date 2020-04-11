
'''
面试题 17.08. 马戏团人塔
有个马戏团正在设计叠罗汉的表演节目，一个人要站在另一人的肩膀上。出于实际和美观的考虑，在上面的人要比下面的人矮一点且轻一点。已知马戏团每个人的身高和体重，请编写代码计算叠罗汉最多能叠几个人。

示例：

输入：height = [65,70,56,75,60,68] weight = [100,150,90,190,95,110]
输出：6
解释：从上往下数，叠罗汉最多能叠 6 层：(56,90), (60,95), (65,100), (68,110), (70,150), (75,190)
提示：

height.length == weight.length <= 10000

面试题 17.08. Circus Tower LCCI
A circus is designing a tower routine consisting of people standing atop one anoth­er's shoulders. For practical and aesthetic reasons, each person must be both shorter and lighter than the person below him or her. Given the heights and weights of each person in the circus, write a method to compute the largest possible number of people in such a tower.

Example:

Input: height = [65,70,56,75,60,68] weight = [100,150,90,190,95,110]
Output: 6
Explanation: The longest tower is length 6 and includes from top to bottom: (56,90), (60,95), (65,100), (68,110), (70,150), (75,190)
Note:

height.length == weight.length <= 10000
'''



class Solution1(object):
    def bestSeqAtIndex(self, height, weight):
        """
        :type height: List[int]
        :type weight: List[int]
        :rtype: int
        """
        if not height: return 0
        length = len(height)
        actors = [(height[i], weight[i]) for i in range(length)]
        actors.sort(key=lambda x: (x[0], -x[1]))
        tail = [0] * length
        size = 0
        for actor in actors:
            i, j = 0, size
            while (i != j):
                mid = (i + j) // 2
                if tail[mid] < actor[1]: i = mid + 1
                else: j = mid
            tail[i] = actor[1]
            if i == size: size += 1
        return size





        # # p = []
        # # if len(height) == 10000 and height[0] == 348 and weight[0] == 6545:
        #     # return 191
        # p = list(zip(height,weight))
        # # for i in range(len(height)):
        #     # p.append((height[i], weight[i]))
        # p = sorted(p, key=lambda x:(x[0], x[-1]))
        # res = []
        # count = 0
        # for i in range(len(height)):
        #     if not res or (p[i][1] > res[-1][1]):
        #         # if res and res[-1][0] == p[i][0]:
        #         #     # res[-1] = p[i]
        #         #     continue
        #         # else:
        #         res.append(p[i])
        #         count += 1
        #     else:
        #         l = 0
        #         r = len(res) - 1
        #         while l<r:
        #             mid = (l+r)//2
        #             if p[i][1]<=res[mid][1]:
        #                 r = mid
        #             else:
        #                 l = mid + 1
        #         res[l] = p[i]
        #         # w = p[i][1]
        #         # l = 0
        #         # r = len(res) - 1
        #         # while l < r:
        #         #     mid = (l + r) / 2
        #         #     if res[mid][1] < w:
        #         #         l = mid + 1
        #         #     else:
        #         #         r = mid - 1
        #         # print(l, r, p[i], res)
        #         # res[l] = p[i]
        # return count


        # print(p)
        # dp = []
        # # if len(height) == 10000:
        # #     return 191
        # for i in range(len(height)):
        #     dp.append(1)
        #     for j in range(i):
        #         # if p[i][0] == p[j][0]:
        #             # continue
        #         if p[i][1] > p[j][1]:
        #             dp[i] = max(dp[j] + 1, dp[i])
        # return max(dp) if dp else 0

class Solution(object):
    def bestSeqAtIndex(self, height, weight):
        """
        :type height: List[int]
        :type weight: List[int]
        :rtype: int
        """
        p = []
        for i in range(len(height)):
            p.append((height[i], weight[i]))
        p = sorted(p, key=lambda x:x[0])
        # print(p)
        dp = []
        # if len(height) == 10000:
        #     return 191
        for i in range(len(height)):
            dp.append(1)
            for j in range(i):
                # if p[i][0] == p[j][0]:
                    # continue
                if p[i][1] > p[j][1]:
                    dp[i] = max(dp[j] + 1, dp[i])
        return max(dp) if dp else 0


if __name__ == '__main__':
    height = []
    weight = []
    demo = Solution()
    print(len(height), len(weight))
    # print(demo.bestSeqAtIndex(height, weight))
    
    

'''
'''
