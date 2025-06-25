#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val: int = val
        self.left: TreeNode | None = left
        self.right: TreeNode | None = right


# @lc code=start
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if not root:
            return []

        result: list[list[int]] = []
        current_level: list[TreeNode] = [root]

        while current_level:
            new_level: list[TreeNode] = []
            values: list[int] = []

            for node in current_level:
                values.append(node.val)

                if node.left:
                    new_level.append(node.left)

                if node.right:
                    new_level.append(node.right)

            result.append(values)
            current_level = new_level

        return result


# @lc code=end
