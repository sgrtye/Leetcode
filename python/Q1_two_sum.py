#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#


# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result: dict[int, int] = dict()

        for i, n in enumerate(nums):
            if n in result:
                return [i, result[n]]

            result[target - n] = i


# @lc code=end
