# @lcpr-before-debug-begin
from python3problem424 import *
from typing import *

# @lcpr-before-debug-end

#
# @lc app=leetcode id=424 lang=python3
# @lcpr version=30109
#
# [424] Longest Repeating Character Replacement
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = dict()

        l = 0
        maxf = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])

            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1

        return r - l + 1


# @lc code=end


#
# @lcpr case=start
# "ABAB"\n2\n
# @lcpr case=end

# @lcpr case=start
# "AABABBA"\n1\n
# @lcpr case=end

# @lcpr case=start
# "A"\n0\n
# @lcpr case=end

#
