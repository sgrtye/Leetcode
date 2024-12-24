#
# @lc app=leetcode id=102 lang=python3
# @lcpr version=30110
#
# [102] Binary Tree Level Order Traversal
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
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        current = [root]

        while current:
            new_list = []
            level_result = []
            for node in current:
                if node.left:
                    new_list.append(node.left)
                if node.right:
                    new_list.append(node.right)
                level_result.append(node.val)
            current = new_list
            res.append(level_result)

        return res


# @lc code=end


#
# @lcpr case=start
# [3,9,20,null,null,15,7]\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

#
