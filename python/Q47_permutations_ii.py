#
# @lc app=leetcode id=47 lang=python3
#
# [47] Permutations II
#


# @lc code=start
class Solution:
    def backtrack(
        self, remaining: dict[int, int], stack: list[int], length: int
    ) -> None:
        if length == self.length:
            self.result.append(stack.copy())

        for n, c in remaining.items():
            if c > 0:
                remaining[n] -= 1
                stack.append(n)

                self.backtrack(remaining, stack, length + 1)

                stack.pop()
                remaining[n] += 1

    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        self.result: list[list[int]] = []

        self.nums: list[int] = nums
        self.length: int = len(nums)

        remaining: dict[int, int] = dict()
        for n in nums:
            remaining[n] = remaining.get(n, 0) + 1

        self.backtrack(remaining, [], 0)

        return self.result


# @lc code=end
