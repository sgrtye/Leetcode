#
# @lc app=leetcode id=152 lang=python3
#
# [152] Maximum Product Subarray
#


# @lc code=start
class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        min_dp: list[int] = [nums[0]] * len(nums)
        max_dp: list[int] = [nums[0]] * len(nums)
        result: int = nums[0]

        for i in range(1, len(nums)):
            number: int = nums[i]

            if number > 0:
                min_dp[i] = min(number, number * min_dp[i - 1])
                max_dp[i] = max(number, number * max_dp[i - 1])
            elif number < 0:
                min_dp[i] = min(number, number * max_dp[i - 1])
                max_dp[i] = max(number, number * min_dp[i - 1])
            else:
                min_dp[i] = 0
                max_dp[i] = 0

            if max_dp[i] > result:
                result = max_dp[i]

        return result


# @lc code=end
