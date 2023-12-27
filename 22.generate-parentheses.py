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
    def backTracking(self, len, left, right):
        if len == 0:
            if left == right:
                self.result.append("".join(self.stack))
            return

        if right > left:
            return

        self.stack.append("(")
        self.backTracking(len - 1, left + 1, right)
        self.stack.pop()

        self.stack.append(")")
        self.backTracking(len - 1, left, right + 1)
        self.stack.pop()

    def generateParenthesis(self, n: int) -> List[str]:
        self.result = []
        self.stack = []

        self.backTracking(n * 2, 0, 0)

        return self.result


# @lc code=end


#
# @lcpr case=start
# 3\n
# @lcpr case=end

# @lcpr case=start
# 1\n
# @lcpr case=end

# @lcpr case=start
# 8\n
# @lcpr case=end

#
