# @lcpr-before-debug-begin
from python3problem25 import *
from typing import *

# @lcpr-before-debug-end

#
# @lc app=leetcode id=25 lang=python3
# @lcpr version=30110
#
# [25] Reverse Nodes in k-Group
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
    def longerThanK(self, node: Optional[ListNode], k: int) -> bool:
        for _ in range(k):
            if not node:
                return False
            node = node.next

        return True

    def reverse(
        self, node: Optional[ListNode], k: int
    ) -> (Optional[ListNode], Optional[ListNode]):
        prev = None
        curr = node

        for _ in range(k):
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        node.next = curr

        return prev, node

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = previous = ListNode()
        current = head
        previous.next = current

        while self.longerThanK(current, k):
            new_head, new_tail = self.reverse(current, k)
            previous.next = new_head
            previous = new_tail
            current = new_tail.next

        return dummy.next


# @lc code=end


#
# @lcpr case=start
# [1,2,3,4,5]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,5]\n3\n
# @lcpr case=end

#
