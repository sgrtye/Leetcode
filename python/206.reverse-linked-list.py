# @lcpr-before-debug-begin
from python3problem206 import *
from typing import *

# @lcpr-before-debug-end

#
# @lc app=leetcode id=206 lang=python3
# @lcpr version=30109
#
# [206] Reverse Linked List
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
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous = None
        current = head

        while current:
            tmp = current.next
            current.next = previous
            previous = current
            current = tmp

        return previous


# @lc code=end


#
# @lcpr case=start
# [1,2,3,4,5]\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

#
