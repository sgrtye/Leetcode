# @lcpr-before-debug-begin
from python3problem125 import *
from typing import *

# @lcpr-before-debug-end

#
# @lc app=leetcode id=125 lang=python3
# @lcpr version=30106
#
# [125] Valid Palindrome
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [c.lower() for c in s if c.isalnum()]

        l, r = 0, len(s) - 1

        while l <= r:
            if s[l] != s[r]:
                return False

            l += 1
            r -= 1

        return True


# @lc code=end


#
# @lcpr case=start
# "A man, a plan, a canal: Panama"\n
# @lcpr case=end

# @lcpr case=start
# "race a car"\n
# @lcpr case=end

# @lcpr case=start
# " "\n
# @lcpr case=end

#
