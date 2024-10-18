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
        max_area: int = 0
        left: int = 0
        right: int = len(height) - 1

        while left < right:
            max_area = max(max_area, (right - left) * min(height[left], height[right]))

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area


# @lc code=end


#
# @lcpr case=start
# [1,8,6,2,5,4,8,3,7]\n
# @lcpr case=end

# @lcpr case=start
# [1,1]\n
# @lcpr case=end

#
