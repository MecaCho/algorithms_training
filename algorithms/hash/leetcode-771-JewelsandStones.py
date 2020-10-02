'''
771. Jewels and Stones
You're given strings J representing the types of stones that are jewels, and S representing the stones you have.  Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.

The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive, so "a" is considered a different type of stone from "A".

Example 1:

Input: J = "aA", S = "aAAbbbb"
Output: 3
Example 2:

Input: J = "z", S = "ZZ"
Output: 0
Note:

S and J will consist of letters and have length at most 50.
The characters in J are distinct.

771. 宝石与石头
 给定字符串J 代表石头中宝石的类型，和字符串 S代表你拥有的石头。 S 中每个字符代表了一种你拥有的石头的类型，你想知道你拥有的石头中有多少是宝石。

J 中的字母不重复，J 和 S中的所有字符都是字母。字母区分大小写，因此"a"和"A"是不同类型的石头。

示例 1:

输入: J = "aA", S = "aAAbbbb"
输出: 3
示例 2:

输入: J = "z", S = "ZZ"
输出: 0
注意:

S 和 J 最多含有50个字母。
 J 中的字符不重复。
'''



class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        import collections
        stones = collections.Counter(S)
        return sum(stones[j] for j in J)



class Solution1(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        sum = 0
        for i in S:
            if i in J:
                sum += 1
        return sum


class Solution2(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        return len([i for i in S if i in J])


class Solution3(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        # import collections
        # stones = collections.Counter(S)
        # return sum(stones[j] for j in J)

        return sum(S.count(j) for j in J)


# solutions

'''
方法一：暴力
思路与算法

暴力法的思路很直观，遍历字符串 SS，对于 SS 中的每个字符，遍历一次字符串 JJ，如果其和 JJ 中的某一个字符相同，则是宝石。

代码

JavaPython3C++JavaScriptGolangC

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        return sum(s in J for s in S)
复杂度分析

时间复杂度：O(mn)O(mn)，其中 mm 是字符串 JJ 的长度，nn 是字符串 SS 的长度。遍历字符串 SS 的时间复杂度是 O(n)O(n)，对于 SS 中的每个字符，需要遍历字符串 JJ 判断是否是宝石，时间复杂度是 O(m)O(m)，因此总时间复杂度是 O(mn)O(mn)。

空间复杂度：O(1)O(1)。只需要维护常量的额外空间。

方法二：哈希集合
思路与算法

方法一中，对于字符串 SS 中的每个字符，都需要遍历一次字符串 JJ，导致时间复杂度较高。如果使用哈希集合存储字符串 JJ 中的宝石，则可以降低判断的时间复杂度。

遍历字符串 JJ，使用哈希集合存储其中的字符，然后遍历字符串 SS，对于其中的每个字符，如果其在哈希集合中，则是宝石。

代码

JavaPython3C++JavaScriptGolangC

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        jewelsSet = set(J)
        return sum(s in jewelsSet for s in S)
复杂度分析

时间复杂度：O(m+n)O(m+n)，其中 mm 是字符串 JJ 的长度，nn 是字符串 SS 的长度。遍历字符串 JJ 将其中的字符存储到哈希集合中，时间复杂度是 O(m)O(m)，然后遍历字符串 SS，对于 SS 中的每个字符在 O(1)O(1) 的时间内判断当前字符是否是宝石，时间复杂度是 O(n)O(n)，因此总时间复杂度是 O(m+n)O(m+n)。

空间复杂度：O(m)O(m)，其中 mm 是字符串 JJ 的长度。使用哈希集合存储字符串 JJ 中的字符。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/jewels-and-stones/solution/bao-shi-yu-shi-tou-by-leetcode-solution/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''