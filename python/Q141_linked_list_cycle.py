#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x: int) -> None:
        self.val: int = x
        self.next: ListNode | None = None


# @lc code=start
class Solution:
    def hasCycle(self, head: ListNode | None) -> bool:
        if head is None:
            return False

        fast: ListNode | None = head
        slow: ListNode = head

        while fast and fast.next:
            fast = fast.next.next

            assert slow.next is not None
            slow = slow.next

            if fast == slow:
                return True

        return False


# @lc code=end
