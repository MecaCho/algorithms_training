# encoding=utf8

'''
241. Different Ways to Add Parentheses
Given a string expression of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. You may return the answer in any order.

The test cases are generated such that the output values fit in a 32-bit integer and the number of different results does not exceed 104.

 

Example 1:

Input: expression = "2-1-1"
Output: [0,2]
Explanation:
((2-1)-1) = 0 
(2-(1-1)) = 2
Example 2:

Input: expression = "2*3-4*5"
Output: [-34,-14,-10,-10,10]
Explanation:
(2*(3-(4*5))) = -34 
((2*3)-(4*5)) = -14 
((2*(3-4))*5) = -10 
(2*((3-4)*5)) = -10 
(((2*3)-4)*5) = 10
 

Constraints:

1 <= expression.length <= 20
expression consists of digits and the operator '+', '-', and '*'.
All the integer values in the input expression are in the range [0, 99].
'''


class Solution(object):
    def diffWaysToCompute(self, expression):
        """
        :type expression: str
        :rtype: List[int]
        """
        res = []
        ops = {'+':lambda x,y:x+y, '-':lambda x,y:x-y, '*':lambda x,y:x*y}
        for indx in range(1,len(expression)-1):
            if expression[indx] in ops.keys():
                for left in self.diffWaysToCompute(expression[:indx]):
                    for right in self.diffWaysToCompute(expression[indx+1:]):
                        res.append(ops[expression[indx]](left,right))                      
        if not res:
            res.append(int(expression))
        
        return res
        


