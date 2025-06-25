#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#


# @lc code=start
class Solution:
    def backtrack(self, remaining: set[int], stack: list[int]) -> None:
        if not remaining:
            self.result.append(stack.copy())

        for n in remaining.copy():
            stack.append(n)
            remaining.remove(n)
            self.backtrack(remaining, stack)
            remaining.add(n)
            stack.pop()

    def permute(self, nums: list[int]) -> list[list[int]]:
        self.result: list[list[int]] = []
        self.backtrack(set(nums), [])

        return self.result


# @lc code=end
