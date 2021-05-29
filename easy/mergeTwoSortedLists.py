'''

https://leetcode.com/problems/merge-two-sorted-lists/
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        print(l1.__class__)
        print(l2)
        return ListNode()


obj = Solution()
list1 = [1, 2, 4]
list2 = [1, 3, 4]
l1 = ListNode()
l2 = ListNode()
# print(obj.mergeTwoLists([1, 2, 4], [1, 3, 4]))
print(obj.mergeTwoLists(l1, l2))
