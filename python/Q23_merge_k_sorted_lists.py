#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeList(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        dummy: ListNode = ListNode()
        current: ListNode = dummy

        while l1 and l2:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next

            current = current.next

        if l1:
            current.next = l1

        if l2:
            current.next = l2

        return dummy.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        while len(lists) > 1:
            new_list: list[ListNode | None] = []

            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                new_list.append(self.mergeList(l1, l2))

            lists = new_list

        return lists[0] if lists else None


# @lc code=end
