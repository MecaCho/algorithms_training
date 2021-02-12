'''
703. 数据流中的第K大元素
设计一个找到数据流中第K大元素的类（class）。注意是排序后的第K大元素，不是第K个不同的元素。

你的 KthLargest 类需要一个同时接收整数 k 和整数数组nums 的构造器，它包含数据流中的初始元素。每次调用 KthLargest.add，返回当前数据流中第K大的元素。

示例:

int k = 3;
int[] arr = [4,5,8,2];
KthLargest kthLargest = new KthLargest(3, arr);
kthLargest.add(3);   // returns 4
kthLargest.add(5);   // returns 5
kthLargest.add(10);  // returns 5
kthLargest.add(9);   // returns 8
kthLargest.add(4);   // returns 8
说明:
你可以假设 nums 的长度≥ k-1 且k ≥ 1。

703. Kth Largest Element in a Stream
Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Your KthLargest class will have a constructor which accepts an integer k and an integer array nums, which contains initial elements from the stream. For each call to the method KthLargest.add, return the element representing the kth largest element in the stream.

Example:

int k = 3;
int[] arr = [4,5,8,2];
KthLargest kthLargest = new KthLargest(3, arr);
kthLargest.add(3);   // returns 4
kthLargest.add(5);   // returns 5
kthLargest.add(10);  // returns 5
kthLargest.add(9);   // returns 8
kthLargest.add(4);   // returns 8
Note:
You may assume that nums' length ≥ k-1 and k ≥ 1.

'''

import heapq
class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.h = nums
        heapq.heapify(self.h)
        for i in range(len(nums) - k):
            heapq.heappop(self.h)


    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if len(self.h) < self.k:
            heapq.heappush(self.h, val)
        else:
            if self.h[0] < val:
                heapq.heappop(self.h)
                heapq.heappush(self.h, val)



# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

# solutions

'''
方法一：优先队列
我们可以使用一个大小为 kk 的优先队列来存储前 kk 大的元素，其中优先队列的队头为队列中最小的元素，也就是第 kk 大的元素。

在单次插入的操作中，我们首先将元素 \textit{val}val 加入到优先队列中。如果此时优先队列的大小大于 kk，我们需要将优先队列的队头元素弹出，以保证优先队列的大小为 kk。

C++JavaGolangCJavaScript

type KthLargest struct {
    sort.IntSlice
    k int
}

func Constructor(k int, nums []int) KthLargest {
    kl := KthLargest{k: k}
    for _, val := range nums {
        kl.Add(val)
    }
    return kl
}

func (kl *KthLargest) Push(v interface{}) {
    kl.IntSlice = append(kl.IntSlice, v.(int))
}

func (kl *KthLargest) Pop() interface{} {
    a := kl.IntSlice
    v := a[len(a)-1]
    kl.IntSlice = a[:len(a)-1]
    return v
}

func (kl *KthLargest) Add(val int) int {
    heap.Push(kl, val)
    if kl.Len() > kl.k {
        heap.Pop(kl)
    }
    return kl.IntSlice[0]
}
复杂度分析

时间复杂度：

初始化时间复杂度为：O(n \log k)O(nlogk) ，其中 nn 为初始化时 \textit{nums}nums 的长度；

单次插入时间复杂度为：O(\log k)O(logk)。

空间复杂度：O(k)O(k)。需要使用优先队列存储前 kk 大的元素。
'''

# solutions1

'''
方法一：直接降序排序，然后取第k个元素返回，add时每次都再排序一次，这样时间复杂度为O(k*logk)

# 1.直接排序
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        self.k = k
        self.nums.sort(reverse = True)
        while len(self.nums) > k:
            self.nums.pop()

    def add(self, val: int) -> int:
        self.nums.append(val)
        self.nums.sort(reverse = True)
        if len(self.nums) > self.k:
            self.nums.pop()
        return self.nums[-1]
方法二：使用小顶堆实现的优先队列，Python 中标准库 heapq 就是小顶堆，时间复杂度降低为O(k)

# 2.小顶堆
import heapq
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.pool = nums
        heapq.heapify(self.pool)
        self.k = k
        while len(self.pool) > k:
            heapq.heappop(self.pool)

    def add(self, val: int) -> int:
        if len(self.pool) < self.k:
            heapq.heappush(self.pool, val)
        elif val > self.pool[0]:
            heapq.heapreplace(self.pool, val)
        return self.pool[0]
'''
