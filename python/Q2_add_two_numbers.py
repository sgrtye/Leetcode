#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val: int = val
        self.next: ListNode | None = next


# @lc code=start
class Solution:
    def addTwoNumbers(
        self, l1: ListNode | None, l2: ListNode | None
    ) -> ListNode | None:
        carry: bool = False
        dummy: ListNode = ListNode(0)
        current: ListNode = dummy

        while l1 or l2 or carry:
            total: int = 0

            if l1:
                total += l1.val
                l1 = l1.next

            if l2:
                total += l2.val
                l2 = l2.next

            if carry:
                total += 1
                carry = False

            carry = total >= 10

            new_node: ListNode = ListNode(total % 10)
            current.next = new_node
            current = new_node

        return dummy.next


# @lc code=end
