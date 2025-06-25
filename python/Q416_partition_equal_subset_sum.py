#
# @lc app=leetcode id=416 lang=python3
#
# [416] Partition Equal Subset Sum
#


# @lc code=start
class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        target: int = sum(nums)
        if target % 2 == 1:
            return False

        target = target // 2

        dp: list[list[bool]] = [[False] * (target + 1) for _ in range(len(nums) + 1)]
        for i in range(len(nums) + 1):
            dp[i][0] = True

        for i in range(1, len(nums) + 1):
            element: int = nums[i - 1]

            for j in range(1, target + 1):
                dp[i][j] |= dp[i - 1][j]

                if j >= element:
                    dp[i][j] |= dp[i - 1][j - element]

        return dp[-1][-1]


# @lc code=end
