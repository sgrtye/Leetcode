# @lcpr-before-debug-begin
from python3problem230 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode id=230 lang=python3
# @lcpr version=30110
#
# [230] Kth Smallest Element in a BST
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inOrder(self, node: Optional[TreeNode], k: int) -> None:
        if len(self.list) > k:
            return
        
        if node.left:
            self.inOrder(node.left, k)
        
        self.list.append(node.val)

        if node.right:
            self.inOrder(node.right, k)

    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.list = []
        self.inOrder(root, k)
        return self.list[k - 1]
        
# @lc code=end



#
# @lcpr case=start
# [3,1,4,null,2]\n1\n
# @lcpr case=end

# @lcpr case=start
# [5,3,6,2,4,null,null,1]\n3\n
# @lcpr case=end

#

