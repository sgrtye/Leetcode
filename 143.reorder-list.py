# @lcpr-before-debug-begin
from python3problem143 import *
from typing import *

# @lcpr-before-debug-end

#
# @lc app=leetcode id=143 lang=python3
# @lcpr version=30110
#
# [143] Reorder List
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = head
        fast = head.next

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        previous = None
        current = slow.next
        slow.next = None

        while current:
            temp = current.next
            current.next = previous
            previous = current
            current = temp

        first_half = head
        second_half = previous
        current = ListNode()

        while first_half and second_half:
            current.next = first_half
            first_half = first_half.next
            current = current.next
            current.next = second_half
            second_half = second_half.next
            current = current.next

        if first_half:
            current.next = first_half


# @lc code=end


#
# @lcpr case=start
# [1,2,3,4]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,5]\n
# @lcpr case=end

#
