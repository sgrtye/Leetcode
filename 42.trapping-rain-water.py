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
        if not height:
            return 0

        l, r = 0, len(height) - 1
        left_max, right_max = 0, 0
        water = 0

        while l <= r:
            if left_max < right_max:
                water += max(0, min(left_max, right_max) - height[l])
                left_max = max(left_max, height[l])
                l += 1
            else:
                water += max(0, min(left_max, right_max) - height[r])
                right_max = max(right_max, height[r])
                r -= 1

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

#
