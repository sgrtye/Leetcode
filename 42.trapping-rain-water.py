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
        left_max = height[0]
        right_max = height[-1]
        water_amount = 0

        l = 0
        r = len(height) - 1
        
        while l < r:
            if left_max <= right_max:
                l += 1
                water_amount += max(left_max - height[l], 0)
                left_max = max(left_max, height[l])
            else:
                r -= 1
                water_amount += max(right_max - height[r], 0)
                right_max = max(right_max, height[r])

        return water_amount

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

