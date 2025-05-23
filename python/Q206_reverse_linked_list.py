#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous: ListNode | None = None
        current: ListNode | None = head

        while current:
            tmp: ListNode | None = current.next
            current.next = previous
            previous = current
            current = tmp

        return previous


# @lc code=end
