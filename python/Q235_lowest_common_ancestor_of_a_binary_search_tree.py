#
# @lc app=leetcode id=235 lang=python3
#
# [235] Lowest Common Ancestor of a Binary Search Tree
#


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x: int) -> None:
        self.val: int = x
        self.left: TreeNode | None = None
        self.right: TreeNode | None = None


# @lc code=start
class Solution:
    def lowestCommonAncestor(
        self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> TreeNode:
        if root.val > p.val and root.val > q.val:
            assert root.left is not None
            return self.lowestCommonAncestor(root.left, p, q)

        if root.val < p.val and root.val < q.val:
            assert root.right is not None
            return self.lowestCommonAncestor(root.right, p, q)

        return root


# @lc code=end
