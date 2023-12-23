# @lcpr-before-debug-begin
from python3problem22 import *
from typing import *

# @lcpr-before-debug-end

#
# @lc app=leetcode id=22 lang=python3
# @lcpr version=30106
#
# [22] Generate Parentheses
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def backTrack(self, left: int, right: int, n: int) -> None:
        if left == right == n:
            self.result.append("".join(self.stack))
            return

        if left < n:
            self.stack.append("(")
            self.backTrack(left + 1, right, n)
            self.stack.pop()

        if right < left:
            self.stack.append(")")
            self.backTrack(left, right + 1, n)
            self.stack.pop()

    def generateParenthesis(self, n: int) -> List[str]:
        self.result = []
        self.stack = []

        self.backTrack(0, 0, n)

        return self.result


# @lc code=end


#
# @lcpr case=start
# 3\n
# @lcpr case=end

# @lcpr case=start
# 1\n
# @lcpr case=end

#
