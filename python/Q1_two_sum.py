#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#


# @lc code=start
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        mapping: dict[int, int] = dict()

        for i, n in enumerate(nums):
            if n in mapping:
                return [i, mapping[n]]

            mapping[target - n] = i

        return []


# @lc code=end
