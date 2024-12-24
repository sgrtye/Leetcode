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
        left: int = 0
        right: int = 0
        max_length: int = 0
        letter_set: set[str] = set()

        while right < len(s):
            letter: str = s[right]
            while letter in letter_set:
                letter_set.remove(s[left])
                left += 1

            letter_set.add(letter)
            max_length = max(max_length, right - left + 1)
            right += 1

        return max_length


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
