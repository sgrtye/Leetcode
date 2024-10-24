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
        t_dict: dict[str, int] = dict()
        for c in t:
            t_dict[c] = t_dict.get(c, 0) + 1

        result: str = s
        found: bool = False
        window_dict: dict[str, int] = dict()
        unsatisfied_count: int = len(t_dict)

        left: int = 0
        for right in range(len(s)):
            window_dict[s[right]] = window_dict.get(s[right], 0) + 1
            if s[right] in t_dict and window_dict[s[right]] == t_dict[s[right]]:
                unsatisfied_count -= 1

            if unsatisfied_count == 0:
                while unsatisfied_count == 0:
                    if s[left] in t_dict and window_dict[s[left]] == t_dict[s[left]]:
                        unsatisfied_count += 1

                    window_dict[s[left]] -= 1
                    left += 1

                found = True
                result = (
                    s[left - 1 : right + 1]
                    if right - left + 2 < len(result)
                    else result
                )

        return result if found else ""


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
