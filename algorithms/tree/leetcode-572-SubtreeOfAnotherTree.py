#eencoding=utf8
'''
572. 另一个树的子树
给定两个非空二叉树 s 和 t，检验 s 中是否包含和 t 具有相同结构和节点值的子树。s 的一个子树包括 s 的一个节点和这个节点的所有子孙。s 也可以看做它自身的一棵子树。

示例 1:
给定的树 s:

     3
    / \
   4   5
  / \
 1   2
给定的树 t：

   4
  / \
 1   2
返回 true，因为 t 与 s 的一个子树拥有相同的结构和节点值。

示例 2:
给定的树 s：

     3
    / \
   4   5
  / \
 1   2
    /
   0
给定的树 t：

   4
  / \
 1   2
返回 false。

572. Subtree of Another Tree
Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.

Example 1:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
Given tree t:
   4
  / \
 1   2
Return true, because t has the same structure and node values with a subtree of s.
Example 2:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
    /
   0
Given tree t:
   4
  / \
 1   2
Return false.
'''



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None



class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        # self.res = False
        # def dfs(root, t):
        #     if not root and not t:
        #         return True
        #     elif not root or not t:
        #         return False
        #     else:
        #         return root.val == t.val and dfs(root.left, t.left) and dfs(root.right, t.right)
        #         # else:
        #         #     return dfs(root.left, t) or dfs(root.right, t)
        # if not s:
        #     return False
        # return dfs(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

        def traversal(root, res=None):
            if not root:
                return res

            res.append(root.val)
            traversal(root.left, res)
            traversal(root.right, res)
            return res
        s_list = traversal(s, [])
        t_list = traversal(t, [])
        print(s_list, t_list)
        # return t_list in s_list

# tips

'''
Which approach is better here- recursive or iterative?
If recursive approach is better, can you write recursive function with its parameters?

Two trees s and t are said to be identical if their root values are same and their left and right subtrees are identical. Can you write this in form of recursive formulae?

Recursive formulae can be: isIdentical(s,t)= s.val==t.val AND isIdentical(s.left,t.left) AND isIdentical(s.right,t.right)
'''

'''
方法一：DFS 暴力匹配
思路和算法

这是一种最朴素的方法 —— DFS 枚举 ss 中的每一个节点，判断这个点的子树是否和 tt 相等。如何判断一个节点的子树是否和 tt 相等呢，我们又需要做一次 DFS 来检查，即让两个指针一开始先指向该节点和 tt 的根，然后「同步移动」两根指针来「同步遍历」这两棵树，判断对应位置是否相等。


1 / 6

C++Golang
func isSubtree(s *TreeNode, t *TreeNode) bool {
    if s == nil {
        return false
    }
    return check(s, t) || isSubtree(s.Left, t) || isSubtree(s.Right, t)
}

func check(a, b *TreeNode) bool {
    if a == nil && b == nil {
        return true
    }
    if a == nil || b == nil {
        return false
    }
    if a.Val == b.Val {
        return check(a.Left, b.Left) && check(a.Right, b.Right)
    }
    return false
}
复杂度分析

时间复杂度：对于每一个 ss 上的点，都需要做一次 DFS 来和 tt 匹配，匹配一次的时间代价是 O(|t|)O(∣t∣)，那么总的时间代价就是 O(|s| \times |t|)O(∣s∣×∣t∣)。故渐进时间复杂度为 O(|s| \times |t|)O(∣s∣×∣t∣)。
空间复杂度：假设 ss 深度为 d_sd 
s
​	
 ，tt 的深度为 d_td 
t
​	
 ，任意时刻栈空间的最大使用代价是 O(\max \{ d_s, d_t \})O(max{d 
s
​	
 ,d 
t
​	
 })。故渐进空间复杂度为 O(\max \{ d_s, d_t \})O(max{d 
s
​	
 ,d 
t
​	
 })。
方法二：DFS 序列上做串匹配
思路和算法

这个方法需要我们先了解一个「小套路」：一棵子树上的点在 DFS 序列（即先序遍历）中是连续的。了解了这个「小套路」之后，我们可以确定解决这个问题的方向就是：把 ss 和 tt 先转换成 DFS 序，然后看 tt 的 DFS 序是否是 ss 的 DFS 序的「子串」。

这样做正确吗？ 假设 ss 由两个点组成，11 是根，22 是 11 的左孩子；tt 也由两个点组成，11 是根，22 是 11 的右孩子。这样一来 ss 和 tt 的 DFS 序相同，可是 tt 并不是 ss 的某一棵子树。由此可见「ss 的 DFS 序包含 tt 的 DFS 序」是「tt 是 ss 子树」的 必要不充分条件，所以单纯这样做是不正确的。

为了解决这个问题，我们可以引入两个空值 lNull 和 rNull，当一个节点的左孩子或者右孩子为空的时候，就插入这两个空值，这样 DFS 序列就唯一对应一棵树。处理完之后，就可以通过判断 「ss 的 DFS 序包含 tt 的 DFS 序」来判断答案。



在判断「ss 的 DFS 序包含 tt 的 DFS 序」的时候，可以暴力匹配，也可以使用 KMP 或者 Rabin-Karp 算法，在使用 Rabin-Karp 算法的时候，要注意串中可能有负值。

这里给出用 KMP 判断的代码实现。

C++Golang
func isSubtree(s *TreeNode, t *TreeNode) bool {
    maxEle := math.MinInt32
    getMaxElement(s, &maxEle)
    getMaxElement(t, &maxEle)
    lNull := maxEle + 1;
    rNull := maxEle + 2;

    sl, tl := getDfsOrder(s, []int{}, lNull, rNull), getDfsOrder(t, []int{}, lNull, rNull)
    return kmp(sl, tl)
}

func kmp(s, t []int) bool {
    sLen, tLen := len(s), len(t)
    fail := make([]int, sLen)
    for i := 0; i < sLen; i++ {
        fail[i] = -1
    }
    for i, j := 1, -1; i < tLen; i++ {
        for j != -1 && t[i] != t[j+1] {
            j = fail[j]
        }
        if t[i] == t[j+1] {
            j++
        }
        fail[i] = j
    }

    for i, j := 0, -1; i < sLen; i++ {
        for j != -1 && s[i] != t[j+1] {
            j = fail[j]
        }
        if s[i] == t[j+1] {
            j++
        }
        if j == tLen - 1 {
            return true
        }
    }
    return false
}

func getDfsOrder(t *TreeNode, list []int, lNull, rNull int) []int {
    if t == nil {
        return list
    }
    list = append(list, t.Val)
    if t.Left != nil {
        list = getDfsOrder(t.Left, list, lNull, rNull)
    } else {
        list = append(list, lNull)
    }

    if t.Right != nil {
        list = getDfsOrder(t.Right, list, lNull, rNull)
    } else {
        list = append(list, rNull)
    }
    return list
} 

func getMaxElement(t *TreeNode, maxEle *int) {
    if t == nil {
        return
    }
    if t.Val > *maxEle {
        *maxEle = t.Val
    }
    getMaxElement(t.Left, maxEle)
    getMaxElement(t.Right, maxEle)
}
复杂度分析

时间复杂度：遍历两棵树得到 DFS 序列的时间代价是 O(|s| + |t|)O(∣s∣+∣t∣)，在匹配的时候，如果使用暴力匹配，时间代价为 O(|s| \times |t|)O(∣s∣×∣t∣)，使用 KMP 或 Rabin-Karp 进行串匹配的时间代价都是 O(|s| + |t|)O(∣s∣+∣t∣)。由于这里的代码使用 KMP 实现的，所以渐进时间复杂度为 O(|s| + |t|)O(∣s∣+∣t∣)。
空间复杂度：这里保存了两个 DFS 序列，还计算了 |t|∣t∣ 长度的 fail 数组，辅助空间的总代价为 O(|s| + |t|)O(∣s∣+∣t∣)，任意时刻栈空间的最大使用代价是 O(\max \{ d_s, d_t \})O(max{d 
s
​	
 ,d 
t
​	
 })，由于 $ \max { d_s, d_t } = O(|s| + |t|) $，故渐进空间复杂度为 O(|s| + |t|)O(∣s∣+∣t∣)。
方法三：树哈希
思路和算法

考虑把每个子树都映射成一个唯一的数，如果 tt 对应的数字和 ss 中任意一个子树映射的数字相等，则 tt 是 ss 的某一棵子树。如何映射呢？我们可以定义这样的哈希函数：

f_o = v_o + 31 \cdot f_l \cdot p(s_l) + 179 \cdot f_r \cdot p(s_r)
f 
o
​	
 =v 
o
​	
 +31⋅f 
l
​	
 ⋅p(s 
l
​	
 )+179⋅f 
r
​	
 ⋅p(s 
r
​	
 )

这里 f_xf 
x
​	
  表示节点 xx 的哈希值，s_xs 
x
​	
  表示节点 xx 对应的子树大小，v_xv 
x
​	
  代表节点 xx 的 val，p(n)p(n) 表示第 nn 个素数，oo 表示当前节点，ll 和 rr 分别表示左右孩子。这个式子的意思是：当前节点 oo 的哈希值等于这个点的 val 加上 3131 倍左子树的哈希值乘以第 s_ls 
l
​	
  个素数，再加上 179179 倍右子树的哈希值乘以第 s_rs 
r
​	
  个素数。这里的 3131 和 179179 这两个数字只是为了区分左右子树，你可以自己选择你喜欢的权值。

这样做为什么可行呢？ 回到我们的初衷，我们希望把每个子树都映射成一个唯一的数，这样真的能够确保唯一吗？实际上未必。但是我们在这个哈希函数中考虑到每个点的 val、子树哈希值、子树大小以及左右子树的不同权值，所以这些因素共同影响一个点的哈希值，所以出现冲突的几率较小，一般我们可以忽略。当然你也可以设计你自己的哈希函数，只要考虑到这些因素，就可以把冲突的可能性设计得比较小。可是如果还是出现了冲突怎么办呢？ 我们可以设计两个哈希函数 f_1f 
1
​	
  和 f_2f 
2
​	
 ，用这两个哈希函数生成第三个哈希函数，比如 f = f_1 + f_2f=f 
1
​	
 +f 
2
​	
 、f = f_1 \times f_2f=f 
1
​	
 ×f 
2
​	
  等等，这样可以进一步缩小冲突，如果 f_1f 
1
​	
  的冲突概率是 P_1P 
1
​	
 ，f_2f 
2
​	
  的冲突概率是 P_2P 
2
​	
 ，那么 ff 的冲突概率就是 P_1 \times P_2P 
1
​	
 ×P 
2
​	
 ，理论上已经非常小了，这就是「双哈希」。当然，为了减少冲突，你也可以设计「三哈希」、「四哈希」等，可是这样编程的复杂度就会增加。实际上，一般情况下，只要运气不是太差，一个哈希函数就足够了。

我们可以用「埃氏筛法」或者「欧拉筛法」求出前 \arg \pi (\max \{ |s|, |t| \})argπ(max{∣s∣,∣t∣}) 个素数（其中 \pi (x)π(x) 表示 xx 以内素数个数，\arg \pi (x)argπ(x) 为它的反函数，表示有多少以内包含 xx 个素数，这个映射是不唯一的，我们取最小值），然后 DFS 计算哈希值，最后比较 ss 的所有子树是否有和 tt 相同的哈希值即可。

C++
class Solution {
public:
    static constexpr int MAX_N = 1000 + 5;
    static constexpr int MOD = int(1E9) + 7;

    bool vis[MAX_N];
    int p[MAX_N], tot;
    void getPrime() {
        vis[0] = vis[1] = 1; tot = 0;
        for (int i = 2; i < MAX_N; ++i) {
            if (!vis[i]) p[++tot] = i;
            for (int j = 1; j <= tot && i * p[j] < MAX_N; ++j) {
                vis[i * p[j]] = 1;
                if (i % p[j] == 0) break;
            }
        }
    }

    struct Status {
        int f, s; // f 为哈希值 | s 为子树大小
        Status(int f_ = 0, int s_ = 0) 
            : f(f_), s(s_) {}
    };

    unordered_map <TreeNode *, Status> hS, hT;

    void dfs(TreeNode *o, unordered_map <TreeNode *, Status> &h) {
        h[o] = Status(o->val, 1);
        if (!o->left && !o->right) return;
        if (o->left) {
            dfs(o->left, h);
            h[o].s += h[o->left].s;
            h[o].f = (h[o].f + (31LL * h[o->left].f * p[h[o->left].s]) % MOD) % MOD;
        }
        if (o->right) {
            dfs(o->right, h);
            h[o].s += h[o->right].s;
            h[o].f = (h[o].f + (179LL * h[o->right].f * p[h[o->right].s]) % MOD) % MOD;
        }
    }

    bool isSubtree(TreeNode* s, TreeNode* t) {
        getPrime();
        dfs(s, hS);
        dfs(t, hT);

        int tHash = hT[t].f;
        for (const auto &[k, v]: hS) {
            if (v.f == tHash) {
                return true;
            }
        } 

        return false;
    }
};
复杂度分析

时间复杂度：筛选素数（此处为欧拉筛）的时间代价是 O(\arg \pi (\max \{ |s|, |t| \}))O(argπ(max{∣s∣,∣t∣}))，对于 10^610 
6
  以下的 xx，一般有 \arg \pi (x) < 15 xargπ(x)<15x，也就是在 15 x15x 个自然数里一定能找到 xx 个素数，所以这里可以认为它比线性稍微慢一点。DFS 求解和循环比较的时间代价是 O(|s| + |t|)O(∣s∣+∣t∣)。故渐进时间复杂度为 O(\arg \pi (\max \{ |s|, |t| \}) + |s| + |t|) = O(\arg \pi (\max \{ |s|, |t| \}))O(argπ(max{∣s∣,∣t∣})+∣s∣+∣t∣)=O(argπ(max{∣s∣,∣t∣}))。
空间复杂度：这里用了哈希表来记录每个点的哈希值和子树大小，空间代价是 O(|s| + |t|)O(∣s∣+∣t∣)，筛选素数的 vis 数组的空间代价为 O(\arg \pi (\max \{ |s|, |t| \}))O(argπ(max{∣s∣,∣t∣}))，任意时刻栈空间的最大使用代价是 O(\max \{ d_s, d_t \})O(max{d 
s
​	
 ,d 
t
​	
 })，故渐进空间复杂度为 O(\arg \pi (\max \{ |s|, |t| \}))O(argπ(max{∣s∣,∣t∣}))。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/subtree-of-another-tree/solution/ling-yi-ge-shu-de-zi-shu-by-leetcode-solution/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''



'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

            self.res = False
                    def dfs(root, t):
                                if not root and not t:
                                                return True
                                                            elif not root or not t:
                                                                            return False
                                                                                        else:
                                                                                                        return root.val == t.val and dfs(root.left, t.left) and dfs(root.right, t.right)
                                                                                                                        # else:
                                                                                                                                        #     return dfs(root.left, t) or dfs(root.right, t)
                                                                                                                                                if not root:
                                                                                                                                                            return False
                                                                                                                                                                    return dfs(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
                                                                                                                                                                ''''
