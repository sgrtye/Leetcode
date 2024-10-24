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
        left: int = 0
        right: int = 0
        max_length: int = 0
        letter_dict: dict[str, int] = dict()

        while right < len(s):
            letter_dict[s[right]] = letter_dict.get(s[right], 0) + 1
            while max(letter_dict.values()) + k < right - left + 1:
                letter_dict[s[left]] -= 1
                left += 1

            max_length = max(max_length, right - left + 1)
            right += 1

        return max_length


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
