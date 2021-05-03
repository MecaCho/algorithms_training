'''

7. Reverse Integer
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.


Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.


7. 整数反转
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

示例 1:

输入: 123
输出: 321
 示例 2:

输入: -123
输出: -321
示例 3:

输入: 120
输出: 21
注意:

假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231,  231 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。
'''


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if -10 < x < 10:
            return x
        res = int(str(x)[::-1].lstrip("0") if x > 0 else "-" + str(x)[:0:-1].lstrip("0"))
        if -2**31<res<2**31-1:
            return res
        return 0
       
       
       
class Solution20210503(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        flag = False
        if x < 0:
            x = -x
            flag = True
        res = 0
        while x:
            num = x % 10
            res = 10 * res + num
            x /= 10
        if -2**31 <= res <= 2**31-1:
            return -res if flag else res
        return 0

       
# solutions

'''
方法一：数学
思路

记 \textit{rev}rev 为翻转后的数字，为完成翻转，我们可以重复「弹出」xx 的末尾数字，将其「推入」\textit{rev}rev 的末尾，直至 xx 为 00。

要在没有辅助栈或数组的帮助下「弹出」和「推入」数字，我们可以使用如下数学方法：


// 弹出 x 的末尾数字 digit
digit = x % 10
x /= 10

// 将数字 digit 推入 rev 末尾
rev = rev * 10 + digit
题目需要判断反转后的数字是否超过 3232 位有符号整数的范围 [-2^{31},2^{31}-1][−2 
31
 ,2 
31
 −1]，例如 x=2123456789x=2123456789 反转后的 \textit{rev}=9876543212>2^{31}-1=2147483647rev=9876543212>2 
31
 −1=2147483647，超过了 3232 位有符号整数的范围。

因此我们需要在「推入」数字之前，判断是否满足

-2^{31}\le\textit{rev}\cdot10+\textit{digit}\le2^{31}-1
−2 
31
 ≤rev⋅10+digit≤2 
31
 −1

若该不等式不成立则返回 00。

但是题目要求不允许使用 6464 位整数，即运算过程中的数字必须在 3232 位有符号整数的范围内，因此我们不能直接按照上述式子计算，需要另寻他路。

考虑 x>0x>0 的情况，记 \textit{INT\_MAX}=2^{31}-1=2147483647INT_MAX=2 
31
 −1=2147483647，由于

\begin{aligned} \textit{INT\_MAX}&=\lfloor\dfrac{\textit{INT\_MAX}}{10}\rfloor\cdot10+(\textit{INT\_MAX}\bmod10)\\ &=\lfloor\dfrac{\textit{INT\_MAX}}{10}\rfloor\cdot10+7 \end{aligned}
INT_MAX
​	
  
=⌊ 
10
INT_MAX
​	
 ⌋⋅10+(INT_MAXmod10)
=⌊ 
10
INT_MAX
​	
 ⌋⋅10+7
​	
 

则不等式

\textit{rev}\cdot10+\textit{digit}\le\textit{INT\_MAX}
rev⋅10+digit≤INT_MAX

等价于

\textit{rev}\cdot10+\textit{digit}\le\lfloor\dfrac{\textit{INT\_MAX}}{10}\rfloor\cdot10+7
rev⋅10+digit≤⌊ 
10
INT_MAX
​	
 ⌋⋅10+7

移项得

(\textit{rev}-\lfloor\dfrac{\textit{INT\_MAX}}{10}\rfloor)\cdot10\le7-\textit{digit}
(rev−⌊ 
10
INT_MAX
​	
 ⌋)⋅10≤7−digit

讨论该不等式成立的条件：

若 \textit{rev}>\lfloor\cfrac{\textit{INT\_MAX}}{10}\rfloorrev>⌊ 
10
INT_MAX
​	
 ⌋，由于 \textit{digit}\ge0digit≥0，不等式不成立。
若 \textit{rev}=\lfloor\cfrac{\textit{INT\_MAX}}{10}\rfloorrev=⌊ 
10
INT_MAX
​	
 ⌋，当且仅当 \textit{digit}\le7digit≤7 时，不等式成立。
若 \textit{rev}<\lfloor\cfrac{\textit{INT\_MAX}}{10}\rfloorrev<⌊ 
10
INT_MAX
​	
 ⌋，由于 \textit{digit}\le9digit≤9，不等式成立。

注意到当 \textit{rev}=\lfloor\cfrac{\textit{INT\_MAX}}{10}\rfloorrev=⌊ 
10
INT_MAX
​	
 ⌋ 时若还能推入数字，则说明 xx 的位数与 \textit{INT\_MAX}INT_MAX 的位数相同，且要推入的数字 \textit{digit}digit 为 xx 的最高位。由于 xx 不超过 \textit{INT\_MAX}INT_MAX，因此 \textit{digit}digit 不会超过 \textit{INT\_MAX}INT_MAX 的最高位，即 \textit{digit}\le2digit≤2。所以实际上当 \textit{rev}=\lfloor\cfrac{\textit{INT\_MAX}}{10}\rfloorrev=⌊ 
10
INT_MAX
​	
 ⌋ 时不等式必定成立。

因此判定条件可简化为：当且仅当 \textit{rev}\le\lfloor\cfrac{\textit{INT\_MAX}}{10}\rfloorrev≤⌊ 
10
INT_MAX
​	
 ⌋ 时，不等式成立。

x<0x<0 的情况类似，留给读者自证，此处不再赘述。

综上所述，判断不等式

-2^{31}\le\textit{rev}\cdot10+\textit{digit}\le2^{31}-1
−2 
31
 ≤rev⋅10+digit≤2 
31
 −1

是否成立，可改为判断不等式

\lceil\cfrac{-2^{31}}{10}\rceil\le\textit{rev}\le\lfloor\dfrac{2^{31}-1}{10}\rfloor
⌈ 
10
−2 
31
 
​	
 ⌉≤rev≤⌊ 
10
2 
31
 −1
​	
 ⌋

是否成立，若不成立则返回 00。

代码

C++JavaC#GolangPython3CJavaScript

func reverse(x int) (rev int) {
    for x != 0 {
        if rev < math.MinInt32/10 || rev > math.MaxInt32/10 {
            return 0
        }
        digit := x % 10
        x /= 10
        rev = rev*10 + digit
    }
    return
}
复杂度分析

时间复杂度：O(\log |x|)O(log∣x∣)。翻转的次数即 xx 十进制的位数。

空间复杂度：O(1)O(1)。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/reverse-integer/solution/zheng-shu-fan-zhuan-by-leetcode-solution-bccn/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
