#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val: int = val
        self.left: TreeNode | None = left
        self.right: TreeNode | None = right


# @lc code=start
class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        if not root:
            return 0

        result: int = 0

        if (depth := self.maxDepth(root.left)) > result:
            result = depth

        if (depth := self.maxDepth(root.right)) > result:
            result = depth

        return result + 1


# @lc code=end
