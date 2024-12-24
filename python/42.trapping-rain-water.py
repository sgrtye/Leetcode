# @lcpr-before-debug-begin
from python3problem42 import *
from typing import *

# @lcpr-before-debug-end

#
# @lc app=leetcode id=42 lang=python3
# @lcpr version=30106
#
# [42] Trapping Rain Water
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        left_height: int = 0
        right_height: int = 0
        left: int = 0
        right: int = len(height) - 1
        water: int = 0

        while left <= right:
            if left_height < right_height:
                water += max(min(left_height, right_height) - height[left], 0)
                left_height = max(left_height, height[left])
                left += 1
            else:
                water += max(min(left_height, right_height) - height[right], 0)
                right_height = max(right_height, height[right])
                right -= 1

        return water


# @lc code=end


#
# @lcpr case=start
# [0,1,0,2,1,0,1,3,2,1,2,1]\n
# @lcpr case=end

# @lcpr case=start
# [4,2,0,3,2,5]\n
# @lcpr case=end

# @lcpr case=start
# [5,5,1,7,1,1,5,2,7,6]\n
# @lcpr case=end

# @lcpr case=start
# [4]\n
# @lcpr case=end

#
