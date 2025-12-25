#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#


# @lc code=start
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen: set[int] = set()

        for n in nums:
            if n in seen:
                return True

            seen.add(n)

        return False


# @lc code=end
