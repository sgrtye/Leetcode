# @lcpr-before-debug-begin
from python3problem150 import *
from typing import *

# @lcpr-before-debug-end

#
# @lc app=leetcode id=150 lang=python3
# @lcpr version=30106
#
# [150] Evaluate Reverse Polish Notation
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        evaluation: list[int] = []
        operations: dict[str, Callable[[int, int]], int] = {
            "+": lambda addend2, addend1: addend1 + addend2,
            "-": lambda subtrahend, minuend: minuend - subtrahend,
            "*": lambda factor2, factor1: factor1 * factor2,
            "/": lambda divisor, dividend: int(dividend / divisor),
        }

        for t in tokens:
            if t in operations:
                evaluation.append(operations[t](evaluation.pop(), evaluation.pop()))
            else:
                evaluation.append(int(t))

        return evaluation[0]


# @lc code=end


#
# @lcpr case=start
# ["2","1","+","3","*"]\n
# @lcpr case=end

# @lcpr case=start
# ["4","13","5","/","+"]\n
# @lcpr case=end

# @lcpr case=start
# ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]\n
# @lcpr case=end


# @lcpr case=start
# ["6", "-132", "/"]\n
# @lcpr case=end
#
