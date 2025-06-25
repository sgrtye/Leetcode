#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#


# @lc code=start
class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        result: list[int] = []

        for t in tokens:
            match t:
                case "+":
                    result.append(result.pop() + result.pop())
                case "-":
                    tmp1: int = result.pop()
                    tmp2: int = result.pop()
                    result.append(tmp2 - tmp1)
                case "*":
                    result.append(result.pop() * result.pop())
                case "/":
                    tmp1: int = result.pop()
                    tmp2: int = result.pop()
                    result.append(int(tmp2 / tmp1))
                case t:
                    result.append(int(t))

        return result[0]


# @lc code=end
