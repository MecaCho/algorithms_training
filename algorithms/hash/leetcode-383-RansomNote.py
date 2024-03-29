# encoding=utf8

'''
383. Ransom Note
Given two stings ransomNote and magazine, return true if ransomNote can be constructed from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

 

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true
 

Constraints:

1 <= ransomNote.length, magazine.length <= 105
ransomNote and magazine consist of lowercase English letters.
'''

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        c1 = Counter(ransomNote)
        c2 = Counter(magazine)
        for k,v in c1.items():
            if not c2[k] or c2[k] < v:
                return False
        return True






class Solution:
        def canConstruct(self, ransomNote: str, magazine: str) -> bool:
                    return Counter(ransomNote) <= Counter(magazine)
