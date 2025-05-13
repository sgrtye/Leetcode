#
# @lc app=leetcode id=704 lang=python3
#
# [704] Binary Search
#


# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l: int = 0
        r: int = len(nums) - 1

        while l <= r:
            m: int = l + ((r - l) // 2)
            number: int = nums[m]

            if number < target:
                l = m + 1
            elif number > target:
                r = m - 1
            else:
                return m

        return -1


# @lc code=end
