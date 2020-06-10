'''
面试题 02.05. 链表求和
给定两个用链表表示的整数，每个节点包含一个数位。

这些数位是反向存放的，也就是个位排在链表首部。

编写函数对这两个整数求和，并用链表形式返回结果。



示例：

输入：(7 -> 1 -> 6) + (5 -> 9 -> 2)，即617 + 295
输出：2 -> 1 -> 9，即912
进阶：假设这些数位是正向存放的，请再做一遍。

示例：

输入：(6 -> 1 -> 7) + (2 -> 9 -> 5)，即617 + 295
输出：9 -> 1 -> 2，即912

面试题 02.05. Sum Lists LCCI
You have two numbers represented by a linked list, where each node contains a single digit. The digits are stored in reverse order, such that the 1's digit is at the head of the list. Write a function that adds the two numbers and returns the sum as a linked list.



Example:

Input: (7 -> 1 -> 6) + (5 -> 9 -> 2). That is, 617 + 295.
Output: 2 -> 1 -> 9. That is, 912.
Follow Up: Suppose the digits are stored in forward order. Repeat the above problem.

Example:

Input: (6 -> 1 -> 7) + (2 -> 9 -> 5). That is, 617 + 295.
Output: 9 -> 1 -> 2. That is, 912.
'''

# golang solutions

'''
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {

    res := &ListNode{0, nil}

    dummyNode := res

    pre := 0
    for l1 != nil || l2 != nil || pre != 0{
        num1, num2 := 0, 0
        if l1 != nil{
            num1 = l1.Val
            l1 = l1.Next
        }

        if l2 != nil{
            num2 = l2.Val
            l2 = l2.Next
        }

        sum_ := pre + num1 + num2
        curNum := sum_ % 10
        pre = sum_ / 10

        res.Next = &ListNode{curNum, nil}
        res = res.Next
    }

    return dummyNode.Next
}
'''

# tips

'''
当然，你可以将链表转换为整数，计算总和，然后将其转换回新的链表。如果你在面试中这样做，面试官可能会接受答案，然后看看你在不能将其转换为数字然后返回的情况下，还能否做到这一点。

尝试递归。假设你有两个链表，A = 1 -> 5 -> 9（代表951）和B = 2 -> 3 -> 6 -> 7（代表7632），以及一个操作链表其余部分的函数（5 -> 9和3 -> 6 -> 7）。你能用这个来创建求和方法吗？sum(1 -> 5 -> 9, 2 -> 3 -> 6 -> 7)和sum(5 -> 9, 3 -> 6 -> 7)之间有何关系？

确保你考虑到了链表的长度不同的情况。

你的算法在形如9 -> 7 -> 8和6 -> 8 -> 5的链表上工作吗？仔细检查一下。

对于后续问题：问题是，当链表的长度不一样时，一个链表的首部可能代表1000的位置，而另一个链表代表10的位置。如果你把它们做的一样长呢？有没有方法修改链表来做到这一点，而不改变它所代表的值？
'''