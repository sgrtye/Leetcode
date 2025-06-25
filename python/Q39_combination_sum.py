#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#


# @lc code=start
class Solution:
    def backtrack(self, index: int, current_sum: int, stack: list[int]) -> None:
        if current_sum == self.target:
            self.result.append(stack.copy())
            return

        if current_sum > self.target or index == self.length:
            return

        value: int = self.candidates[index]

        stack.append(value)
        self.backtrack(index, current_sum + value, stack)

        stack.pop()
        self.backtrack(index + 1, current_sum, stack)

    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        self.target: int = target
        self.length: int = len(candidates)
        self.candidates: list[int] = candidates

        self.result: list[list[int]] = []

        self.backtrack(0, 0, [])

        return self.result


# @lc code=end
