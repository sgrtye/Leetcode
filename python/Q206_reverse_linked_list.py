#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val: int = val
        self.next: ListNode | None = next


# @lc code=start
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        previous: ListNode | None = None
        current: ListNode | None = head

        while current:
            tmp: ListNode | None = current.next
            current.next = previous
            previous = current
            current = tmp

        return previous


# @lc code=end
