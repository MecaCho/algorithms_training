# encoding=utf8

'''
23. 合并K个排序链表
合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。

示例:

输入:
[
  1->4->5,
  1->3->4,
  2->6
]
输出: 1->1->2->3->4->4->5->6

23. Merge k Sorted Lists
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
'''



# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None



class Solution(object):
    def merge_two(self, list1, list2):
        new_list = ListNode(0)
        res = new_list
        # head = list1
        while list1 or list2:
            if list1 and list2:
                if list1.val < list2.val:
                    new_node = ListNode(list1.val)
                    new_list.next = new_node
                    new_list = new_list.next
                    list1 = list1.next
                else:
                    new_node = ListNode(list2.val)
                    new_list.next = new_node
                    new_list = new_list.next
                    list2 = list2.next
            if not list1:
                new_list.next = list2
                break
            if not list2:
                new_list.next = list1
                break

        return res.next

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return
        if len(lists) == 1:
            return lists[0]
        merge_t = [self.merge_two(lists.pop(), lists.pop())]
        # print(merge_t)
        return self.mergeKLists(merge_t + lists)







# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


def quick_sort(arr):
    if arr:
        left_arr = [node for node in arr if node.val < arr[0].val]
        mid_arr = [node for node in arr if node.val == arr[0].val]
        right_arr = [node for node in arr if node.val > arr[0].val]
        return quick_sort(left_arr) + mid_arr + quick_sort(right_arr)
    return []


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        all_nodes = []
        for node_list in lists:
            node = node_list
            while node is not None:
                all_nodes.append(node)
                node = node.next
        all_nodes = quick_sort(all_nodes)
        for i in range(len(all_nodes) - 1):
            all_nodes[i].next = all_nodes[i + 1]
        if all_nodes:
            return all_nodes[0]
        else:
            return None
