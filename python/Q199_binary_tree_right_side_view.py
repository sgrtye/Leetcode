#
# @lc app=leetcode id=199 lang=python3
#
# [199] Binary Tree Right Side View
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        result: list[int] = []
        current_level: list[TreeNode] = [root]

        while current_level:
            new_level: list[TreeNode] = []
            value: int = 0

            for node in current_level:
                value = node.val

                if node.left:
                    new_level.append(node.left)

                if node.right:
                    new_level.append(node.right)

            result.append(value)
            current_level = new_level

        return result


# @lc code=end
