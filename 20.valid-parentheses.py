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
        if (len(s)) % 2 != 0:
            return False

        stack = []
        parentheses = {"(": ")", "[": "]", "{": "}"}

        for c in s:
            if c in parentheses.keys():
                stack.append(c)
            else:
                if not stack or parentheses[stack.pop()] != c:
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
