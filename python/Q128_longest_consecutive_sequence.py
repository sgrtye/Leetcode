#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#


# @lc code=start
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        result: int = 0
        nums_set: set[int] = set(nums)

        for n in nums_set:
            if n - 1 in nums_set:
                continue

            count: int = 1
            while n + count in nums_set:
                count += 1

            result = max(result, count)

        return result


# @lc code=end
