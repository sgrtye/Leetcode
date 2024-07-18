# @lcpr-before-debug-begin
from python3problem1609 import *
from typing import *

# @lcpr-before-debug-end

#
# @lc app=leetcode id=1609 lang=python3
# @lcpr version=30204
#
# [1609] Even Odd Tree
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
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        even_level = True
        current_level = [root]

        while current_level:
            next_level = []
            previous_value = None

            for n in current_level:
                if (n.val % 2 == 1) ^ even_level:
                    return False

                if n.left:
                    next_level.append(n.left)

                if n.right:
                    next_level.append(n.right)

                if previous_value is None:
                    previous_value = n.val
                    continue

                if ((n.val > previous_value) ^ even_level) or (
                    (n.val < previous_value) ^ (not even_level)
                ):
                    return False

                previous_value = n.val

            even_level = not even_level
            current_level = next_level

        return True


# @lc code=end


# @lcpr-div-debug-arg-start
# funName=isEvenOddTree
# paramTypes= ["number[]"]
# @lcpr-div-debug-arg-end


#
# @lcpr case=start
# [1,10,4,3,null,7,9,12,8,6,null,null,2]\n
# @lcpr case=end

# @lcpr case=start
# [5,4,2,3,3,7]\n
# @lcpr case=end

# @lcpr case=start
# [5,9,1,3,5,7]\n
# @lcpr case=end

# @lcpr case=start
# [13,34,32,23,25,27,29,44,40,36,34,30,30,28,26,3,7,9,11,15,17,21,25,null,null,27,31,35,null,37,null,30,null,26,null,null,null,24,null,20,16,12,10,null,null,8,null,null,null,null,null,6,null,null,null,null,null,15,19,null,null,null,null,23,null,27,29,33,37,null,null,null,null,null,null,48,null,null,null,46,null,null,null,42,38,34,32,null,null,null,null,19]\n
# @lcpr case=end

#
