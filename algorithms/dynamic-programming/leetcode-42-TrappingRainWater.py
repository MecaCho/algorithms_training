# encoding=utf8



'''
42. Trapping Rain Water
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6

42. 接雨水
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。



上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 感谢 Marcos 贡献此图。

示例:

输入: [0,1,0,2,1,0,1,3,2,1,2,1]
输出: 6
'''

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0
        length = len(height)
        max_left = [height[0]]
        max_right = [0 for i in range(length-1)] + [height[-1]]
        for i in range(1, length):
            max_left.append(max(max_left[i-1], height[i-1]))
            j = length - 1 - i

            max_right[j] = max(max_right[j+1], height[j+1])

        print(max_left, max_right)
        res = 0
        for i in range(1, length - 1):

            res += max(min(max_left[i], max_right[i]) - height[i], 0)
        return res


class Solution20210402(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0
        length = len(height)

        max_left = [height[0]]
        max_right = [0 for _ in range(length - 1)] + [height[-1]]

        for i in range(1, length):
            j = length - i - 1
            max_left.append(max(max_left[i - 1], height[i - 1]))
            max_right[j] = max(height[j + 1], max_right[j + 1])

        print(max_left, max_right)

        res = 0
        for i in range(length):
            res += max(0, min(max_right[i] - height[i], max_left[i] - height[i]))

        return res



class Solution1(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # 双指针
        length = len(height)
        i, j = 0, length - 1

        left_max = height[0]
        right_max = height[-1]

        res = 0
        while i < j:
            left_max = max(height[i], left_max)
            right_max = max(height[j], right_max)
            if height[i] < height[j]:
                res += left_max - height[i]
                i += 1
            else:
                res += right_max - height[j]
                j -= 1
        return res



# solutions


'''
方法一：动态规划
对于下标 ii，下雨后水能到达的最大高度等于下标 ii 两边的最大高度的最小值，下标 ii 处能接的雨水量等于下标 ii 处的水能到达的最大高度减去 \textit{height}[i]height[i]。

朴素的做法是对于数组 \textit{height}height 中的每个元素，分别向左和向右扫描并记录左边和右边的最大高度，然后计算每个下标位置能接的雨水量。假设数组 \textit{height}height 的长度为 nn，该做法需要对每个下标位置使用 O(n)O(n) 的时间向两边扫描并得到最大高度，因此总时间复杂度是 O(n^2)O(n 
2
 )。

上述做法的时间复杂度较高是因为需要对每个下标位置都向两边扫描。如果已经知道每个位置两边的最大高度，则可以在 O(n)O(n) 的时间内得到能接的雨水总量。使用动态规划的方法，可以在 O(n)O(n) 的时间内预处理得到每个位置两边的最大高度。

创建两个长度为 nn 的数组 \textit{leftMax}leftMax 和 \textit{rightMax}rightMax。对于 0 \le i<n0≤i<n，\textit{leftMax}[i]leftMax[i] 表示下标 ii 及其左边的位置中，\textit{height}height 的最大高度，\textit{rightMax}[i]rightMax[i] 表示下标 ii 及其右边的位置中，\textit{height}height 的最大高度。

显然，\textit{leftMax}[0]=\textit{height}[0]leftMax[0]=height[0]，\textit{rightMax}[n-1]=\textit{height}[n-1]rightMax[n−1]=height[n−1]。两个数组的其余元素的计算如下：

当 1 \le i \le n-11≤i≤n−1 时，\textit{leftMax}[i]=\max(\textit{leftMax}[i-1], \textit{height}[i])leftMax[i]=max(leftMax[i−1],height[i])；

当 0 \le i \le n-20≤i≤n−2 时，\textit{rightMax}[i]=\max(\textit{rightMax}[i+1], \textit{height}[i])rightMax[i]=max(rightMax[i+1],height[i])。

因此可以正向遍历数组 \textit{height}height 得到数组 \textit{leftMax}leftMax 的每个元素值，反向遍历数组 \textit{height}height 得到数组 \textit{rightMax}rightMax 的每个元素值。

在得到数组 \textit{leftMax}leftMax 和 \textit{rightMax}rightMax 的每个元素值之后，对于 0 \le i<n0≤i<n，下标 ii 处能接的雨水量等于 \min(\textit{leftMax}[i],\textit{rightMax}[i])-\textit{height}[i]min(leftMax[i],rightMax[i])−height[i]。遍历每个下标位置即可得到能接的雨水总量。

动态规划做法可以由下图体现。



JavaGolangJavaScriptPython3C++C

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        n = len(height)
        leftMax = [height[0]] + [0] * (n - 1)
        for i in range(1, n):
            leftMax[i] = max(leftMax[i - 1], height[i])

        rightMax = [0] * (n - 1) + [height[n - 1]]
        for i in range(n - 2, -1, -1):
            rightMax[i] = max(rightMax[i + 1], height[i])

        ans = sum(min(leftMax[i], rightMax[i]) - height[i] for i in range(n))
        return ans
复杂度分析

时间复杂度：O(n)O(n)，其中 nn 是数组 \textit{height}height 的长度。计算数组 \textit{leftMax}leftMax 和 \textit{rightMax}rightMax 的元素值各需要遍历数组 \textit{height}height 一次，计算能接的雨水总量还需要遍历一次。

空间复杂度：O(n)O(n)，其中 nn 是数组 \textit{height}height 的长度。需要创建两个长度为 nn 的数组 \textit{leftMax}leftMax 和 \textit{rightMax}rightMax。

方法二：单调栈
除了计算并存储每个位置两边的最大高度以外，也可以用单调栈计算能接的雨水总量。

维护一个单调栈，单调栈存储的是下标，满足从栈底到栈顶的下标对应的数组 \textit{height}height 中的元素递减。

从左到右遍历数组，遍历到下标 ii 时，如果栈内至少有两个元素，记栈顶元素为 \textit{top}top，\textit{top}top 的下面一个元素是 \textit{left}left，则一定有 \textit{height}[\textit{left}] \ge \textit{height}[\textit{top}]height[left]≥height[top]。如果 \textit{height}[i]>\textit{height}[\textit{top}]height[i]>height[top]，则得到一个可以接雨水的区域，该区域的宽度是 i-\textit{left}-1i−left−1，高度是 \min(\textit{height}[\textit{left}],\textit{height}[i])-\textit{height}[\textit{top}]min(height[left],height[i])−height[top]，根据宽度和高度即可计算得到该区域能接的雨水量。

为了得到 \textit{left}left，需要将 \textit{top}top 出栈。在对 \textit{top}top 计算能接的雨水量之后，\textit{left}left 变成新的 \textit{top}top，重复上述操作，直到栈变为空，或者栈顶下标对应的 \textit{height}height 中的元素大于或等于 \textit{height}[i]height[i]。

在对下标 ii 处计算能接的雨水量之后，将 ii 入栈，继续遍历后面的下标，计算能接的雨水量。遍历结束之后即可得到能接的雨水总量。

下面用一个例子 \textit{height}=[0,1,0,2,1,0,1,3,2,1,2,1]height=[0,1,0,2,1,0,1,3,2,1,2,1] 来帮助读者理解单调栈的做法。


1 / 21

JavaGolangJavaScriptPython3C++C

class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        stack = list()
        n = len(height)
        
        for i, h in enumerate(height):
            while stack and h > height[stack[-1]]:
                top = stack.pop()
                if not stack:
                    break
                left = stack[-1]
                currWidth = i - left - 1
                currHeight = min(height[left], height[i]) - height[top]
                ans += currWidth * currHeight
            stack.append(i)
        
        return ans
复杂度分析

时间复杂度：O(n)O(n)，其中 nn 是数组 \textit{height}height 的长度。从 00 到 n-1n−1 的每个下标最多只会入栈和出栈各一次。

空间复杂度：O(n)O(n)，其中 nn 是数组 \textit{height}height 的长度。空间复杂度主要取决于栈空间，栈的大小不会超过 nn。

方法三：双指针
动态规划的做法中，需要维护两个数组 \textit{leftMax}leftMax 和 \textit{rightMax}rightMax，因此空间复杂度是 O(n)O(n)。是否可以将空间复杂度降到 O(1)O(1)？

注意到下标 ii 处能接的雨水量由 \textit{leftMax}[i]leftMax[i] 和 \textit{rightMax}[i]rightMax[i] 中的最小值决定。由于数组 \textit{leftMax}leftMax 是从左往右计算，数组 \textit{rightMax}rightMax 是从右往左计算，因此可以使用双指针和两个变量代替两个数组。

维护两个指针 \textit{left}left 和 \textit{right}right，以及两个变量 \textit{leftMax}leftMax 和 \textit{rightMax}rightMax，初始时 \textit{left}=0,\textit{right}=n-1,\textit{leftMax}=0,\textit{rightMax}=0left=0,right=n−1,leftMax=0,rightMax=0。指针 \textit{left}left 只会向右移动，指针 \textit{right}right 只会向左移动，在移动指针的过程中维护两个变量 \textit{leftMax}leftMax 和 \textit{rightMax}rightMax 的值。

当两个指针没有相遇时，进行如下操作：

使用 \textit{height}[\textit{left}]height[left] 和 \textit{height}[\textit{right}]height[right] 的值更新 \textit{leftMax}leftMax 和 \textit{rightMax}rightMax 的值；

如果 \textit{height}[\textit{left}]<\textit{height}[\textit{right}]height[left]<height[right]，则必有 \textit{leftMax}<\textit{rightMax}leftMax<rightMax，下标 \textit{left}left 处能接的雨水量等于 \textit{leftMax}-\textit{height}[\textit{left}]leftMax−height[left]，将下标 \textit{left}left 处能接的雨水量加到能接的雨水总量，然后将 \textit{left}left 加 11（即向右移动一位）；

如果 \textit{height}[\textit{left}] \ge \textit{height}[\textit{right}]height[left]≥height[right]，则必有 \textit{leftMax} \ge \textit{rightMax}leftMax≥rightMax，下标 \textit{right}right 处能接的雨水量等于 \textit{rightMax}-\textit{height}[\textit{right}]rightMax−height[right]，将下标 \textit{right}right 处能接的雨水量加到能接的雨水总量，然后将 \textit{right}right 减 11（即向左移动一位）。

当两个指针相遇时，即可得到能接的雨水总量。

下面用一个例子 \textit{height}=[0,1,0,2,1,0,1,3,2,1,2,1]height=[0,1,0,2,1,0,1,3,2,1,2,1] 来帮助读者理解双指针的做法。


1 / 12

JavaGolangJavaScriptPython3C++C

class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        left, right = 0, len(height) - 1
        leftMax = rightMax = 0

        while left < right:
            leftMax = max(leftMax, height[left])
            rightMax = max(rightMax, height[right])
            if height[left] < height[right]:
                ans += leftMax - height[left]
                left += 1
            else:
                ans += rightMax - height[right]
                right -= 1
        
        return ans
复杂度分析

时间复杂度：O(n)O(n)，其中 nn 是数组 \textit{height}height 的长度。两个指针的移动总次数不超过 nn。

空间复杂度：O(1)O(1)。只需要使用常数的额外空间。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/trapping-rain-water/solution/jie-yu-shui-by-leetcode-solution-tuvc/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
