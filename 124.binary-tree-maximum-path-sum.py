#
# @lc app=leetcode id=124 lang=python3
# @lcpr version=30110
#
# [124] Binary Tree Maximum Path Sum
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
    def findMax(self, node: Optional[TreeNode]) -> int:
        if not node: return 0

        left = self.findMax(node.left)
        right = self.findMax(node.right)
        current_max = max(node.val, left + node.val, right + node.val)
        self.max = max(self.max, max(current_max, left + right + node.val))
        return current_max
    
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max = float('-inf')
        self.findMax(root)
        return self.max
# @lc code=end



#
# @lcpr case=start
# [1,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [-10,9,20,null,null,15,7]\n
# @lcpr case=end

# @lcpr case=start
# [-3]\n
# @lcpr case=end

# @lcpr case=start
# [2,-1]\n
# @lcpr case=end

# @lcpr case=start
# [1,-2,3]\n
# @lcpr case=end

# @lcpr case=start
# [5,4,8,11,null,13,4,7,2,null,null,null,1]
# @lcpr case=end
#

