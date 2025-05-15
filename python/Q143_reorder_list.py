#
# @lc app=leetcode id=143 lang=python3
#
# [143] Reorder List
#


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
        if head is None or head.next is None:
            return

        fast: ListNode = head
        slow: ListNode = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        previous: ListNode | None = None
        current: ListNode | None = slow

        while current:
            tmp: ListNode | None = current.next
            current.next = previous
            previous = current
            current = tmp

        first_half: ListNode = head
        second_half: ListNode = previous

        while True:
            tmp1: ListNode = first_half.next
            tmp2: ListNode = second_half.next

            first_half.next = second_half
            if tmp1 == slow:
                break
            second_half.next = tmp1

            first_half = tmp1
            second_half = tmp2


# @lc code=end
