#
# @lc app=leetcode id=1448 lang=python3
#
# [1448] Count Good Nodes in Binary Tree
#


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val: int = val
        self.left: TreeNode | None = left
        self.right: TreeNode | None = right


# @lc code=start
class Solution:
    def good_nodes(self, root: TreeNode, maximum: int) -> int:
        result: int = 0
        maximum_value: int = maximum if maximum > root.val else root.val

        if root.left:
            result += self.good_nodes(root.left, maximum_value)

        if root.right:
            result += self.good_nodes(root.right, maximum_value)

        if root.val >= maximum:
            result += 1

        return result

    def goodNodes(self, root: TreeNode) -> int:
        return self.good_nodes(root, -(10**4) - 1)


# @lc code=end
