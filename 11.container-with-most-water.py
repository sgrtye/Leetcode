# @lcpr-before-debug-begin
from python3problem11 import *
from typing import *

# @lcpr-before-debug-end

#
# @lc app=leetcode id=11 lang=python3
# @lcpr version=30106
#
# [11] Container With Most Water
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_amount = 0
        l, r = 0, len(height) - 1

        while l < r:
            max_amount = max(max_amount, min(height[l], height[r]) * (r - l))

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return max_amount


# @lc code=end


#
# @lcpr case=start
# [1,8,6,2,5,4,8,3,7]\n
# @lcpr case=end

# @lcpr case=start
# [1,1]\n
# @lcpr case=end

#
