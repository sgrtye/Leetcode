#
# @lc app=leetcode id=230 lang=python3
#
# [230] Kth Smallest Element in a BST
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder_with_max(self, root: TreeNode, k: int) -> None:
        if len(self.values) >= k:
            return

        if root.left:
            self.inorder_with_max(root.left, k)

        self.values.append(root.val)

        if root.right:
            self.inorder_with_max(root.right, k)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.values: list[int] = []
        self.inorder_with_max(root, k)
        return self.values[k - 1]


# @lc code=end
