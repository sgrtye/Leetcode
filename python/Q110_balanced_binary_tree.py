#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val: int = val
        self.left: TreeNode | None = left
        self.right: TreeNode | None = right


# @lc code=start
class Solution:
    def is_balanced(self, root: TreeNode | None) -> tuple[int, bool]:
        if not root:
            return 0, True

        left_depth, left_balanced = self.is_balanced(root.left)
        if not left_balanced:
            return -1, False
        right_depth, right_balanced = self.is_balanced(root.right)
        if not right_balanced:
            return -1, False

        depth: int = left_depth if left_depth > right_depth else right_depth
        depth += 1

        return depth, abs(left_depth - right_depth) < 2

    def isBalanced(self, root: TreeNode | None) -> bool:
        return self.is_balanced(root)[1]


# @lc code=end
