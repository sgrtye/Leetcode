#
# @lc app=leetcode id=494 lang=python3
#
# [494] Target Sum
#


# @lc code=start
class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        dp: list[dict[int, int]] = [dict() for _ in range(len(nums) + 1)]
        dp[0][0] = 1

        for i in range(1, len(nums) + 1):
            num: int = nums[i - 1]

            for total, count in dp[i - 1].items():
                dp[i][total + num] = dp[i].get(total + num, 0) + count
                dp[i][total - num] = dp[i].get(total - num, 0) + count

        return dp[-1].get(target, 0)


# @lc code=end
