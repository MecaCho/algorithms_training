# encoding=utf8

'''
421. Maximum XOR of Two Numbers in an Array

Given an integer array nums, return the maximum result of nums[i] XOR nums[j], where 0 ≤ i ≤ j < n.

Follow up: Could you do this in O(n) runtime?

 

Example 1:

Input: nums = [3,10,5,25,2,8]
Output: 28
Explanation: The maximum result is 5 XOR 25 = 28.
Example 2:

Input: nums = [0]
Output: 0
Example 3:

Input: nums = [2,4]
Output: 6
Example 4:

Input: nums = [8,10,2]
Output: 10
Example 5:

Input: nums = [14,70,53,83,49,91,36,80,92,51,66,70]
Output: 127
 

Constraints:

1 <= nums.length <= 2 * 104
0 <= nums[i] <= 231 - 1

421. 数组中两个数的最大异或值

给你一个整数数组 nums ，返回 nums[i] XOR nums[j] 的最大运算结果，其中 0 ≤ i ≤ j < n 。

进阶：你可以在 O(n) 的时间解决这个问题吗？

 

示例 1：

输入：nums = [3,10,5,25,2,8]
输出：28
解释：最大运算结果是 5 XOR 25 = 28.
示例 2：

输入：nums = [0]
输出：0
示例 3：

输入：nums = [2,4]
输出：6
示例 4：

输入：nums = [8,10,2]
输出：10
示例 5：

输入：nums = [14,70,53,83,49,91,36,80,92,51,66,70]
输出：127
 

提示：

1 <= nums.length <= 2 * 104
0 <= nums[i] <= 231 - 1
'''

class Trie(object):
    def __init__(self):
        # 左子树指向表示 0 的子节点
        self.left = None
        # 右子树指向表示 1 的子节点
        self.right = None

class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 字典树的根节点
        root = Trie()
        # 最高位的二进制位编号为 30
        HIGH_BIT = 30

        def add(num):
            cur = root
            for k in range(HIGH_BIT, -1, -1):
                bit = (num >> k) & 1
                if bit == 0:
                    if not cur.left:
                        cur.left = Trie()
                    cur = cur.left
                else:
                    if not cur.right:
                        cur.right = Trie()
                    cur = cur.right

        def check(num):
            cur = root
            x = 0
            for k in range(HIGH_BIT, -1, -1):
                bit = (num >> k) & 1
                if bit == 0:
                    # a_i 的第 k 个二进制位为 0，应当往表示 1 的子节点 right 走
                    if cur.right:
                        cur = cur.right
                        x = x * 2 + 1
                    else:
                        cur = cur.left
                        x = x * 2
                else:
                    # a_i 的第 k 个二进制位为 1，应当往表示 0 的子节点 left 走
                    if cur.left:
                        cur = cur.left
                        x = x * 2 + 1
                    else:
                        cur = cur.right
                        x = x * 2
            return x

        n = len(nums)
        x = 0
        for i in range(1, n):
            add(nums[i - 1])
            # 将 nums[i] 看作 ai，找出最大的 x 更新答案
            x = max(x, check(nums[i]))

        return x

# golang solution

'''
func findMaximumXOR(nums []int) int {

    var res int

	for i := 0; i < len(nums); i++ {
		for j := i + 1; j < len(nums); j++ {
			tmp := nums[i] ^ nums[j]
			if tmp > res {
				res = nums[i] ^ nums[j]
			}
		}
	}

	return res
}
'''

# solutions

'''
前言
假设我们在数组中选择了元素 a_ia 
i
​	
  和 a_ja 
j
​	
 （i \neq ji 

​	
 =j），使得它们达到最大的按位异或运算结果 xx：

x = a_i \oplus a_j
x=a 
i
​	
 ⊕a 
j
​	
 

其中 \oplus⊕ 表示按位异或运算。要想求出 xx，一种简单的方法是使用二重循环枚举 ii 和 jj，但这样做的时间复杂度为 O(n^2)O(n 
2
 )，会超出时间限制。因此，我们需要寻求时间复杂度更低的做法。

根据按位异或运算的性质，x = a_i \oplus a_jx=a 
i
​	
 ⊕a 
j
​	
  等价于 a_j = x \oplus a_ia 
j
​	
 =x⊕a 
i
​	
 。我们可以根据这一变换，设计一种「从高位到低位依次确定 xx 二进制表示的每一位」的方法，以此得到 xx 的值。该方法的精髓在于：

由于数组中的元素都在 [0, 2^{31})[0,2 
31
 ) 的范围内，那么我们可以将每一个数表示为一个长度为 3131 位的二进制数（如果不满 3131 位，在最高位之前补上若干个前导 00 即可）；

这 3131 个二进制位从低位到高位依次编号为 0, 1, \cdots, 300,1,⋯,30。我们从最高位第 3030 个二进制位开始，依次确定 xx 的每一位是 00 还是 11；

由于我们需要找出最大的 xx，因此在枚举每一位时，我们先判断 xx 的这一位是否能取到 11。如果能，我们取这一位为 11，否则我们取这一位为 00。

「判断 xx 的某一位是否能取到 11」这一步骤并不容易。下面介绍两种判断的方法。

方法一：哈希表
思路与算法

假设我们已经确定了 xx 最高的若干个二进制位，当前正在确定第 kk 个二进制位。根据「前言」部分的分析，我们希望第 kk 个二进制位能够取到 11。

我们用 \textit{pre}^k(x)pre 
k
 (x) 表示 xx 从最高位第 3030 个二进制位开始，到第 kk 个二进制位为止的数，那么 a_j = x \oplus a_ia 
j
​	
 =x⊕a 
i
​	
  蕴含着：

\textit{pre}^k (a_j) = \textit{pre}^k (x) \oplus \textit{pre}^k (a_i)
pre 
k
 (a 
j
​	
 )=pre 
k
 (x)⊕pre 
k
 (a 
i
​	
 )

由于 \textit{pre}^k(x)pre 
k
 (x) 对于我们来说是已知的，因此我们将所有的 \textit{pre}^k (a_j)pre 
k
 (a 
j
​	
 ) 放入哈希表中，随后枚举 ii 并计算 \textit{pre}^k (x) \oplus \textit{pre}^k (a_i)pre 
k
 (x)⊕pre 
k
 (a 
i
​	
 )。如果其出现在哈希表中，那么说明第 kk 个二进制位能够取到 11，否则第 kk 个二进制位只能为 00。

本方法若仅阅读文字，理解起来可能较为困难，读者可以参考下面的代码以及注释。

细节

计算 \textit{pre}^k(x)pre 
k
 (x) 可以使用右移运算 \texttt{>>}>>。

代码

C++JavaC#Python3JavaScriptGolangC

func findMaximumXOR(nums []int) (x int) {
    const highBit = 30 // 最高位的二进制位编号为 30
    for k := highBit; k >= 0; k-- {
        // 将所有的 pre^k(a_j) 放入哈希表中
        seen := map[int]bool{}
        for _, num := range nums {
            // 如果只想保留从最高位开始到第 k 个二进制位为止的部分
            // 只需将其右移 k 位
            seen[num>>k] = true
        }

        // 目前 x 包含从最高位开始到第 k+1 个二进制位为止的部分
        // 我们将 x 的第 k 个二进制位置为 1，即为 x = x*2+1
        xNext := x*2 + 1
        found := false

        // 枚举 i
        for _, num := range nums {
            if seen[num>>k^xNext] {
                found = true
                break
            }
        }

        if found {
            x = xNext
        } else {
            // 如果没有找到满足等式的 a_i 和 a_j，那么 x 的第 k 个二进制位只能为 0
            // 即为 x = x*2
            x = xNext - 1
        }
    }
    return
}
复杂度分析

时间复杂度：O(n \log C)O(nlogC)，其中 nn 是数组 \textit{nums}nums 的长度，CC 是数组中的元素范围，在本题中 C < 2^{31}C<2 
31
 。枚举答案 xx 的每一个二进制位的时间复杂度为 O(\log C)O(logC)，在每一次枚举的过程中，我们需要 O(n)O(n) 的时间进行判断，因此总时间复杂度为 O(n \log C)O(nlogC)。

空间复杂度：O(n)O(n)，即为哈希表需要使用的空间。

方法二：字典树
思路与算法

我们也可以将数组中的元素看成长度为 3131 的字符串，字符串中只包含 00 和 11。如果我们将字符串放入字典树中，那么在字典树中查询一个字符串的过程，恰好就是从高位开始确定每一个二进制位的过程。字典树的具体逻辑以及实现可以参考「208. 实现 Trie（前缀树）的官方题解」，这里我们只说明如何使用字典树解决本题。

根据 x = a_i \oplus a_jx=a 
i
​	
 ⊕a 
j
​	
 ，我们枚举 a_ia 
i
​	
 ，并将 a_0, a_1, \cdots, a_{i-1}a 
0
​	
 ,a 
1
​	
 ,⋯,a 
i−1
​	
  作为 a_ja 
j
​	
  放入字典树中，希望找出使得 xx 达到最大值的 a_ja 
j
​	
 。

如何求出 xx 呢？我们可以从字典树的根节点开始进行遍历，遍历的「参照对象」为 a_ia 
i
​	
 。在遍历的过程中，我们根据 a_ia 
i
​	
  的第 xx 个二进制位是 00 还是 11，确定我们应当走向哪个子节点以继续遍历。假设我们当前遍历到了第 kk 个二进制位：

如果 a_ia 
i
​	
  的第 kk 个二进制位为 00，那么我们应当往表示 11 的子节点走，这样 0 \oplus 1 = 10⊕1=1，可以使得 xx 的第 kk 个二进制位为 11。如果不存在表示 11 的子节点，那么我们只能往表示 00 的子节点走，xx 的第 kk 个二进制位为 00；

如果 a_ia 
i
​	
  的第 kk 个二进制位为 11，那么我们应当往表示 00 的子节点走，这样 1 \oplus 0 = 11⊕0=1，可以使得 xx 的第 kk 个二进制位为 11。如果不存在表示 00 的子节点，那么我们只能往表示 11 的子节点走，xx 的第 kk 个二进制位为 00。

当遍历完所有的 3131 个二进制位后，我们也就得到了 a_ia 
i
​	
  可以通过异或运算得到的最大 xx。这样一来，如果我们枚举了所有的 a_ia 
i
​	
 ，也就得到了最终的答案。

细节

由于字典树中的每个节点最多只有两个子节点，分别表示 00 和 11，因此本题中的字典树是一棵二叉树。在设计字典树的数据结构时，我们可以令左子节点 \textit{left}left 表示 00，右子节点 \textit{right}right 表示 11。

代码

下面的 \texttt{C++}C++ 代码没有析构字典树的空间。如果在面试中遇到了本题，可以和面试官进行沟通，询问是否需要析构对应的空间。

C++JavaC#Python3GolangC

const highBit = 30

type trie struct {
    left, right *trie
}

func (t *trie) add(num int) {
    cur := t
    for i := highBit; i >= 0; i-- {
        bit := num >> i & 1
        if bit == 0 {
            if cur.left == nil {
                cur.left = &trie{}
            }
            cur = cur.left
        } else {
            if cur.right == nil {
                cur.right = &trie{}
            }
            cur = cur.right
        }
    }
}

func (t *trie) check(num int) (x int) {
    cur := t
    for i := highBit; i >= 0; i-- {
        bit := num >> i & 1
        if bit == 0 {
            // a_i 的第 k 个二进制位为 0，应当往表示 1 的子节点 right 走
            if cur.right != nil {
                cur = cur.right
                x = x*2 + 1
            } else {
                cur = cur.left
                x = x * 2
            }
        } else {
            // a_i 的第 k 个二进制位为 1，应当往表示 0 的子节点 left 走
            if cur.left != nil {
                cur = cur.left
                x = x*2 + 1
            } else {
                cur = cur.right
                x = x * 2
            }
        }
    }
    return
}

func findMaximumXOR(nums []int) (x int) {
    root := &trie{}
    for i := 1; i < len(nums); i++ {
        // 将 nums[i-1] 放入字典树，此时 nums[0 .. i-1] 都在字典树中
        root.add(nums[i-1])
        // 将 nums[i] 看作 ai，找出最大的 x 更新答案
        x = max(x, root.check(nums[i]))
    }
    return
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}
复杂度分析

时间复杂度：O(n \log C)O(nlogC)，其中 nn 是数组 \textit{nums}nums 的长度，CC 是数组中的元素范围，在本题中 C < 2^{31}C<2 
31
 。我们需要将 a_0a 
0
​	
  到 a_{n-2}a 
n−2
​	
  加入字典树中，并且需要以 a_1a 
1
​	
  到 a_{n-1}a 
n−1
​	
  作为「参照对象」在字典树上进行遍历，每一项操作的单次时间复杂度为 O(\log C)O(logC)，因此总时间复杂度为 O(n \log C)O(nlogC)。

空间复杂度：O(n \log C)O(nlogC)。每一个元素在字典树中需要使用 O(\log C)O(logC) 的空间，因此总空间复杂度为 O(n \log C)O(nlogC)。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/maximum-xor-of-two-numbers-in-an-array/solution/shu-zu-zhong-liang-ge-shu-de-zui-da-yi-h-n9m9/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''

