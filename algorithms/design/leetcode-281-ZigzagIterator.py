'''
281. 锯齿迭代器
给出两个一维的向量，请你实现一个迭代器，交替返回它们中间的元素。

示例:

输入:
v1 = [1,2]
v2 = [3,4,5,6]

输出: [1,3,2,4,5,6]

解析: 通过连续调用 next 函数直到 hasNext 函数返回 false，
     next 函数返回值的次序应依次为: [1,3,2,4,5,6]。
拓展：假如给你 k 个一维向量呢？你的代码在这种情况下的扩展性又会如何呢?

拓展声明：
 “锯齿” 顺序对于 k > 2 的情况定义可能会有些歧义。所以，假如你觉得 “锯齿” 这个表述不妥，也可以认为这是一种 “循环”。例如：

输入:
[1,2,3]
[4,5,6,7]
[8,9]

输出: [1,4,8,2,5,9,3,6,7].

281. Zigzag Iterator
Given two 1d vectors, implement an iterator to return their elements alternately.



Example:

Input:
v1 = [1,2]
v2 = [3,4,5,6]
Output: [1,3,2,4,5,6]
Explanation: By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,3,2,4,5,6].


Follow up:

What if you are given k 1d vectors? How well can your code be extended to such cases?

Clarification for the follow up question:
The "Zigzag" order is not clearly defined and is ambiguous for k > 2 cases. If "Zigzag" does not look right to you, replace "Zigzag" with "Cyclic". For example:

Input:
[1,2,3]
[4,5,6,7]
[8,9]

Output: [1,4,8,2,5,9,3,6,7].
'''


class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        max_num = max(len(v1), len(v2))
        self.vals = []
        for i in range(max_num):
            if i < len(v1):
                self.vals.append(v1[i])
            if i < len(v2):
                self.vals.append(v2[i])




    def next(self):
        """
        :rtype: int
        """
        val = None
        if self.vals:
            val = self.vals.pop(0)
        return val



    def hasNext(self):
        """
        :rtype: bool
        """
        return self.vals != []



# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())


# Golang

'''
type ZigzagIterator struct {
	Vals []int
	Num  int
	Loc  int
}

func Constructor(v1, v2 []int) *ZigzagIterator {

	max_num := len(v2)
	if len(v1) > len(v2) {
		max_num = len(v1)
	}
	z := ZigzagIterator{}
	z.Num = len(v1) + len(v2)
	z.Loc = 0
	for i := 0; i < max_num; i++ {
		if i < len(v1) {
			z.Vals = append(z.Vals, v1[i])
		}

		if i < len(v2) {
			z.Vals = append(z.Vals, v2[i])
		}

	}
	return &z

}

func (this *ZigzagIterator) next() int {
	val := this.Vals[this.Loc]
	this.Loc++

	return val

}

func (this *ZigzagIterator) hasNext() bool {
	res := this.Loc < this.Num
	// fmt.Println(res)
	return res
}

/**
 * Your ZigzagIterator object will be instantiated and called as such:
 * obj := Constructor(param_1, param_2);
 * for obj.hasNext() {
 *	 ans = append(ans, obj.next())
 * }
 */
'''
