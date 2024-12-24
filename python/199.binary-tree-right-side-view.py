#
# @lc app=leetcode id=199 lang=python3
# @lcpr version=30110
#
# [199] Binary Tree Right Side View
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
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        current = [root]

        while current:
            new_list = []
            for node in current:
                if node.left:
                    new_list.append(node.left)
                if node.right:
                    new_list.append(node.right)
                level_result = node.val
            current = new_list
            res.append(level_result)

        return res


# @lc code=end


#
# @lcpr case=start
# [1,2,3,null,5,null,4]\n
# @lcpr case=end

# @lcpr case=start
# [1,null,3]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

#
