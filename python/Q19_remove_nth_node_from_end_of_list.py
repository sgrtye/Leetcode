#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val: int = val
        self.next: ListNode | None = next


# @lc code=start
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        dummy: ListNode = ListNode(next=head)

        fast: ListNode = dummy
        slow: ListNode = dummy

        for _ in range(n):
            assert fast.next is not None
            fast = fast.next

        while fast and fast.next:
            fast = fast.next

            assert slow.next is not None
            slow = slow.next

        assert slow.next is not None
        slow.next = slow.next.next

        return dummy.next


# @lc code=end
