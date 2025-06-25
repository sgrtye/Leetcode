#
# @lc app=leetcode id=124 lang=python3
#
# [124] Binary Tree Maximum Path Sum
#


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val: int = val
        self.left: TreeNode | None = left
        self.right: TreeNode | None = right


# @lc code=start
class Solution:
    def max_path(self, root: TreeNode | None) -> tuple[int, int]:
        if not root:
            return 0, -3 * 10**7

        left_connected, left_max = self.max_path(root.left)
        right_connected, right_max = self.max_path(root.right)

        left_updated: int = left_connected if left_connected > 0 else 0
        right_updated: int = right_connected if right_connected > 0 else 0

        connected_max: int = (
            left_updated if left_updated > right_updated else right_updated
        )

        connected_max += root.val

        previous_path: int = left_max if left_max > right_max else right_max
        current_path: int = left_updated + root.val + right_updated
        max_path: int = previous_path if previous_path > current_path else current_path

        return connected_max, max_path

    def maxPathSum(self, root: TreeNode | None) -> int:
        return self.max_path(root)[1]


# @lc code=end
