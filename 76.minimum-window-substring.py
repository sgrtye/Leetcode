# @lcpr-before-debug-begin
from python3problem76 import *
from typing import *

# @lcpr-before-debug-end

#
# @lc app=leetcode id=76 lang=python3
# @lcpr version=30109
#
# [76] Minimum Window Substring
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_dict = dict()
        for c in t:
            t_dict[c] = t_dict.get(c, 0) + 1

        unsatisfied_count = len(t_dict)
        window_dict = dict()
        l = 0
        result = None
        for r in range(len(s)):
            char = s[r]
            window_dict[char] = window_dict.get(char, 0) + 1

            if char not in t_dict:
                continue

            if window_dict[char] == t_dict[char]:
                unsatisfied_count -= 1

            if unsatisfied_count == 0:
                while unsatisfied_count == 0:
                    remove_char = s[l]
                    if remove_char in t_dict and window_dict[remove_char] == t_dict[remove_char]:
                        unsatisfied_count += 1
                    window_dict[remove_char] = window_dict[remove_char] - 1
                    l += 1

                if result is not None:
                    result = s[l - 1:r + 1] if r - l + 2 < len(result) else result
                else:
                    result = s[l - 1:r + 1]

        return result if result is not None else ""


# @lc code=end


#
# @lcpr case=start
# "ADOBECODEBANC"\n"ABC"\n
# @lcpr case=end

# @lcpr case=start
# "a"\n"a"\n
# @lcpr case=end

# @lcpr case=start
# "a"\n"aa"\n
# @lcpr case=end

# @lcpr case=start
# "ab"\n"a"\n
# @lcpr case=end

# @lcpr case=start
# "bba"\n"ab"\n
# @lcpr case=end

# @lcpr case=start
# "abcabdebac"\n"cea"\n
# @lcpr case=end

#
