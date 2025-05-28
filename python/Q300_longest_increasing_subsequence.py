#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#

# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp: list[int] = [1] * len(nums)
        result: int = 1

        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i] and (new_value := dp[j] + 1) > dp[i]:
                    dp[i] = new_value

                    if new_value > result:
                        result = new_value

        return result


# @lc code=end
