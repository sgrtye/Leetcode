#
# @lc app=leetcode id=143 lang=python3
#
# [143] Reorder List
#


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val: int = val
        self.next: ListNode | None = next


# @lc code=start
class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head is None or head.next is None:
            return

        fast: ListNode | None = head
        slow: ListNode = head

        while fast and fast.next:
            fast = fast.next.next

            assert slow.next is not None
            slow = slow.next

        previous: ListNode | None = None
        current: ListNode | None = slow

        while current:
            tmp: ListNode | None = current.next
            current.next = previous
            previous = current
            current = tmp

        first_half: ListNode = head
        assert previous is not None
        second_half: ListNode = previous

        while True:
            tmp1: ListNode | None = first_half.next
            tmp2: ListNode | None = second_half.next

            first_half.next = second_half
            if tmp1 == slow:
                break
            second_half.next = tmp1

            assert tmp1 is not None
            assert tmp2 is not None

            first_half = tmp1
            second_half = tmp2


# @lc code=end
