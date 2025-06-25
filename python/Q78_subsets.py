#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#


# @lc code=start
class Solution:
    def backtrack(self, index: int, subset: list[int]) -> None:
        if index == self.length:
            self.result.append(subset.copy())
            return

        subset.append(self.nums[index])
        self.backtrack(index + 1, subset)

        subset.pop()
        self.backtrack(index + 1, subset)

    def subsets(self, nums: list[int]) -> list[list[int]]:
        self.nums: list[int] = nums
        self.length: int = len(nums)
        self.result: list[list[int]] = []

        self.backtrack(0, [])

        return self.result


# @lc code=end
