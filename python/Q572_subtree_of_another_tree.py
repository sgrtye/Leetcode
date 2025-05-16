#
# @lc app=leetcode id=572 lang=python3
#
# [572] Subtree of Another Tree
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def same_tree(self, root: TreeNode | None, other: TreeNode | None) -> bool:
        if not root and not other:
            return True

        if not root or not other or root.val != other.val:
            return False

        left_match: bool = self.same_tree(root.left, other.left)
        right_match: bool = self.same_tree(root.right, other.right)
        return left_match and right_match

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None:
            return False

        if self.same_tree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


# @lc code=end
