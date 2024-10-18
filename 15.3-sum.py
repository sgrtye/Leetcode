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
        previous: int | None = None
        result: list[list[int]] = []

        for i in range(len(nums) - 2):
            if nums[i] == previous:
                continue
            previous = nums[i]

            left: int = i + 1
            right: int = len(nums) - 1

            while left < right:
                total: int = nums[i] + nums[left] + nums[right]
                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

                elif total < 0:
                    left += 1

                else:
                    right -= 1

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
