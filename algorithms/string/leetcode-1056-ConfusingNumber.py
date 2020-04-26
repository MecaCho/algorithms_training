
'''
1056. 易混淆数
给定一个数字 N，当它满足以下条件的时候返回 true：

原数字旋转 180° 以后可以得到新的数字。

如 0, 1, 6, 8, 9 旋转 180° 以后，得到了新的数字 0, 1, 9, 8, 6 。

2, 3, 4, 5, 7 旋转 180° 后，得到的不是数字。

易混淆数 (confusing number) 在旋转180°以后，可以得到和原来不同的数，且新数字的每一位都是有效的。



示例 1：



输入：6
输出：true
解释：
把 6 旋转 180° 以后得到 9，9 是有效数字且 9!=6 。
示例 2：



输入：89
输出：true
解释:
把 89 旋转 180° 以后得到 68，86 是有效数字且 86!=89 。
示例 3：



输入：11
输出：false
解释：
把 11 旋转 180° 以后得到 11，11 是有效数字但是值保持不变，所以 11 不是易混淆数字。
示例 4：



输入：25
输出：false
解释：
把 25 旋转 180° 以后得到的不是数字。


提示：

0 <= N <= 10^9
可以忽略掉旋转后得到的前导零，例如，如果我们旋转后得到 0008 那么该数字就是 8 。

1056. Confusing Number
Given a number N, return true if and only if it is a confusing number, which satisfies the following condition:

We can rotate digits by 180 degrees to form new digits. When 0, 1, 6, 8, 9 are rotated 180 degrees, they become 0, 1, 9, 8, 6 respectively. When 2, 3, 4, 5 and 7 are rotated 180 degrees, they become invalid. A confusing number is a number that when rotated 180 degrees becomes a different number with each digit valid.



Example 1:



Input: 6
Output: true
Explanation:
We get 9 after rotating 6, 9 is a valid number and 9!=6.
Example 2:



Input: 89
Output: true
Explanation:
We get 68 after rotating 89, 86 is a valid number and 86!=89.
Example 3:



Input: 11
Output: false
Explanation:
We get 11 after rotating 11, 11 is a valid number but the value remains the same, thus 11 is not a confusing number.
Example 4:



Input: 25
Output: false
Explanation:
We get an invalid number after rotating 25.


Note:

0 <= N <= 10^9
After the rotation we can ignore leading zeros, for example if after rotation we have 0008 then this number is considered as just 8.
'''



class Solution(object):
    def confusingNumber(self, N):
        """
        :type N: int
        :rtype: bool
        """
        N = str(N)
        hash_map = {"6": "9", "9": "6", "8": "8", "0": "0", "1": "1"}
        new_num = []
        for i in range(len(N)):
            if N[i] not in hash_map:
                return False
            else:
                new_num.append(hash_map[N[i]])
        # print(new_num, num)
        return not "".join(new_num) == N[::-1]
