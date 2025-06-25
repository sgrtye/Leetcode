#
# @lc app=leetcode id=572 lang=python3
#
# [572] Subtree of Another Tree
#


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val: int = val
        self.left: TreeNode | None = left
        self.right: TreeNode | None = right


# @lc code=start
class Solution:
    def same_tree(self, root: TreeNode | None, other: TreeNode | None) -> bool:
        if not root and not other:
            return True

        if not root or not other or root.val != other.val:
            return False

        left_match: bool = self.same_tree(root.left, other.left)
        right_match: bool = self.same_tree(root.right, other.right)
        return left_match and right_match

    def isSubtree(self, root: TreeNode | None, subRoot: TreeNode | None) -> bool:
        if root is None:
            return False

        if self.same_tree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


# @lc code=end
