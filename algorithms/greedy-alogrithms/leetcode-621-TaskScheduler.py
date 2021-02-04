# encoding=utf8

'''
621. Task Scheduler
Given a characters array tasks, representing the tasks a CPU needs to do, where each letter represents a different task. Tasks could be done in any order. Each task is done in one unit of time. For each unit of time, the CPU could complete either one task or just be idle.

However, there is a non-negative integer n that represents the cooldown period between two same tasks (the same letter in the array), that is that there must be at least n units of time between any two same tasks.

Return the least number of units of times that the CPU will take to finish all the given tasks.



Example 1:

Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation:
A -> B -> idle -> A -> B -> idle -> A -> B
There is at least 2 units of time between any two same tasks.
Example 2:

Input: tasks = ["A","A","A","B","B","B"], n = 0
Output: 6
Explanation: On this case any permutation of size 6 would work since n = 0.
["A","A","A","B","B","B"]
["A","B","A","B","A","B"]
["B","B","B","A","A","A"]
...
And so on.
Example 3:

Input: tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2
Output: 16
Explanation:
One possible solution is
A -> B -> C -> A -> D -> E -> A -> F -> G -> A -> idle -> idle -> A -> idle -> idle -> A


Constraints:

1 <= task.length <= 104
tasks[i] is upper-case English letter.
The integer n is in the range [0, 100].

621. 任务调度器
给你一个用字符数组 tasks 表示的 CPU 需要执行的任务列表。其中每个字母表示一种不同种类的任务。任务可以以任意顺序执行，并且每个任务都可以在 1 个单位时间内执行完。在任何一个单位时间，CPU 可以完成一个任务，或者处于待命状态。

然而，两个 相同种类 的任务之间必须有长度为整数 n 的冷却时间，因此至少有连续 n 个单位时间内 CPU 在执行不同的任务，或者在待命状态。

你需要计算完成所有任务所需要的 最短时间 。



示例 1：

输入：tasks = ["A","A","A","B","B","B"], n = 2
输出：8
解释：A -> B -> (待命) -> A -> B -> (待命) -> A -> B
     在本示例中，两个相同类型任务之间必须间隔长度为 n = 2 的冷却时间，而执行一个任务只需要一个单位时间，所以中间出现了（待命）状态。
示例 2：

输入：tasks = ["A","A","A","B","B","B"], n = 0
输出：6
解释：在这种情况下，任何大小为 6 的排列都可以满足要求，因为 n = 0
["A","A","A","B","B","B"]
["A","B","A","B","A","B"]
["B","B","B","A","A","A"]
...
诸如此类
示例 3：

输入：tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2
输出：16
解释：一种可能的解决方案是：
     A -> B -> C -> A -> D -> E -> A -> F -> G -> A -> (待命) -> (待命) -> A -> (待命) -> (待命) -> A


提示：

1 <= task.length <= 104
tasks[i] 是大写英文字母
n 的取值范围为 [0, 100]
'''


import collections
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        freq = collections.Counter(tasks)

        # 最多的执行次数
        maxExec = max(freq.values())
        # 具有最多执行次数的任务数量
        maxCount = sum(1 for v in freq.values() if v == maxExec)

        return max((maxExec - 1) * (n + 1) + maxCount, len(tasks))


# solutions

'''
方法一：模拟
思路与算法

一种容易想到的方法是，我们按照时间顺序，依次给每一个时间单位分配任务。

那么如果当前有多种任务不在冷却中，那么我们应该如何挑选执行的任务呢？直觉上，我们应当选择剩余执行次数最多的那个任务，将每种任务的剩余执行次数尽可能平均，使得 CPU 处于待命状态的时间尽可能少。当然这也是可以证明的，详细证明见下一个小标题。

因此我们可以用二元组 (\textit{nextValid}_i, \textit{rest}_i)(nextValid 
i
​	
 ,rest 
i
​	
 ) 表示第 ii 个任务，其中 \textit{nextValid}_inextValid 
i
​	
  表示其因冷却限制，最早可以执行的时间；\textit{rest}_irest 
i
​	
  表示其剩余执行次数。初始时，所有的 \textit{nextValid}_inextValid 
i
​	
  均为 11，而 \textit{rest}_irest 
i
​	
  即为任务 ii 在数组 \textit{tasks}tasks 中出现的次数。

我们用 \textit{time}time 记录当前的时间。根据我们的策略，我们需要选择不在冷却中并且剩余执行次数最多的那个任务，也就是说，我们需要找到满足 \textit{nextValid}_i \leq \textit{time}nextValid 
i
​	
 ≤time 的并且 \textit{rest}_irest 
i
​	
  最大的索引 ii。因此我们只需要遍历所有的二元组，即可找到 ii。在这之后，我们将 (\textit{nextValid}_i, \textit{rest}_i)(nextValid 
i
​	
 ,rest 
i
​	
 ) 更新为 (\textit{time}+n+1, \textit{rest}_i-1)(time+n+1,rest 
i
​	
 −1)，记录任务 ii 下一次冷却结束的时间以及剩余执行次数。如果更新后的 \textit{rest}_i=0rest 
i
​	
 =0，那么任务 ii 全部做完，我们在遍历二元组时也就可以忽略它了。

而对于 \textit{time}time 的更新，我们可以选择将其不断增加 11，模拟每一个时间片。但这会导致我们在 CPU 处于待命状态时，对二元组进行不必要的遍历。为了减少时间复杂度，我们可以在每一次遍历之前，将 \textit{time}time 更新为所有 \textit{nextValid}_inextValid 
i
​	
  中的最小值，直接「跳过」待命状态，保证每一次对二元组的遍历都是有效的。需要注意的是，只有当这个最小值大于 \textit{time}time 时，才需要这样快速更新。

证明

对于某个时间点 tt，设任务 aa 和 bb 均不在冷却中，并且它们分别剩余 pp 和 qq 次。不失一般性，假设 p>qp>q，那么我们应当在此时选择任务 aa，但我们选择了任务 bb。我们需要证明，存在一种交换方法，使得将此时的任务 bb「变成」任务 aa 后，总时间不会增加。

为了叙述方便，设 a_1, a_2, \cdots, a_pa 
1
​	
 ,a 
2
​	
 ,⋯,a 
p
​	
  为选择任务 aa 的时间点，b_1, b_2, \cdots, b_qb 
1
​	
 ,b 
2
​	
 ,⋯,b 
q
​	
  为选择任务 bb 的时间点，根据假设有

a_1 > b_1 = t
a 
1
​	
 >b 
1
​	
 =t

以及对于任意相邻的两项 a_i, a_{i+1}a 
i
​	
 ,a 
i+1
​	
  或者 b_j, b_{j+1}b 
j
​	
 ,b 
j+1
​	
 ，均有

a_{i+1} - a_i > n
a 
i+1
​	
 −a 
i
​	
 >n

以及

b_{j+1} - b_j > n
b 
j+1
​	
 −b 
j
​	
 >n

接下来我们分情况讨论：

如果 \exists k' \in [2, q]∃k 
′
 ∈[2,q] 使得 a_{k'} < b_{k'}a 
k 
′
 
​	
 <b 
k 
′
 
​	
 ，那么我们找出其中最小的那个 k'k 
′
  记为 kk。此时我们有

\begin{cases} a_1 > b_1 \\ a_2 > b_2 \\ \cdots \\ a_{k-1} > b_{k-1} \\ a_k < b_k \end{cases}
⎩
⎪
⎪
⎪
⎪
⎪
⎪
⎪
⎨
⎪
⎪
⎪
⎪
⎪
⎪
⎪
⎧
​	
  
a 
1
​	
 >b 
1
​	
 
a 
2
​	
 >b 
2
​	
 
⋯
a 
k−1
​	
 >b 
k−1
​	
 
a 
k
​	
 <b 
k
​	
 
​	
 

那么我们可以构造序列：

b_1, b_2, \cdots, b_{k-1}, a_k, a_{k+1}, \cdots, a_pb 
1
​	
 ,b 
2
​	
 ,⋯,b 
k−1
​	
 ,a 
k
​	
 ,a 
k+1
​	
 ,⋯,a 
p
​	
  作为交换后选择任务 aa 的时间点；
a_1, a_2, \cdots, a_{k-1}, b_k, b_{k+1}, \cdots, b_qa 
1
​	
 ,a 
2
​	
 ,⋯,a 
k−1
​	
 ,b 
k
​	
 ,b 
k+1
​	
 ,⋯,b 
q
​	
  作为交换后选择任务 bb 的时间点。
对于交换后任务 aa 的序列，其一共有 pp 项，并且有

a_k - b_{k-1} > a_k - a_{k-1} > n
a 
k
​	
 −b 
k−1
​	
 >a 
k
​	
 −a 
k−1
​	
 >n

因此其满足任意相邻两项之差大于 nn，不会违反冷却时间的规则。

同理对于对于交换后任务 bb 的序列，其一共有 qq 项，并且有

b_k - a_{k-1} > a_k - a_{k-1} > n
b 
k
​	
 −a 
k−1
​	
 >a 
k
​	
 −a 
k−1
​	
 >n

同样不会违反冷却时间的规则。

如果 \forall k' \in [2, q]∀k 
′
 ∈[2,q] 均有 a_{k'} > b_{k'}a 
k 
′
 
​	
 >b 
k 
′
 
​	
 ，那么我们只要构造序列：

b_1, b_2, \cdots, b_kb 
1
​	
 ,b 
2
​	
 ,⋯,b 
k
​	
  作为交换后选择任务 aa 的时间点；
a_1, a_2, \cdots, a_k, b_{k+1}, \cdots, b_na 
1
​	
 ,a 
2
​	
 ,⋯,a 
k
​	
 ,b 
k+1
​	
 ,⋯,b 
n
​	
  作为交换后选择任务 bb 的时间点。
由于 b_{k+1} - a_k > b_{k+1} - b_k > nb 
k+1
​	
 −a 
k
​	
 >b 
k+1
​	
 −b 
k
​	
 >n，因此不会违反冷却时间的规则。

无论哪一种情况，我们都将 b_1=tb 
1
​	
 =t 变成了选择任务 aa 的时间点，并且由于我们只在任务 aa 和 bb 的内部进行交换，因此交换后总时间一定不会增加。这样就证明了一定存在一种总时间最少的方法，是通过不断地选择不在冷却中并且剩余执行次数最多的那个任务得到的。

代码

C++JavaPython3JavaScriptGolangC

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = collections.Counter(tasks)

        # 任务总数
        m = len(freq)
        nextValid = [1] * m
        rest = list(freq.values())

        time = 0
        for i in range(len(tasks)):
            time += 1
            minNextValid = min(nextValid[j] for j in range(m) if rest[j] > 0)
            time = max(time, minNextValid)
            
            best = -1
            for j in range(m):
                if rest[j] and nextValid[j] <= time:
                    if best == -1 or rest[j] > rest[best]:
                        best = j
            
            nextValid[best] = time + n + 1
            rest[best] -= 1

        return time
复杂度分析

时间复杂度：O(|\textit{tasks}| \cdot |\Sigma|)O(∣tasks∣⋅∣Σ∣)，其中 |\Sigma|∣Σ∣ 是数组 \textit{task}task 中出现任务的种类，在本题中任务用大写字母表示，因此 |\Sigma|∣Σ∣ 不会超过 2626。在对 \textit{time}time 的更新进行优化后，每一次遍历中我们都可以安排一个任务，因此会进行 |\textit{tasks}|∣tasks∣ 次遍历，每次遍历的时间复杂度为 O(|\Sigma|)O(∣Σ∣)，相乘即可得到总时间复杂度。

空间复杂度：O(|\Sigma|)O(∣Σ∣)。我们需要使用哈希表统计每种任务出现的次数，以及使用数组 \textit{nextValid}nextValid 和 \textit{test}test 帮助我们进行遍历得到结果，这些数据结构的空间复杂度均为 O(|\Sigma|)O(∣Σ∣)。

方法二：构造
思路与算法

我们首先考虑所有任务种类中执行次数最多的那一种，记它为 \texttt{A}A，的执行次数为 \textit{maxExec}maxExec。

我们使用一个宽为 n+1n+1 的矩阵可视化地展现执行 \texttt{A}A 的时间点。其中任务以行优先的顺序执行，没有任务的格子对应 CPU 的待命状态。由于冷却时间为 nn，因此我们将所有的 \texttt{A}A 排布在矩阵的第一列，可以保证满足题目要求，并且容易看出这是可以使得总时间最小的排布方法，对应的总时间为：

(\textit{maxExec} - 1)(n + 1) + 1
(maxExec−1)(n+1)+1

同理，如果还有其它也需要执行 \textit{maxExec}maxExec 次的任务，我们也需要将它们依次排布成列。例如，当还有任务 \texttt{B}B 和 \texttt{C}C 时，我们需要将它们排布在矩阵的第二、三列。



如果需要执行 \textit{maxExec}maxExec 次的任务的数量为 \textit{maxCount}maxCount，那么类似地可以得到对应的总时间为：

(\textit{maxExec} - 1)(n + 1) + \textit{maxCount}
(maxExec−1)(n+1)+maxCount

读者可能会对这个总时间产生疑问：如果 \textit{maxCount} > n+1maxCount>n+1，那么多出的任务会无法排布进矩阵的某一列中，上面计算总时间的方法就不对了。我们把这个疑问放在这里，先「假设」一定有 \textit{maxCount} \leq n+1maxCount≤n+1。

处理完执行次数为 \textit{maxExec}maxExec 次的任务，剩余任务的执行次数一定都小于 \textit{maxExec}maxExec，那么我们应当如何将它们放入矩阵中呢？一种构造的方法是，我们从倒数第二行开始，按照反向列优先的顺序（即先放入靠左侧的列，同一列中先放入下方的行），依次放入每一种任务，并且同一种任务需要连续地填入。例如还有任务 \texttt{D}D，\texttt{E}E 和 \texttt{F}F 时，我们会按照下图的方式依次放入这些任务。



对于任意一种任务而言，一定不会被放入同一行两次（否则说明该任务的执行次数大于等于 \textit{maxExec}maxExec），并且由于我们是按照列优先的顺序放入这些任务，因此任意两个相邻的任务之间要么间隔 nn（例如上图中位于同一列的相同任务），要么间隔 n+1n+1（例如上图中第一列和第二列的 \texttt{F}F），都是满足题目要求的。因此如果我们按照这样的方法填入所有的任务，那么就可以保证总时间不变，仍然为：

(\textit{maxExec} - 1)(n + 1) + \textit{maxCount}
(maxExec−1)(n+1)+maxCount

当然，这些都建立在我们的「假设」之上，即我们不会填「超出」n+1n+1 列。但读者可以想一想，如果我们真的填「超出」了 n+1n+1 列，会发生什么呢？



上图给出了一个例子，此时 n+1=5n+1=5 但我们填了 77 列。标记为 \texttt{X}X 的格子表示 CPU 的待命状态。看上去我们需要 (5-1) \times 7 + 4 = 32(5−1)×7+4=32 的时间来执行所有任务，但实际上如果我们填「超出」了 n+1n+1 列，那么所有的 CPU 待命状态都是可以省去的。这是因为 CPU 待命状态本身只是为了规定任意两个相邻任务的执行间隔至少为 nn，但如果列数超过了 n+1n+1，那么就算没有这些待命状态，任意两个相邻任务的执行间隔肯定也会至少为 nn。此时，总执行时间就是任务的总数 |\textit{task}|∣task∣。

同时我们可以发现：

如果我们没有填「超出」了 n+1n+1 列，那么图中存在 00 个或多个位置没有放入任务，由于位置数量为 (\textit{maxExec} - 1)(n + 1) + \textit{maxCount}(maxExec−1)(n+1)+maxCount，因此有：

|\textit{task}| < (\textit{maxExec} - 1)(n + 1) + \textit{maxCount}
∣task∣<(maxExec−1)(n+1)+maxCount

如果我们填「超出」了 n+1n+1 列，那么同理有：

|\textit{task}| > (\textit{maxExec} - 1)(n + 1) + \textit{maxCount}
∣task∣>(maxExec−1)(n+1)+maxCount

因此，在任意的情况下，需要的最少时间就是 (\textit{maxExec} - 1)(n + 1) + \textit{maxCount}(maxExec−1)(n+1)+maxCount 和 |\textit{task}|∣task∣ 中的较大值。

代码

C++JavaPython3JavaScriptGolangC

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = collections.Counter(tasks)

        # 最多的执行次数
        maxExec = max(freq.values())
        # 具有最多执行次数的任务数量
        maxCount = sum(1 for v in freq.values() if v == maxExec)

        return max((maxExec - 1) * (n + 1) + maxCount, len(tasks))
复杂度分析

时间复杂度：O(|\textit{task}| + |\Sigma|)O(∣task∣+∣Σ∣)，其中 |\Sigma|∣Σ∣ 是数组 \textit{task}task 中出现任务的种类，在本题中任务用大写字母表示，因此 |\Sigma|∣Σ∣ 不会超过 2626。

空间复杂度：O(|\Sigma|)O(∣Σ∣)。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/task-scheduler/solution/ren-wu-diao-du-qi-by-leetcode-solution-ur9w/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
