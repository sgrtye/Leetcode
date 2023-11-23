# @lcpr-before-debug-begin
from python3problem105 import *
from typing import *

# @lcpr-before-debug-end

#
# @lc app=leetcode id=105 lang=python3
# @lcpr version=30110
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
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
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None

        node = TreeNode(val=preorder[0])
        count = 0
        while inorder[count] != preorder[0]:
            count += 1
        node.left = self.buildTree(preorder[1 : count + 1], inorder[0 : count])
        node.right = self.buildTree(preorder[count + 1 :], inorder[count + 1 :])
        return node
# @lc code=end


#
# @lcpr case=start
# [3,9,20,15,7]\n[9,3,15,20,7]\n
# @lcpr case=end

# @lcpr case=start
# [-1]\n[-1]\n
# @lcpr case=end

#
