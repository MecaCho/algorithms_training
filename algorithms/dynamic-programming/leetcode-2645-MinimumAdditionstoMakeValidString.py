# encoding=utf8

'''
2645. Minimum Additions to Make Valid String

Given a string word to which you can insert letters "a", "b" or "c" anywhere and any number of times, return the minimum number of letters that must be inserted so that word becomes valid.

A string is called valid if it can be formed by concatenating the string "abc" several times.

 

Example 1:

Input: word = "b"
Output: 2
Explanation: Insert the letter "a" right before "b", and the letter "c" right next to "a" to obtain the valid string "abc".
Example 2:

Input: word = "aaa"
Output: 6
Explanation: Insert letters "b" and "c" next to each "a" to obtain the valid string "abcabcabc".
Example 3:

Input: word = "abc"
Output: 0
Explanation: word is already valid. No modifications are needed. 
 

Constraints:

1 <= word.length <= 50
word consists of letters "a", "b" and "c" only. 
'''

class Solution:
    def addMinimum(self, word: str) -> int:
        n = len(word)
        cnt = 1
        for i in range(1, n):
            if word[i] <= word[i-1]:
                cnt += 1
        return cnt * 3 - n



