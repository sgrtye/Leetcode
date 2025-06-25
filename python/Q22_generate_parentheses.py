#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#


# @lc code=start
class Solution:
    def backtrack(
        self,
        n: int,
        result: list[str],
        stack: list[str],
        open_count: int = 0,
        close_count: int = 0,
    ) -> None:
        if n == open_count == close_count:
            result.append("".join(stack))
            return

        if open_count < n:
            stack.append("(")
            self.backtrack(n, result, stack, open_count + 1, close_count)
            stack.pop()

        if open_count > close_count:
            stack.append(")")
            self.backtrack(n, result, stack, open_count, close_count + 1)
            stack.pop()

    def generateParenthesis(self, n: int) -> list[str]:
        result: list[str] = []
        stack: list[str] = []

        self.backtrack(n, result, stack)
        return result


# @lc code=end
