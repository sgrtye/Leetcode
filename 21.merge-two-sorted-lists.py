# @lcpr-before-debug-begin
from python3problem21 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode id=21 lang=python3
# @lcpr version=30109
#
# [21] Merge Two Sorted Lists
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = current = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next

            current = current.next
            
        if list1 is not None:
            current.next = list1
            
        if list2 is not None:
            current.next = list2
            
        return res.next
        
# @lc code=end



#
# @lcpr case=start
# [1,2,4]\n[1,3,4]\n
# @lcpr case=end

# @lcpr case=start
# []\n[]\n
# @lcpr case=end

# @lcpr case=start
# []\n[0]\n
# @lcpr case=end

#

