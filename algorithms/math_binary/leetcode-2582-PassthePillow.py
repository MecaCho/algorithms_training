# encoding=utf8

'''
2582. Pass the Pillow

There are n people standing in a line labeled from 1 to n. The first person in the line is holding a pillow initially. Every second, the person holding the pillow passes it to the next person standing in the line. Once the pillow reaches the end of the line, the direction changes, and people continue passing the pillow in the opposite direction.

For example, once the pillow reaches the nth person they pass it to the n - 1th person, then to the n - 2th person and so on.
Given the two positive integers n and time, return the index of the person holding the pillow after time seconds.

 

Example 1:

Input: n = 4, time = 5
Output: 2
Explanation: People pass the pillow in the following way: 1 -> 2 -> 3 -> 4 -> 3 -> 2.
Afer five seconds, the pillow is given to the 2nd person.
Example 2:

Input: n = 3, time = 2
Output: 3
Explanation: People pass the pillow in the following way: 1 -> 2 -> 3.
Afer two seconds, the pillow is given to the 3rd person.
 

Constraints:

2 <= n <= 1000
1 <= time <= 1000
'''

class Solution:
    def passThePillow(self, n: int, time: int) -> int:
# 如果 time<n\textit{time} < ntime<n，枕头没有传递到队尾，传递到 time+1\textit{time} + 1time+1。
# 如果 time≥n\textit{time} \ge ntime≥n，枕头已经传递过队尾，传递到 n−(time−(n−1))=n×2−time−1n - (\textit{time} - (n - 1)) = n \times 2 - \textit{time} - 1n−(time−(n−1))=n×2−time−1。
        time %= (n-1)*2
        return time + 1 if time < n else n*2 - time -1


