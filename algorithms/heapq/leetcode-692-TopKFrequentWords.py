'''
692. 前K个高频单词
给一非空的单词列表，返回前 k 个出现次数最多的单词。

返回的答案应该按单词出现频率由高到低排序。如果不同的单词有相同出现频率，按字母顺序排序。

示例 1：

输入: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
输出: ["i", "love"]
解析: "i" 和 "love" 为出现次数最多的两个单词，均为2次。
    注意，按字母顺序 "i" 在 "love" 之前。


示例 2：

输入: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
输出: ["the", "is", "sunny", "day"]
解析: "the", "is", "sunny" 和 "day" 是出现次数最多的四个单词，
    出现次数依次为 4, 3, 2 和 1 次。


注意：

假定 k 总为有效值， 1 ≤ k ≤ 集合元素数。
输入的单词均由小写字母组成。


扩展练习：

尝试以 O(n log k) 时间复杂度和 O(n) 空间复杂度解决。

692. Top K Frequent Words
Given a non-empty list of words, return the k most frequent elements.

Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency, then the word with the lower alphabetical order comes first.

Example 1:
Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
Output: ["i", "love"]
Explanation: "i" and "love" are the two most frequent words.
    Note that "i" comes before "love" due to a lower alphabetical order.
Example 2:
Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
Output: ["the", "is", "sunny", "day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
    with the number of occurrence being 4, 3, 2 and 1 respectively.
Note:
You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Input words contain only lowercase letters.
Follow up:
Try to solve it in O(n log k) time and O(n) extra space.
'''





class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        # count = collections.Counter(words)
        # heap = [(-freq, word) for word, freq in count.items()]
        # heapq.heapify(heap)
        # return [heapq.heappop(heap)[1] for _ in xrange(k)]

        hash_map = {}
        for i in range(len(words)):
            if words[i] in hash_map:
                hash_map[words[i]] += 1
            else:
                hash_map[words[i]] = 1
        # hash_map = collections.Counter(words)
        import heapq
        l = []
        for key,v in hash_map.items():
            # heapq.heappush(l, (-v, key))
            l.append((-v, key))
        heapq.heapify(l)
        # print([item for item in heapq.nlargest(k, l)])
        # return [item[1] for item in heapq.nlargest(k, l)][::-1]
        return [item[1] for item in heapq.nsmallest(k, l)]
        # return [l[i][1] for i in range(k)]
        # return [heapq.heappop(l)[1] for i in range(k)]

        
        
# solutions

class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        counter = collections.Counter(words)
        heap = [(-freq, word) for word, freq in counter.items()]
        heapq.heapify(heap)
        return [heapq.heappop(heap)[1] for _ in xrange(k)]

'''
方法一：哈希表 + 排序
思路及算法

我们可以预处理出每一个单词出现的频率，然后依据每个单词出现的频率降序排序，最后返回前 kk 个字符串即可。

具体地，我们利用哈希表记录每一个字符串出现的频率，然后将哈希表中所有字符串进行排序，排序时，如果两个字符串出现频率相同，那么我们让两字符串中字典序较小的排在前面，否则我们让出现频率较高的排在前面。最后我们只需要保留序列中的前 kk 个字符串即可。

代码

C++JavaC#GolangJavaScriptC

func topKFrequent(words []string, k int) []string {
    cnt := map[string]int{}
    for _, w := range words {
        cnt[w]++
    }
    uniqueWords := make([]string, 0, len(cnt))
    for w := range cnt {
        uniqueWords = append(uniqueWords, w)
    }
    sort.Slice(uniqueWords, func(i, j int) bool {
        s, t := uniqueWords[i], uniqueWords[j]
        return cnt[s] > cnt[t] || cnt[s] == cnt[t] && s < t
    })
    return uniqueWords[:k]
}
复杂度分析

时间复杂度：O(l \times n + l \times m \log m)O(l×n+l×mlogm)，其中 nn 表示给定字符串序列的长度，ll 表示字符串的平均长度，mm 表示实际字符串种类数。我们需要 l \times nl×n 的时间将字符串插入到哈希表中，以及 l \times m \log ml×mlogm 的时间完成字符串比较（最坏情况下所有字符串出现频率都相同，我们需要将它们两两比较）。

空间复杂度：O(l \times m)O(l×m)，其中 ll 表示字符串的平均长度，mm 表示实际字符串种类数。哈希表和生成的排序数组空间占用均为 O(l \times m)O(l×m)。

方法二：优先队列
思路及算法

对于前 kk 大或前 kk 小这类问题，有一个通用的解法：优先队列。优先队列可以在 O(\log n)O(logn) 的时间内完成插入或删除元素的操作（其中 nn 为优先队列的大小），并可以 O(1)O(1) 地查询优先队列顶端元素。

在本题中，我们可以创建一个小根优先队列（顾名思义，就是优先队列顶端元素是最小元素的优先队列）。我们将每一个字符串插入到优先队列中，如果优先队列的大小超过了 kk，那么我们就将优先队列顶端元素弹出。这样最终优先队列中剩下的 kk 个元素就是前 kk 个出现次数最多的单词。

代码

C++JavaGolang

type pair struct {
    w string
    c int
}
type hp []pair
func (h hp) Len() int            { return len(h) }
func (h hp) Less(i, j int) bool  { a, b := h[i], h[j]; return a.c < b.c || a.c == b.c && a.w > b.w }
func (h hp) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *hp) Push(v interface{}) { *h = append(*h, v.(pair)) }
func (h *hp) Pop() interface{}   { a := *h; v := a[len(a)-1]; *h = a[:len(a)-1]; return v }

func topKFrequent(words []string, k int) []string {
    cnt := map[string]int{}
    for _, w := range words {
        cnt[w]++
    }
    h := &hp{}
    for w, c := range cnt {
        heap.Push(h, pair{w, c})
        if h.Len() > k {
            heap.Pop(h)
        }
    }
    ans := make([]string, k)
    for i := k - 1; i >= 0; i-- {
        ans[i] = heap.Pop(h).(pair).w
    }
    return ans
}
复杂度分析

时间复杂度：O(l \times n + m \times l \log k)O(l×n+m×llogk)，其中 nn 表示给定字符串序列的长度，mm 表示实际字符串种类数，ll 表示字符串的平均长度。我们需要 l \times nl×n 的时间将字符串插入到哈希表中，以及每次插入元素到优先队列中都需要 l \log kllogk 的时间，共需要插入 mm 次。

空间复杂度：O(l \times (m + k))O(l×(m+k))，其中 ll 表示字符串的平均长度，mm 表示实际字符串种类数。哈希表空间占用为 O(l \times m)O(l×m)，优先队列空间占用为 O(l \times k)O(l×k)。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/top-k-frequent-words/solution/qian-kge-gao-pin-dan-ci-by-leetcode-solu-3qk0/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
