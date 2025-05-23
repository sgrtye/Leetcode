#
# @lc app=leetcode id=543 lang=python3
#
# [543] Diameter of Binary Tree
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def depth_and_diameter_of_subtree(self, root: TreeNode | None) -> tuple[int, int]:
        if not root:
            return 0, 0

        left_depth, left_diameter = self.depth_and_diameter_of_subtree(root.left)
        right_depth, right_diameter = self.depth_and_diameter_of_subtree(root.right)

        max_depth: int = left_depth if left_depth > right_depth else right_depth
        max_depth += 1

        max_diameter: int = max(left_diameter, right_diameter, left_depth + right_depth)

        return max_depth, max_diameter

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        return self.depth_and_diameter_of_subtree(root)[1]


# @lc code=end
