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
        left_max = [0] * len(height)
        right_max = [0] * (len(height) + 1)
        water_amount = [0] * len(height)

        for i in range(len(height)):
            left_max[i] = max(left_max[i - 1], height[i])
        
        for i in range(len(height) - 1, -1, -1):
            right_max[i] = max(right_max[i + 1], height[i])
        
        for i in range(1, len(height) - 1):
            water_amount[i] = max(min(left_max[i - 1], right_max[i + 1]) - height[i], 0)
        
        return sum(water_amount)

# @lc code=end



#
# @lcpr case=start
# [0,1,0,2,1,0,1,3,2,1,2,1]\n
# @lcpr case=end

# @lcpr case=start
# [4,2,0,3,2,5]\n
# @lcpr case=end

#

