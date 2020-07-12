'''
174. Dungeon Game
The demons had captured the princess (P) and imprisoned her in the bottom-right corner of a dungeon. The dungeon consists of M x N rooms laid out in a 2D grid. Our valiant knight (K) was initially positioned in the top-left room and must fight his way through the dungeon to rescue the princess.

The knight has an initial health point represented by a positive integer. If at any point his health point drops to 0 or below, he dies immediately.

Some of the rooms are guarded by demons, so the knight loses health (negative integers) upon entering these rooms; other rooms are either empty (0's) or contain magic orbs that increase the knight's health (positive integers).

In order to reach the princess as quickly as possible, the knight decides to move only rightward or downward in each step.



Write a function to determine the knight's minimum initial health so that he is able to rescue the princess.

For example, given the dungeon below, the initial health of the knight must be at least 7 if he follows the optimal path RIGHT-> RIGHT -> DOWN -> DOWN.

-2 (K)	-3	3
-5	-10	1
10	30	-5 (P)


Note:

The knight's health has no upper bound.
Any room can contain threats or power-ups, even the first room the knight enters and the bottom-right room where the princess is imprisoned.

174. 地下城游戏
一些恶魔抓住了公主（P）并将她关在了地下城的右下角。地下城是由 M x N 个房间组成的二维网格。我们英勇的骑士（K）最初被安置在左上角的房间里，他必须穿过地下城并通过对抗恶魔来拯救公主。

骑士的初始健康点数为一个正整数。如果他的健康点数在某一时刻降至 0 或以下，他会立即死亡。

有些房间由恶魔守卫，因此骑士在进入这些房间时会失去健康点数（若房间里的值为负整数，则表示骑士将损失健康点数）；其他房间要么是空的（房间里的值为 0），要么包含增加骑士健康点数的魔法球（若房间里的值为正整数，则表示骑士将增加健康点数）。

为了尽快到达公主，骑士决定每次只向右或向下移动一步。



编写一个函数来计算确保骑士能够拯救到公主所需的最低初始健康点数。

例如，考虑到如下布局的地下城，如果骑士遵循最佳路径 右 -> 右 -> 下 -> 下，则骑士的初始健康点数至少为 7。

-2 (K)	-3	3
-5	-10	1
10	30	-5 (P)


说明:

骑士的健康点数没有上限。

任何房间都可能对骑士的健康点数造成威胁，也可能增加骑士的健康点数，包括骑士进入的左上角房间以及公主被监禁的右下角房间。
'''

class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """

        row_len, col_len = len(dungeon), len(dungeon[0])
        dp = [[float("inf") for j in range(col_len+1)] for _ in range(row_len+1)]
        dp[row_len-1][col_len], dp[row_len][col_len-1] = 1, 1

        for i in range(row_len-1, -1, -1):
            for j in range(col_len-1, -1, -1):
                dp[i][j] = max(min(dp[i+1][j], dp[i][j+1])-dungeon[i][j], 1)
        return dp[0][0]


# solution

'''
Probably when you see this problem and you have some experience in this type of problems you can guess, that this is dynamic programming problem. However even if you understand this, it is not easy to solve it. Let us use top-down dp, that is Let dp[i][j] be the minimum hp we need to reach the princess if we start from point (i,j). Let us consider the following example:

-2	-3	+3
-5	-10	+1
+10	+30	-5
Let us add bottom dummy row and right dummy column to handle border cases more easy. We fill it with infinities, except two ones - neibours of our princess. I will explain it a bit later.

How we can evaluate dp[i][j]? We need to look at two cells: dp[i+1][j] and dp[i][j+1] and evaluate two possible candidates: dp[i+1][j]-dungeon[i][j] and dp[i][j+1]-dungeon[i][j].

If at least one of these two numbers is negative, it means that we can survive just with 1 hp: (look at number +30 in our table for example)
If both this numbers are positive, we need to take the mimumum of them, see for example number -10 in our table: to survive we need either 5- -10 = 15 if we go right and 1- -10 = 11 if we go down, of course we choose 11.
This conditions can be written in one a bit ugly line: dp[i][j] = max(min(dp[i+1][j],dp[i][j+1])-dungeon[i][j],1).
Finally, why I put 1 to two neibors of princess? To make this formula valid for princess cell: if we have negative number like -5 in this cell, we need 6 hp to survive, if we have non-negative number in this cell, we need 1 hp to survive.
7	5	2	inf
6	11	5	inf
1	1	6	1
inf	inf	1	#

'''