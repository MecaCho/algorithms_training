




'''
126. 单词接龙 II
给定两个单词（beginWord 和 endWord）和一个字典 wordList，找出所有从 beginWord 到 endWord 的最短转换序列。转换需遵循如下规则：

每次转换只能改变一个字母。
转换过程中的中间单词必须是字典中的单词。
说明:

如果不存在这样的转换序列，返回一个空列表。
所有单词具有相同的长度。
所有单词只由小写字母组成。
字典中不存在重复的单词。
你可以假设 beginWord 和 endWord 是非空的，且二者不相同。
示例 1:

输入:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

输出:
[
  ["hit","hot","dot","dog","cog"],
  ["hit","hot","lot","log","cog"]
]
示例 2:

输入:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

输出: []

解释: endWord "cog" 不在字典中，所以不存在符合要求的转换序列。

126. Word Ladder II
Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation sequence(s) from beginWord to endWord, such that:

Only one letter can be changed at a time
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
Note:

Return an empty list if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output:
[
  ["hit","hot","dot","dog","cog"],
  ["hit","hot","lot","log","cog"]
]
Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: []

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
'''


class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """

        if endWord not in wordList:
            return []
        word_grah = collections.defaultdict(list)
        length = len(beginWord)

        for word in wordList:
            for i in range(length):
                word_grah[word[:i] + "*" + word[i + 1:]].append(word)

        # print(word_grah)

        tmp = [(beginWord, [beginWord], 1)]

        visited = {beginWord: 1}

        self.res = [[beginWord]]

        level_length = 0
        res = []
        while tmp:
            # print(tmp)

            new_tmp = []
            visited_ = copy.deepcopy(visited)
            for i in range(len(tmp)):
                cur_word, sum_word, level = tmp.pop(0)
                # print(sum_word)
                for i in range(length):
                    new_word = cur_word[:i] + "*" + cur_word[i + 1:]
                    if new_word not in word_grah:
                        continue

                    if endWord in word_grah[new_word]:
                        if level_length == 0:
                            level_length = level + 1
                        if len(sum_word) == level_length - 1:
                            res.append(sum_word + [endWord])
                        continue
                    # print(sum_word, new_word, word_grah[new_word])
                    for w in word_grah[new_word]:
                        if w not in visited:
                            visited_[w] = True
                            new_sum_word = sum_word + [w]
                            new_tmp.append((w, new_sum_word, level + 1))
            visited = visited_
            tmp = new_tmp

        return res


# solutions

'''
方法一：广度优先搜索
思路

本题要求的是最短转换序列，看到最短首先想到的就是 BFS。想到 BFS 自然而然的就能想到图，但是本题并没有直截了当的给出图的模型，因此我们需要把它抽象成图的模型。

我们可以把每个单词都抽象为一个点，如果两个单词可以只改变一个字母进行转换，那么说明他们之间有一条双向边。因此我们只需要把满足转换条件的点相连，就形成了一张图。根据示例 1 中的输入，我们可以建出下图：



基于该图，我们以 hit 为图的起点， 以cog 为终点进行广度优先搜索（BFS），寻找 hit 到 cog 的最短路径。下图即为答案中的一条路径。



最大的难点解决了，我们再考虑其他要求。本题要求输出所有的最短路径。那么我们在到达某个点的时候需要把它前面经过的点一起记录下来放到一起，当到达终点的时候一起输出到结果中。

算法

基于上面的思路我们考虑如何编程实现。

方便起见，我们先给每一个单词标号，即给每个单词分配一个 id。创建一个由单词 word到 id 对应的映射 wordId，并将 beginWord 与 wordList 中所有的单词都加入这个映射中。之后我们检查 endWord 是否在该映射内，若不存在，则输入无解。我们可以使用哈希表实现上面的映射关系。

同理我们可以创建一个由对应 id 到 word 的映射 idWord，方便最后输出结果。由于 id 实际上是整数且连续，所以这个映射用数组实现即可。

接下来我们将 idWord 中的单词两两匹配，检查它们是否可以通过改变一个字母进行互相转换。如果可以，则在这两个点之间建一条双向边。

为了保留相同长度的多条路径，我们采用 cost 数组，其中 cost[i] 表示 beginWord 对应的点到第 i 个点的代价（即转换次数）。初始情况下其所有元素初始化为无穷大。

接下来将起点加入队列开始广度优先搜索，队列的每一个节点中保存从起点开始的所有路径。

对于每次取出的节点 now，每个节点都是一个数组，数组中的最后一个元素为当前路径的最后节点 last :

若该节点为终点，则将其路径转换为对应的单词存入答案;
若该节点不为终点，则遍历和它连通的节点（假设为 to ）中满足 cost[to] >= cost[now] + 1cost[to]>=cost[now]+1 的加入队列，并更新 cost[to] = cost[now] + 1cost[to]=cost[now]+1。如果 cost[to] < cost[now] + 1cost[to]<cost[now]+1，说明这个节点已经被访问过，不需要再考虑。
代码

JavaC++Golang

func findLadders(beginWord string, endWord string, wordList []string) [][]string {
    ids := map[string]int{}
    for i, word := range wordList {
        ids[word] = i
    }
    if _, ok := ids[beginWord]; !ok {
        wordList = append(wordList, beginWord)
        ids[beginWord] = len(wordList) - 1
    }
    if _, ok := ids[endWord]; !ok {
        return [][]string{}
    }

    n := len(wordList)
    edges := make([][]int, len(wordList))
    for i := 0; i < n; i++ {
        for j := i + 1; j < n; j++ {
            if transformCheck(wordList[i], wordList[j]) {
                edges[i] = append(edges[i], j)
                edges[j] = append(edges[j], i)
            }
        }
    }
    res := [][]string{}
    cost := make([]int, n)
    queue := [][]int{[]int{ids[beginWord]}}

    for i := 0; i < n; i++ {
        cost[i] = math.MaxInt32
    }
    cost[ids[beginWord]] = 0

    for i := 0; i < len(queue); i++ {
        now := queue[i]
        last := now[len(now) - 1]
        if last == ids[endWord] {
            tmp := []string{}
            for _, index := range now {
                tmp = append(tmp, wordList[index])
            }
            res = append(res, tmp)
        } else {
            for _, to := range edges[last] {
                if cost[last] + 1 <= cost[to] {
                    cost[to] = cost[last] + 1
                    tmp := make([]int, len(now))
                    copy(tmp, now)
                    tmp = append(tmp, to)
                    queue = append(queue, tmp)
                }
            }
        }
    }
    return res
}

func transformCheck(from, to string) bool {
	for i := 0; i < len(from); i++ {
		if from[i] != to[i] {
			return from[i + 1:] == to[i + 1:]
		}
	}
	return false
}
复杂度分析

时间复杂度：O(N^2*C)O(N 
2
 ∗C)。其中 NN 为 wordList 的长度，CC 为列表中单词的长度。构建映射关系的时间复杂度为 O(N)O(N)。建图首先两层遍历 wordList，复杂度为 O(N^2)O(N 
2
 )，里面比较两个单词是否可以转换的时间复杂度为 O(C)O(C)，总的时间复杂度为 O(N^2*C)O(N 
2
 ∗C)。广度优先搜索的时间复杂度最坏情况下是 O(N^2)O(N 
2
 )，因此总时间复杂度为 O(N^2*C)O(N 
2
 ∗C)。

空间复杂度：O(N^2)O(N 
2
 )。其中 NN 为 wordList 的大小。数组和哈希表的复杂度都为 O(N)O(N)，图 edges 的复杂度最坏为 O(N^2)O(N 
2
 )。广度优先搜索队列的复杂度最坏情况下，即每两个路径都有很多重叠的节点时，也是 O(N^2)O(N 
2
 )，因此总的空间复杂度为 O(N^2)O(N 
2
 )。

拓展

由于本题起点和终点固定，所以可以从起点和终点同时开始进行双向广度优先搜索，可以进一步降低时间复杂度。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/word-ladder-ii/solution/dan-ci-jie-long-ii-by-leetcode-solution/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''