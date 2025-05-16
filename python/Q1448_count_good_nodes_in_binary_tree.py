#
# @lc app=leetcode id=1448 lang=python3
#
# [1448] Count Good Nodes in Binary Tree
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
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
