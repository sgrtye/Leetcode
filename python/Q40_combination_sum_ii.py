#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
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
        self.backtrack(index + 1, current_sum + value, stack)

        stack.pop()
        while index + 1 < self.length and self.candidates[index + 1] == value:
            index += 1
        self.backtrack(index + 1, current_sum, stack)

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.target: int = target
        self.length: int = len(candidates)
        self.candidates: list[int] = candidates

        candidates.sort()

        self.result: list[list[int]] = []

        self.backtrack(0, 0, [])

        return self.result


# @lc code=end
