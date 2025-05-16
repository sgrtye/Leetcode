#
# @lc app=leetcode id=105 lang=python3
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def build_tree(self, limit: int) -> TreeNode:
        if self.pre_index >= len(self.preorder):
            return None

        if self.inorder[self.in_index] == limit:
            self.in_index += 1
            return None

        value: int = self.preorder[self.pre_index]

        new_node: TreeNode = TreeNode(value)
        self.pre_index += 1

        new_node.left = self.build_tree(value)
        new_node.right = self.build_tree(limit)

        return new_node

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.preorder: list[int] = preorder
        self.inorder: list[int] = inorder

        self.pre_index: int = 0
        self.in_index: int = 0

        return self.build_tree(3001)


# @lc code=end
