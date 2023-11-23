# @lcpr-before-debug-begin
from python3problem98 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode id=98 lang=python3
# @lcpr version=30110
#
# [98] Validate Binary Search Tree
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
    def inOrder(self, node: Optional[TreeNode]) -> bool:
        if node.left:
            if not self.inOrder(node.left):
                return False
        
        if self.list:
            if node.val <= self.list[-1]:
                return False
        
        self.list.append(node.val)

        if node.right:
            if not self.inOrder(node.right):
                return False

        return True
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        self.list = []
        return self.inOrder(root)

# @lc code=end


#
# @lcpr case=start
# [2,1,3]\n
# @lcpr case=end

# @lcpr case=start
# [5,1,4,null,null,3,6]\n
# @lcpr case=end

# @lcpr case=start
# [2,2,2]\n
# @lcpr case=end

# @lcpr case=start
# [5,4,6,null,null,3,7]\n
# @lcpr case=end

#
