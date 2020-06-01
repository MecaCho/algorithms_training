'''
544. 输出比赛匹配对
在 NBA 季后赛中，我们总是安排较强的队伍对战较弱的队伍，例如用排名第 1 的队伍和第 n 的队伍对决，这是一个可以让比赛更加有趣的好策略。现在，给你 n 支队伍，你需要以字符串格式输出它们的 最终 比赛配对。

n 支队伍按从 1 到 n 的正整数格式给出，分别代表它们的初始排名（排名 1 最强，排名 n 最弱）。我们用括号（'(', ')'）和逗号（','）来表示匹配对——括号（'(', ')'）表示匹配，逗号（','）来用于分割。 在每一轮的匹配过程中，你都需要遵循将强队与弱队配对的原则。



示例 1：

输入: 2
输出: (1,2)
解析:
初始地，我们有队1和队2两支队伍，按照1，2排列。
因此 用 '(', ')' 和 ','来将队1和队2进行配对，得到最终答案。
示例 2：

输入: 4
输出: ((1,4),(2,3))
解析:
在第一轮，我们将队伍1和4配对，2和3配对，以满足将强队和弱队搭配的效果。得到(1,4),(2,3).
在第二轮，(1,4) 和 (2,3) 的赢家需要进行比赛以确定最终赢家，因此需要再在外面加一层括号。
于是最终答案是((1,4),(2,3))。
示例 3：

输入: 8
输出: (((1,8),(4,5)),((2,7),(3,6)))
解析:
第一轮: (1,8),(2,7),(3,6),(4,5)
第二轮: ((1,8),(4,5)),((2,7),(3,6))
第三轮 (((1,8),(4,5)),((2,7),(3,6)))
由于第三轮会决出最终胜者，故输出答案为(((1,8),(4,5)),((2,7),(3,6)))。


注意:

n 的范围是 [2, 212].
保证 n 可以写成 2k 的形式，其中 k 是正整数。


544. Output Contest Matches
During the NBA playoffs, we always arrange the rather strong team to play with the rather weak team, like make the rank 1 team play with the rank nth team, which is a good strategy to make the contest more interesting. Now, you're given n teams, you need to output their final contest matches in the form of a string.

The n teams are given in the form of positive integers from 1 to n, which represents their initial rank. (Rank 1 is the strongest team and Rank n is the weakest team.) We'll use parentheses('(', ')') and commas(',') to represent the contest team pairing - parentheses('(' , ')') for pairing and commas(',') for partition. During the pairing process in each round, you always need to follow the strategy of making the rather strong one pair with the rather weak one.

Example 1:
Input: 2
Output: (1,2)
Explanation:
Initially, we have the team 1 and the team 2, placed like: 1,2.
Then we pair the team (1,2) together with '(', ')' and ',', which is the final answer.
Example 2:
Input: 4
Output: ((1,4),(2,3))
Explanation:
In the first round, we pair the team 1 and 4, the team 2 and 3 together, as we need to make the strong team and weak team together.
And we got (1,4),(2,3).
In the second round, the winners of (1,4) and (2,3) need to play again to generate the final winner, so you need to add the paratheses outside them.
And we got the final answer ((1,4),(2,3)).
Example 3:
Input: 8
Output: (((1,8),(4,5)),((2,7),(3,6)))
Explanation:
First round: (1,8),(2,7),(3,6),(4,5)
Second round: ((1,8),(4,5)),((2,7),(3,6))
Third round: (((1,8),(4,5)),((2,7),(3,6)))
Since the third round will generate the final winner, you need to output the answer (((1,8),(4,5)),((2,7),(3,6))).
Note:
The n is in range [2, 212].
We ensure that the input n can be converted into the form 2k, where k is a positive integer.
'''


class Solution(object):
    def findContestMatch(self, n):
        """
        :type n: int
        :rtype: str
        """
        maches = []
        for i in range(n /2):
            maches.append(( i +1, n- i))
        maches = sorted(maches)

        # print(maches)

        def match(maches):
            if not maches:
                return
            if len(maches) == 1:
                return maches[0]
            if len(maches) == 2:
                return (maches[0], maches[1])
            res = []
            while maches:
                res.append(match([maches.pop(0), maches.pop()]))

            return match(res)

        res = match(maches)
        # print(res)

        return "".join([i for i in str(res).split() if i])

# solutions

'''
方法 1：模拟
想法

team[i] 为当前轮第 i 强的队伍。我们依照轮次维护这些信息。

算法

每轮中，第 i 个队伍变成 "(" + team[i] + "," + team[n-1-i] + ")"，然后只剩下一半的队伍。

pythonjava
class Solution(object):
    def findContestMatch(self, n):
        team = map(str, range(1, n+1))

        while n > 1:
            for i in xrange(n / 2):
                team[i] = "({},{})".format(team[i], team.pop())
            n /= 2

        return team[0]
复杂度分析

时间复杂度：O(N\log N)O(NlogN)，O(\log N)O(logN) 轮每轮会有 O(N)O(N) 的工作。
空间复杂度：O(N\log N)O(NlogN)。
方法 2：线性输出
想法

尝试在线性时间内解决这个问题。我们可以把这个问题看成两个部分：输出正确序列的括号和逗号，输出正确的队伍编号。显然可以证明这个线性时间算法是存在的。

算法

首先观察括号。通过递归我们会发现这个结果，例如 N = 8 令 R = log_2(N) = 3 是轮数。括号和逗号形如：

(((x,x),(x,x)),((x,x),(x,x)))
这个仅仅通过递归实现

"(" + (sequence for R = 2) + "," + (sequence for R = 2) + ")"
= "(" + "((x,x),(x,x))" + "," + "((x,x),(x,x))" + ")"
现在观察队伍编号，对于 N = 16 的情况为：

team = [1, 16, 8, 9, 4, 13, 5, 12, 2, 15, 7, 10, 3, 14, 6, 11]

我们会发现相邻两个元素的和为 17。更具体化会有，坐标 0 和 1（在模 2 情况下）和为 17，坐标 0 和 2（在模 4 情况下）和为 9，坐标 0 和 4（在模 8 情况下）和为 5，以此类推。

通俗表示为：坐标 0 和 2^r（在模 2^{r+1} 情况下）和为 N * 2^{-r} + 1。

如果我们希望找到下一个 team[i]，那么最低位的 i 会帮助我们决定他的邻居。例如：team[12] = team[0b1100] 的最低位是 w = 4 = 0b100，所以 12 最近的邻居是 12 - w = 8，所以这两个编号之和为 N / w + 1。

pythonjava
class Solution(object):
    def findContestMatch(self, n):
        team = []
        ans = []
        def write(r):
            if r == 0:
                i = len(team)
                w = i & -i
                team.append(n/w+1 - team[i-w] if w else 1)
                ans.append(str(team[-1]))
            else:
                ans.append("(")
                write(r-1)
                ans.append(",")
                write(r-1)
                ans.append(")")

        write(int(math.log(n, 2)))
        return "".join(ans)
复杂度分析

时间复杂度：O(N)O(N)，我们按顺序打印 O(N)O(N) 个字符。
空间复杂度：O(N)O(N)。

作者：LeetCode
链接：https://leetcode-cn.com/problems/output-contest-matches/solution/shu-chu-bi-sai-pi-pei-dui-by-leetcode/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''