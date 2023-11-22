#
# @lc app=leetcode id=543 lang=python3
# @lcpr version=30110
#
# [543] Diameter of Binary Tree
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfSubTree(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        left = self.diameterOfSubTree(root.left)
        right = self.diameterOfSubTree(root.right)
        self.max = max(self.max, left + right)
        return max(left, right) + 1
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max = 0
        self.diameterOfSubTree(root)
        return self.max
# @lc code=end



#
# @lcpr case=start
# [1,2,3,4,5]\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n
# @lcpr case=end

#

