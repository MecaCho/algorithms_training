# encoding=utf8

'''
295. Find Median from Data Stream
Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

For example,
[2,3,4], the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

void addNum(int num) - Add a integer number from the data stream to the data structure.
double findMedian() - Return the median of all elements so far.
 

Example:

addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3) 
findMedian() -> 2
 

Follow up:

If all integer numbers from the stream are between 0 and 100, how would you optimize it?
If 99% of all integer numbers from the stream are between 0 and 100, how would you optimize it?

295. 数据流的中位数
中位数是有序列表中间的数。如果列表长度是偶数，中位数则是中间两个数的平均值。

例如，

[2,3,4] 的中位数是 3

[2,3] 的中位数是 (2 + 3) / 2 = 2.5

设计一个支持以下两种操作的数据结构：

void addNum(int num) - 从数据流中添加一个整数到数据结构中。
double findMedian() - 返回目前所有元素的中位数。
示例：

addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3) 
findMedian() -> 2
进阶:

如果数据流中所有整数都在 0 到 100 范围内，你将如何优化你的算法？
如果数据流中 99% 的整数都在 0 到 100 范围内，你将如何优化你的算法？
'''



class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.arr = []
        self.count = 0


    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        i = 0
        j = len(self.arr) - 1
        while i <= j:
            mid = (i + j ) /2
            if num > self.arr[mid]:
                i = mid + 1
            else:
                j = mid - 1
        self.count += 1
        self.arr = self.arr[:i] + [num] + self.arr[i:]


    def findMedian(self):
        """
        :rtype: float
        """
        if not self.arr:
            return 0
        if self.count % 2 ==0:
            # print(self.arr[self.count/2], self.arr[self.count/2-1])
            return float((self.arr[self.count / 2] + self.arr[self.count / 2 - 1])) / 2
        return self.arr[self.count / 2]



        # Your MedianFinder object will be instantiated and called as such:
        # obj = MedianFinder()
        # obj.addNum(num)
        # param_2 = obj.findMedian()


'''
方法一：简单排序
照问题说的做。

算法：
将数字存储在可调整大小的容器中。每次需要输出中间值时，对容器进行排序并输出中间值。

C++
class MedianFinder {
    vector<double> store;

public:
    // Adds a number into the data structure.
    void addNum(int num)
    {
        store.push_back(num);
    }

    // Returns the median of current data stream
    double findMedian()
    {
        sort(store.begin(), store.end());

        int n = store.size();
        return (n & 1 ? store[n / 2] : (store[n / 2 - 1] + store[n / 2]) * 0.5);
    }
};
复杂度分析

时间复杂度：O(n\log n) + O(1) \simeq O(n\log n)O(nlogn)+O(1)≃O(nlogn)。
添加一个数字对于一个有效调整大小方案的容器来说需要花费 O(1)O(1) 的时间。
找到中间值主要取决于发生的排序。对于标准比较排序，这需要 O(n \log n)O(nlogn) 时间。
空间复杂度：O(n)O(n) 线性空间，用于在容器中保存输入。除了需要的空间之外没有其他空间（因为通常可以在适当的位置进行排序）。
方法二： 插入排序
保持输入容器始终排序

算法：
哪种算法允许将一个数字添加到已排序的数字列表中，但仍保持整个列表的排序状态？插入排序！

我们假设当前列表已经排序。当一个新的数字出现时，我们必须将它添加到列表中，同时保持列表的排序性质。这可以通过使用二分搜索找到插入传入号码的正确位置来轻松实现。
（记住，列表总是排序的）。一旦找到位置，我们需要将所有较高的元素移动一个空间，以便为传入的数字腾出空间。

当插入查询的数量较少或者中间查找查询的数量大致相同。 此方法会很好地工作。

class MedianFinder {
    vector<int> store; // resize-able container

public:
    // Adds a number into the data structure.
    void addNum(int num)
    {
        if (store.empty())
            store.push_back(num);
        else
            store.insert(lower_bound(store.begin(), store.end(), num), num);     // binary search and insertion combined
    }

    // Returns the median of current data stream
    double findMedian()
    {
        int n = store.size();
        return n & 1 ? store[n / 2] : (store[n / 2 - 1] + store[n / 2]) * 0.5;
    }
};
复杂度分析

时间复杂度：O(n) + O(\log n) \approx O(n)O(n)+O(logn)≈O(n).
二分搜索需要花费 O(\log n)O(logn) 时间才能找到正确的插入位置。
插入可能需要花费 O(n)O(n) 的时间，因为必须在容器中移动元素为新元素腾出空间。
空间复杂度：O(n)O(n) 线性空间，用于在容器中保存输入。
方法三：两个堆
以上两种方法对如何解决这个问题提供了一些有价值的见解。具体来说，我们可以推断出两件事：

如果我们可以一直直接访问中值元素，那么找到中值将需要一个恒定的时间。
如果我们能找到一种相当快速的方法来增加容器的数量，那么所产生的额外操作可能会减少。
但也许最重要的洞察是我们只需要一种一致的方式来访问中值元素，这是不容易观察到的。不需要对整个输入进行排序。

事实证明，有两种数据结构符合：

堆（或优先级队列）
自平衡二进制搜索树（我们将在方法4中详细讨论它们）
堆是这道题的天然原料！向元素添加元素需要对数时间复杂度。它们还可以直接访问组中的最大/最小元素。

如果我们可以用以下方式维护两个堆：

用于存储输入数字中较小一半的最大堆
用于存储输入数字的较大一半的最小堆
这样就可以访问输入中的中值：它们组成堆的顶部！

如果满足以下条件：

两个堆都是平衡的（或接近平衡的）
最大堆包含所有较小的数字，而最小堆包含所有较大的数字
那么我们可以这样说：

最大堆中的所有数字都小于或等于最大堆的top元素（我们称之为 xx）
最小堆中的所有数字都大于或等于最小堆的顶部元素（我们称之为 yy）
那么 xx 和 yy 几乎小于（或等于）元素的一半，大于（或等于）另一半。这就是中值元素的定义。

这使我们在这种方法中遇到了一个巨大的难题：平衡这两个堆！

算法：

两个优先级队列：
用于存储较小一半数字的最大堆 lo
用于存储较大一半数字的最小堆 hi
最大堆 lo 允许存储的元素最多比最小堆 hi 多一个。因此，如果我们处理了 kk 元素：
如果 k=2*n+1 \quad(\forall,n \in \mathbb z)k=2∗n+1(∀,n∈z) 则允许 lo 持有 n+1n+1 元素，而 hi 可以持有 nn 元素。
如果 k=2*n\quad(\forall,n\in\mathbb z)k=2∗n(∀,n∈z)，那么两个堆都是平衡的，并且每个堆都包含 nn 个元素。
这给了我们一个很好的特性，即当堆完全平衡时，中间值可以从两个堆的顶部派生。否则，最大堆 lo 的顶部保留合法的中间值。

添加一个数 num：
将 num 添加到最大堆 lo。因为 lo 收到了一个新元素，所以我们必须为 hi 做一个平衡步骤。因此，从 lo 中移除最大的元素并将其提供给 hi。
在上一个操作之后，最小堆 hi 可能会比最大堆 lo 保留更多的元素。我们通过从 hi 中去掉最小的元素并将其提供给 lo 来解决这个问题。
上面的步骤确保两个堆能够平衡
举个小例子就可以解决这个问题了！假设我们从流中获取输入 [41、35、62、5、97、108]。算法的运行过程如下：

Adding number 41
MaxHeap lo: [41]           // MaxHeap stores the largest value at the top (index 0)
MinHeap hi: []             // MinHeap stores the smallest value at the top (index 0)
Median is 41
=======================
Adding number 35
MaxHeap lo: [35]
MinHeap hi: [41]
Median is 38
=======================
Adding number 62
MaxHeap lo: [41, 35]
MinHeap hi: [62]
Median is 41
=======================
Adding number 4
MaxHeap lo: [35, 4]
MinHeap hi: [41, 62]
Median is 38
=======================
Adding number 97
MaxHeap lo: [41, 35, 4]
MinHeap hi: [62, 97]
Median is 41
=======================
Adding number 108
MaxHeap lo: [41, 35, 4]
MinHeap hi: [62, 97, 108]
Median is 51.5
C++
class MedianFinder {
    priority_queue<int> lo;                              // max heap
    priority_queue<int, vector<int>, greater<int>> hi;   // min heap

public:
    // Adds a number into the data structure.
    void addNum(int num)
    {
        lo.push(num);                                    // Add to max heap

        hi.push(lo.top());                               // balancing step
        lo.pop();

        if (lo.size() < hi.size()) {                     // maintain size property
            lo.push(hi.top());
            hi.pop();
        }
    }

    // Returns the median of current data stream
    double findMedian()
    {
        return lo.size() > hi.size() ? (double) lo.top() : (lo.top() + hi.top()) * 0.5;
    }
};
复杂度分析

时间复杂度： O(5 \cdot \log n) + O(1) \approx O(\log n)O(5⋅logn)+O(1)≈O(logn).。
最坏情况下，从顶部有三个堆插入和两个堆删除。每一个都需要花费 O(\log n)O(logn) 时间。
找到平均值需要持续的 O(1)O(1) 时间，因为可以直接访问堆的顶部。
空间复杂度：O(n)O(n) 用于在容器中保存输入的线性空间。
方法四：Multiset 和双指针
自平衡二进制搜索树（如AVL树）具有一些非常有趣的特性。它们将树的高度保持在对数范围内。因此，插入新元素具有相当好的时间性能。中值总是缠绕在树根或它的一个子树上。使用与方法 3 相同的方法解决这个问题，但是使用自平衡二叉树似乎是一个不错的选择。但是，实现这样一个树并不是简单的，而且容易出错。

大多数语言实现模拟这种行为的是 multiset 类。唯一的问题是跟踪中值元素。这很容易用指针解决！

我们保持两个指针：一个用于中位数较低的元素，另一个用于中位数较高的元素。当元素总数为奇数时，两个指针都指向同一个中值元素（因为在本例中只有一个中值）。当元素数为偶数时，指针指向两个连续的元素，其平均值是输入的代表中位数。

算法：

两个迭代器/指针 lo_median 和 hi_median，它们在 multiset上迭代 data。
添加数字 num 时，会出现三种情况：
容器当前为空。因此，我们只需插入 num 并设置两个指针指向这个元素。
容器当前包含奇数个元素。这意味着两个指针当前都指向同一个元素。
如果 num 不等于当前的中位数元素，则 num 将位于元素的任一侧。无论哪一边，该部分的大小都会增加，因此相应的指针会更新。例如，如果 num 小于中位数元素，则在插入 num 时，输入的较小半部分的大小将增加 11。
如果 num 等于当前的中位数元素，那么所采取的操作取决于 num 是如何插入数据的。
容器当前包含偶数个元素。这意味着指针当前指向连续的元素。
如果 num 是两个中值元素之间的数字，则 num 将成为新的中值。两个指针都必须指向它。
否则，num 会增加较小或较高一半的大小。我们相应地更新指针。必须记住，两个指针现在必须指向同一个元素。
找到中间值很容易！它只是两个指针 lo_median 和 hi_median 所指元素的平均值。
C++
class MedianFinder {
    multiset<int> data;
    multiset<int>::iterator lo_median, hi_median;

public:
    MedianFinder()
        : lo_median(data.end())
        , hi_median(data.end())
    {
    }

    void addNum(int num)
    {
        const size_t n = data.size();   // store previous size

        data.insert(num);               // insert into multiset

        if (!n) {
            // no elements before, one element now
            lo_median = hi_median = data.begin();
        }
        else if (n & 1) {
            // odd size before (i.e. lo == hi), even size now (i.e. hi = lo + 1)

            if (num < *lo_median)       // num < lo
                lo_median--;
            else                        // num >= hi
                hi_median++;            // insertion at end of equal range
        }
        else {
            // even size before (i.e. hi = lo + 1), odd size now (i.e. lo == hi)

            if (num > *lo_median && num < *hi_median) {
                lo_median++;                    // num in between lo and hi
                hi_median--;
            }
            else if (num >= *hi_median)         // num inserted after hi
                lo_median++;
            else                                // num <= lo < hi
                lo_median = --hi_median;        // insertion at end of equal range spoils lo
        }
    }

    double findMedian()
    {
        return (*lo_median + *hi_median) * 0.5;
    }
};
此解决方案的单指针版本更短（但更难理解），如下所示：

C++
class MedianFinder {
    multiset<int> data;
    multiset<int>::iterator mid;

public:
    MedianFinder()
        : mid(data.end())
    {
    }

    void addNum(int num)
    {
        const int n = data.size();
        data.insert(num);

        if (!n)                                 // first element inserted
            mid = data.begin();
        else if (num < *mid)                    // median is decreased
            mid = (n & 1 ? mid : prev(mid));
        else                                    // median is increased
            mid = (n & 1 ? next(mid) : mid);
    }

    double findMedian()
    {
        const int n = data.size();
        return (*mid + *next(mid, n % 2 - 1)) * 0.5;
    }
};
复杂度分析

时间复杂度：O(\log n) + O(1) \approx O(\log n)O(logn)+O(1)≈O(logn)。
对于标准 multiset 方案，插入数字需要花费 O(\log n)O(logn) 时间。
找到平均值需要固定的 O(1)O(1) 时间，因为中位数元素可以直接从两个指针访问。
空间复杂度：O(n)O(n) 用于在容器中保存输入的线性空间。

作者：LeetCode
链接：https://leetcode-cn.com/problems/find-median-from-data-stream/solution/shu-ju-liu-de-zhong-wei-shu-by-leetcode/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
