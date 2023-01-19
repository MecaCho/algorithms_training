# encoding=utf8

'''
2299. Strong Password Checker II
A password is said to be strong if it satisfies all the following criteria:

It has at least 8 characters.
It contains at least one lowercase letter.
It contains at least one uppercase letter.
It contains at least one digit.
It contains at least one special character. The special characters are the characters in the following string: "!@#$%^&*()-+".
It does not contain 2 of the same character in adjacent positions (i.e., "aab" violates this condition, but "aba" does not).
Given a string password, return true if it is a strong password. Otherwise, return false.

 

Example 1:

Input: password = "IloveLe3tcode!"
Output: true
Explanation: The password meets all the requirements. Therefore, we return true.
Example 2:

Input: password = "Me+You--IsMyDream"
Output: false
Explanation: The password does not contain a digit and also contains 2 of the same character in adjacent positions. Therefore, we return false.
Example 3:

Input: password = "1aB!"
Output: false
Explanation: The password does not meet the length requirement. Therefore, we return false.
 

Constraints:

1 <= password.length <= 100
password consists of letters, digits, and special characters: "!@#$%^&*()-+".
'''

class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        if len(password) < 8:
            return False
        lowercases = 0
        uppercases = 0
        digits = 0
        specials = 0
        pre_ch = ''
        for i in range(len(password)):
            ch = password[i]
            if pre_ch and ch == pre_ch:
                return False
            pre_ch = ch
            if 'a' <= ch <= 'z':
                lowercases += 1
            elif 'A' <= ch <= 'Z':
                uppercases += 1
            elif '0' <= ch <= '9':
                digits += 1
            elif ch in '!@#$%^&*()-+':
                specials += 1
        if lowercases < 1 or uppercases < 1 or digits < 1 or specials < 1:
            return False
        return True

