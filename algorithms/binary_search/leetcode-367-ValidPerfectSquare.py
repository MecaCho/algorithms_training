# encoding=utf8

'''
367. Valid Perfect Square
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Follow up: Do not use any built-in library function such as sqrt.

 

Example 1:

Input: num = 16
Output: true
Example 2:

Input: num = 14
Output: false
 

Constraints:

1 <= num <= 2^31 - 1


367. 有效的完全平方数
给定一个 正整数 num ，编写一个函数，如果 num 是一个完全平方数，则返回 true ，否则返回 false 。

进阶：不要 使用任何内置的库函数，如  sqrt 。

 

示例 1：

输入：num = 16
输出：true
示例 2：

输入：num = 14
输出：false
 

提示：

1 <= num <= 2^31 - 1

'''

class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        l, r = 0, num
        while l <= r:
            mid = (l+r)/2
            p = mid*mid
            if p == num:
                return True
            elif p > num:
                r = mid - 1
            else:
                l = mid + 1
        return False
      
# solutions

'''
前言
在方法一中，我们使用内置的库函数来解决问题。

在方法二、方法三和方法四中，我们不使用库函数来解决进阶问题。注意，因为不能使用任何内置的库函数，所以也不能使用类似 \sqrt{x} = x^{\frac{1}{2}} = (e^{\ln x})^{\frac{1}{2}} = e^{\frac{1}{2} \ln x} 
x
​
 =x 
2
1
​
 
 =(e 
lnx
 ) 
2
1
​
 
 =e 
2
1
​
 lnx
  的公式来通过其他库函数计算平方根。

方法一：使用内置的库函数
思路和算法

根据完全平方数的性质，我们只需要直接判断 \textit{num}num 的平方根 xx 是否为整数即可。对于不能判断浮点数的值是否等于整数的语言，则可以通过以下规则判断：

若 \sqrt{\textit{num}} 
num
​
  为正整数，则有 \lfloor x_i \rfloor^2 = (\sqrt{\textit{num}})^2 = \textit{num}⌊x 
i
​
 ⌋ 
2
 =( 
num
​
 ) 
2
 =num，其中符号 \lfloor x \rfloor⌊x⌋ 表示 xx 的向下取整。
代码

Python3JavaC#C++GolangJavaScript

func isPerfectSquare(num int) bool {
    x := int(math.Sqrt(float64(num)))
    return x*x == num
}
复杂度分析

代码中使用的 \texttt{pow}pow 函数的时空复杂度与 CPU 支持的指令集相关，这里不深入分析。

方法二：暴力
思路和算法

如果 \textit{num}num 为完全平方数，那么一定存在正整数 xx 满足 x \times x = \textit{num}x×x=num。于是我们可以从 11 开始，从小到大遍历所有正整数，寻找是否存在满足 x \times x = \textit{num}x×x=num 的正整数 xx。在遍历中，如果出现正整数 xx 使 x \times x > \textit{num}x×x>num，那么更大的正整数也不可能满足 x \times x = \textit{num}x×x=num，不需要继续遍历了。

代码

Python3JavaC#C++GolangJavaScript

func isPerfectSquare(num int) bool {
    for x := 1; x*x <= num; x++ {
        if x*x == num {
            return true
        }
    }
    return false
}
复杂度分析

时间复杂度：O(\sqrt{n})O( 
n
​
 )，其中 nn 为正整数 \textit{num}num 的最大值。我们最多需要遍历 \sqrt{n} + 1 
n
​
 +1 个正整数。

空间复杂度：O(1)O(1)。

方法三：二分查找
思路和算法

考虑使用二分查找来优化方法二中的搜索过程。因为 \textit{num}num 是正整数，所以若正整数 xx 满足 x \times x = \textit{num}x×x=num，则 xx 一定满足 1 \le x \le \textit{num}1≤x≤num。于是我们可以将 11 和 \textit{num}num 作为二分查找搜索区间的初始边界。

细节

因为我们在移动左侧边界 \textit{left}left 和右侧边界 \textit{right}right 时，新的搜索区间都不会包含被检查的下标 \textit{mid}mid，所以搜索区间的边界始终是我们没有检查过的。因此，当\textit{left} = \textit{right}left=right 时，我们仍需要检查 \textit{mid} = (\textit{left}+\textit{right}) / 2mid=(left+right)/2。

代码

Python3JavaC#C++GolangJavaScript

func isPerfectSquare(num int) bool {
    left, right := 0, num
    for left <= right {
        mid := (left + right) / 2
        square := mid * mid
        if square < num {
            left = mid + 1
        } else if square > num {
            right = mid - 1
        } else {
            return true
        }
    }
    return false
}
复杂度分析

时间复杂度：O(\log n)O(logn)，其中 nn 为正整数 \textit{num}num 的最大值。

空间复杂度：O(1)O(1)。

方法四：牛顿迭代法
前置知识

牛顿迭代法。牛顿迭代法是一种近似求解方程（近似求解函数零点）的方法。其本质是借助泰勒级数，从初始值开始快速向函数零点逼近。



对于函数 f(x)f(x)，我们任取 x_0x 
0
​
  作为初始值。在每一次迭代中，我们根据当前值 x_ix 
i
​
  找到函数图像上的点 (x_i,f(x_i))(x 
i
​
 ,f(x 
i
​
 ))，过该点做一条斜率为该点导数 f'(x_0)f 
′
 (x 
0
​
 ) 的直线，该直线与横轴（XX 轴）的交点记作 (x_{i+1},0)(x 
i+1
​
 ,0)。x_{i+1}x 
i+1
​
  相较于 x_ix 
i
​
  而言，距离函数零点更近。在经过多次迭代后，我们就可以得到距离函数零点非常近的交点。

思路

如果 \textit{num}num 为完全平方数，那么一定存在正整数 xx 满足 x \times x = \textit{num}x×x=num。于是我们写出如下方程：

y = f(x) = x^2 - \textit{num}
y=f(x)=x 
2
 −num

如果方程能够取得整数解，则说明存在满足 x \times x = \textit{num}x×x=num 的正整数 xx。这个方程可以通过牛顿迭代法求解。

算法

在算法实现中，我们需要解决以下四个问题：

如何选取初始值？
因为 \textit{num}num 是正整数，所以 y = x^2 - \textit{num}y=x 
2
 −num 有两个零点 - \sqrt{\textit{num}}− 
num
​
  和 \sqrt{\textit{num}} 
num
​
 ，其中 1 \le \sqrt{\textit{num}} \le \textit{num}1≤ 
num
​
 ≤num。我们只需要判断 \sqrt{\textit{num}} 
num
​
  是否为正整数即可。又因为 y = x^2 - \textit{num}y=x 
2
 −num 是凸函数，所以只要我们选取的初始值大于等于 \sqrt{\textit{num}} 
num
​
 ，那么每次迭代得到的结果也都会大于等于 \sqrt{\textit{num}} 
num
​
 。

因此，我们可以选择 \textit{num}num 作为初始值。

如何进行迭代？
对 f(x)f(x) 求导，得到

f'(x) = 2 x
f 
′
 (x)=2x

假设当前值为 x_ix 
i
​
 ，将 x_ix 
i
​
  代入 f(x)f(x) 得到函数图像上的点 (x_i,x_i^2 - \textit{num})(x 
i
​
 ,x 
i
2
​
 −num)，过该点做一条斜率为 f'(x_i) = 2 x_if 
′
 (x 
i
​
 )=2x 
i
​
  的直线，则直线的方程为

y - (x_i^2 - \textit{num}) = 2 x_i (x - x_i)
y−(x 
i
2
​
 −num)=2x 
i
​
 (x−x 
i
​
 )

直线与横轴（XX 轴）交点的横坐标为上式中的 y = 0y=0 时 xx 的解。于是令上式中 y=0y=0，得到

2 x_i x - x_i^2 - \textit{num} = 0
2x 
i
​
 x−x 
i
2
​
 −num=0

整理上式即可得到下一次迭代的值：

x_{i+1} = \frac{x_i^2 + \textit{num}}{2 x_i} = \frac{1}{2} \big( x_i + \frac{\textit{num}}{x_i} \big) \tag{1}
x 
i+1
​
 = 
2x 
i
​
 
x 
i
2
​
 +num
​
 = 
2
1
​
 (x 
i
​
 + 
x 
i
​
 
num
​
 )(1)

如何判断迭代是否可以结束？
每一次迭代后，我们都会距离零点更近一步，所以当相邻两次迭代的结果非常接近时，我们就可以断定，此时的结果已经足够我们得到答案了。一般来说，可以判断相邻两次迭代的结果的差值是否小于一个极小的非负数 \epsilonϵ，其中 \epsilonϵ 一般可以取 10^{-6}10 
−6
  或 10^{-7}10 
−7
 。

如何通过迭代得到的近似零点得到最终的答案？
因为初始值的选择以及 y = x^2 - \textit{num}y=x 
2
 −num 凸函数的性质，我们通过迭代得到的 x_ix 
i
​
  一定是 \sqrt{\textit{num}} 
num
​
  的近似零点，且满足 x_i \ge \sqrt{\textit{num}}x 
i
​
 ≥ 
num
​
 。

当 \textit{num}num 是完全平方数时，\sqrt{\textit{num}} 
num
​
  为正整数，则有 \lfloor x_i \rfloor^2 = (\sqrt{\textit{num}})^2 = \textit{num}⌊x 
i
​
 ⌋ 
2
 =( 
num
​
 ) 
2
 =num，其中符号 \lfloor x \rfloor⌊x⌋ 表示 xx 的向下取整。

代码

Python3JavaC#C++GolangJavaScript

func isPerfectSquare(num int) bool {
    x0 := float64(num)
    for {
        x1 := (x0 + float64(num)/x0) / 2
        if x0-x1 < 1e-6 {
            x := int(x0)
            return x*x == num
        }
        x0 = x1
    }
}
复杂度分析

时间复杂度：O(\log n)O(logn)，其中 nn 为正整数 \textit{num}num 的最大值。具体计算如下：

不妨设当前值为 x_ix 
i
​
 ，误差为 \epsilon_i = x_i^2 - \textit{num}ϵ 
i
​
 =x 
i
2
​
 −num；根据式 (1)(1) 解得下一次迭代的值为 x_{i+1}x 
i+1
​
 ，误差为

\begin{aligned} \epsilon_{i+1} & = x_{i+1}^2 - \textit{num} \\ & = \Big( \frac{x_i^2 + \textit{num}}{2 x_i} \Big)^2 - \textit{num} \\ & = \frac{(x_i^2 - \textit{num})^2}{4 x_i^2} \\ & = \frac{\epsilon_i^2}{4x_i^2} \end{aligned}
ϵ 
i+1
​
 
​
  
=x 
i+1
2
​
 −num
=( 
2x 
i
​
 
x 
i
2
​
 +num
​
 ) 
2
 −num
= 
4x 
i
2
​
 
(x 
i
2
​
 −num) 
2
 
​
 
= 
4x 
i
2
​
 
ϵ 
i
2
​
 
​
 
​
 

因为 \textit{num}num 是正整数，所以有

\frac{\epsilon_{i+1}}{\epsilon_i} = \frac{\epsilon_i}{4 x_i^2} = \frac{x_i^2 - \textit{num}}{4 x_i^2} < \frac{1}{4}
ϵ 
i
​
 
ϵ 
i+1
​
 
​
 = 
4x 
i
2
​
 
ϵ 
i
​
 
​
 = 
4x 
i
2
​
 
x 
i
2
​
 −num
​
 < 
4
1
​
 

因为每一次迭代都可以将误差缩小到原来的 \frac{1}{4} 
4
1
​
  以下，所以只需要最多 \log_4 mlog 
4
​
 m 次迭代即可将误差缩小到阈值范围内，其中 mm 为初始值的误差与阈值的比。根据大 OO 符号表示法，其量级可以表示为 O(\log n)O(logn)。

空间复杂度：O(1)O(1)。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/valid-perfect-square/solution/you-xiao-de-wan-quan-ping-fang-shu-by-le-wkee/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
