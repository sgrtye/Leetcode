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
        nums.sort()

        result = []
        previous = None

        for i, n in enumerate(nums):
            tmp = previous
            previous = n
            if n == tmp:
                continue

            l, r = i + 1, len(nums) - 1

            while l < r:
                if nums[l] + nums[r] < -n:
                    l += 1
                elif nums[l] + nums[r] > -n:
                    r -= 1
                else:
                    result.append([n, nums[l], nums[r]])

                    left_number = nums[l]
                    while l < r and nums[l] == left_number:
                        l += 1

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
