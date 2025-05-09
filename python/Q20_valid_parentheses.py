#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#


# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack: list[str] = []
        mapping: dict[str, str] = {
            "(": ")",
            "[": "]",
            "{": "}",
        }

        for c in s:
            if c in mapping:
                stack.append(c)
            else:
                if not stack or c != mapping[stack.pop()]:
                    return False

        return not stack


# @lc code=end
