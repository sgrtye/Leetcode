#
# @lc app=leetcode id=131 lang=python3
#
# [131] Palindrome Partitioning
#


# @lc code=start
class Solution:
    def is_palindrome(self, left: int, right: int) -> bool:
        while left < right:
            if self.s[left] != self.s[right]:
                return False

            left += 1
            right -= 1

        return True

    def backtrack(self, index: int, stack: list[str]) -> None:
        if index == self.length:
            self.result.append(stack.copy())
            return

        for j in range(index, self.length):
            if self.is_palindrome(index, j):
                stack.append(self.s[index : j + 1])
                self.backtrack(j + 1, stack)
                stack.pop()

    def partition(self, s: str) -> list[list[str]]:
        self.s: str = s
        self.length: int = len(s)
        self.result: list[list[str]] = []

        self.backtrack(0, [])

        return self.result


# @lc code=end
