# @lcpr-before-debug-begin
from python3problem138 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode id=138 lang=python3
# @lcpr version=30110
#
# [138] Copy List with Random Pointer
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start

# Definition for a Node.
# class Node:
#     def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
#         self.val = int(x)
#         self.next = next
#         self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        res = Node(0)

        # Create all the copied nodes, then link both links together
        copied_head = res
        while head:
            new = Node(head.val, random = head)

            copied_head.next = new
            copied_head = copied_head.next

            tmp = head.next
            head.next = new
            head = tmp
        
        # Correct the copied version by adding the correct random field and removing all the original nodes
        copied_head = res.next
        while copied_head:
            if copied_head.random.random:
                copied_head.random = copied_head.random.random.next
            else:
                copied_head.random = None
            copied_head = copied_head.next
        
        return res.next
# @lc code=end



#
# @lcpr case=start
# [[7,null],[13,0],[11,4],[10,2],[1,0]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,1],[2,1]]\n
# @lcpr case=end

# @lcpr case=start
# [[3,null],[3,0],[3,null]]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

#

