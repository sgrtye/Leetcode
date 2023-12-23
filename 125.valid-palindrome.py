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
        new_s = [c for c in s.lower() if c.isalnum()]

        l = 0
        r = len(new_s) - 1

        while l < r:
            if new_s[l] != new_s[r]:
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
