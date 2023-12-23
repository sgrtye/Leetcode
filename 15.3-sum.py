# @lcpr-before-debug-begin
from python3problem15 import *
from typing import *

# @lcpr-before-debug-end

#
# @lc app=leetcode id=15 lang=python3
# @lcpr version=30106
#
# [15] 3Sum
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        new_nums = sorted(nums)
        result = []

        for i in range(len(new_nums)):
            if i != 0 and new_nums[i] == new_nums[i - 1]:
                continue

            l = i + 1
            r = len(new_nums) - 1

            while l < r:
                three_sum = new_nums[i] + new_nums[l] + new_nums[r]

                if three_sum > 0:
                    r -= 1
                elif three_sum < 0:
                    l += 1
                else:
                    result.append([new_nums[i], new_nums[l], new_nums[r]])
                    l += 1
                    while new_nums[l] == new_nums[l - 1] and l < r:
                        l += 1

            i += 1

        return result


# @lc code=end


#
# @lcpr case=start
# [-1,0,1,2,-1,-4]\n
# @lcpr case=end

# @lcpr case=start
# [0,1,1]\n
# @lcpr case=end

# @lcpr case=start
# [0,0,0]\n
# @lcpr case=end

#
