# encoding=utf8

'''
423. Reconstruct Original Digits from English
Given a string s containing an out-of-order English representation of digits 0-9, return the digits in ascending order.

 

Example 1:

Input: s = "owoztneoer"
Output: "012"
Example 2:

Input: s = "fviefuro"
Output: "45"
 

Constraints:

1 <= s.length <= 105
s[i] is one of the characters ["e","g","f","i","h","o","n","s","r","u","t","w","v","x","z"].
s is guaranteed to be valid.
'''

class Solution(object):
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        cnt = Counter(s)
        nums = [0]*10
        nums[0] = cnt["z"]
        nums[2] = cnt["w"]
        nums[4] = cnt['u']
        nums[6] = cnt['x']
        nums[8] = cnt['g']

        nums[3] = cnt["h"] - nums[8]
        nums[5] = cnt["f"] - nums[4]
        nums[7] = cnt["s"] - nums[6]

        nums[1] = cnt["o"] - nums[0] - nums[2] - nums[4]
        nums[9] = cnt["i"] - nums[5] - nums[6] - nums[8]

        res = ""
        for i in range(10):
            for j in range(nums[i]):
                res += str(i)
        return res


      
