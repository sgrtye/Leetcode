#
# @lc app=leetcode id=704 lang=python3
#
# [704] Binary Search
#


# @lc code=start
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left: int = 0
        right: int = len(nums) - 1

        while left <= right:
            m: int = left + ((right - left) // 2)
            number: int = nums[m]

            if number < target:
                left = m + 1
            elif number > target:
                right = m - 1
            else:
                return m

        return -1


# @lc code=end
