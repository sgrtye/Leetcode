#
# @lc app=leetcode id=90 lang=python3
#
# [90] Subsets II
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

        while index + 1 < self.length and self.nums[index] == self.nums[index + 1]:
            index += 1
        self.backtrack(index + 1, subset)

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.nums: list[int] = nums
        self.nums.sort()

        self.length: int = len(nums)
        self.result: list[list[int]] = []

        self.backtrack(0, [])

        return self.result


# @lc code=end
