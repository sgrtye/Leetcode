#
# @lc app=leetcode id=1448 lang=python3
# @lcpr version=30110
#
# [1448] Count Good Nodes in Binary Tree
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
    def helper(self, node: TreeNode, max_number: int) -> None:
        if node.val >= max_number:
            self.good += 1

        current_amx = max(max_number, node.val)

        if node.left:
            self.helper(node.left, current_amx)
        if node.right:
            self.helper(node.right, current_amx)

    def goodNodes(self, root: TreeNode) -> int:
        self.good = 0
        self.helper(root, root.val)
        return self.good


# @lc code=end


#
# @lcpr case=start
# [3,1,4,3,null,1,5]\n
# @lcpr case=end

# @lcpr case=start
# [3,3,null,4,2]\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

#
