# @lcpr-before-debug-begin
from python3problem3 import *
from typing import *

# @lcpr-before-debug-end

#
# @lc app=leetcode id=3 lang=python3
# @lcpr version=30109
#
# [3] Longest Substring Without Repeating Characters
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        result = 0
        char_set = set()

        for r, c in enumerate(s):
            while c in char_set:
                char_set.remove(s[l])
                l = l + 1

            char_set.add(c)
            result = max(result, r - l + 1)

        return result


# @lc code=end


#
# @lcpr case=start
# "abcabcbb"\n
# @lcpr case=end

# @lcpr case=start
# "bbbbb"\n
# @lcpr case=end

# @lcpr case=start
# "pwwkew"\n
# @lcpr case=end

#
