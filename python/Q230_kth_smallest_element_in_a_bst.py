#
# @lc app=leetcode id=230 lang=python3
#
# [230] Kth Smallest Element in a BST
#


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val: int = val
        self.left: TreeNode | None = left
        self.right: TreeNode | None = right


# @lc code=start
class Solution:
    def inorder_with_max(self, root: TreeNode, k: int) -> None:
        if len(self.values) >= k:
            return

        if root.left:
            self.inorder_with_max(root.left, k)

        self.values.append(root.val)

        if root.right:
            self.inorder_with_max(root.right, k)

    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        self.values: list[int] = []

        assert root is not None
        self.inorder_with_max(root, k)

        return self.values[k - 1]


# @lc code=end
