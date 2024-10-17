# @lcpr-before-debug-begin
from python3problem20 import *
from typing import *

# @lcpr-before-debug-end

#
# @lc app=leetcode id=20 lang=python3
# @lcpr version=30106
#
# [20] Valid Parentheses
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        stack: list[str] = []
        parentheses: dict[str, str] = {"(": ")", "[": "]", "{": "}"}

        for char in s:
            if char in parentheses:
                stack.append(char)
            else:
                if not stack or char != parentheses[stack.pop()]:
                    return False

        return not stack


# @lc code=end


#
# @lcpr case=start
# "()"\n
# @lcpr case=end

# @lcpr case=start
# "()[]{}"\n
# @lcpr case=end

# @lcpr case=start
# "(]"\n
# @lcpr case=end

#
