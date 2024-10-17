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
    def generateParenthesis(self, n: int) -> List[str]:
        result: list[list[str]] = []
        # string, No. of left parenthesis, No. of right parenthesis
        stack: list[tuple[str, int, int]] = [("", 0, 0)]

        while stack:
            current, left, right = stack.pop()

            if left == right == n:
                result.append(current)

            if left < n:
                stack.append((current + "(", left + 1, right))

            if left > right:
                stack.append((current + ")", left, right + 1))

        return result


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
