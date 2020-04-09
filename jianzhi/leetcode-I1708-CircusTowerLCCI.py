






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
