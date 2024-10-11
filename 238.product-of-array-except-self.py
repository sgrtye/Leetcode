# @lcpr-before-debug-begin
from python3problem238 import *
from typing import *

# @lcpr-before-debug-end

#
# @lc app=leetcode id=238 lang=python3
# @lcpr version=30105
#
# [238] Product of Array Except Self
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix: list[int] = [1] * (len(nums) + 1)
        for i in range(len(nums)):
            prefix[i] = prefix[i - 1] * nums[i]

        suffix: list[int] = [1] * (len(nums) + 1)
        for i in range(len(nums) - 1, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i]

        return [prefix[i - 1] * suffix[i + 1] for i in range(len(nums))]


# @lc code=end


#
# @lcpr case=start
# [1,2,3,4]\n
# @lcpr case=end

# @lcpr case=start
# [-1,1,0,-3,3]\n
# @lcpr case=end

#
