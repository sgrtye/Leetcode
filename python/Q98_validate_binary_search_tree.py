#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def check_valid(self, root: TreeNode | None, minimum: int, maximum: int) -> bool:
        if not root:
            return True

        if not (minimum < root.val < maximum):
            return False

        left_valid: bool = self.check_valid(root.left, minimum, root.val)
        right_valid: bool = self.check_valid(root.right, root.val, maximum)

        return left_valid and right_valid

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.check_valid(root, -(2**31) - 1, 2**31)


# @lc code=end
