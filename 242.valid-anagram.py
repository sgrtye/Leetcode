# @lcpr-before-debug-begin
from python3problem242 import *
from typing import *

# @lcpr-before-debug-end

#
# @lc app=leetcode id=242 lang=python3
# @lcpr version=30105
#
# [242] Valid Anagram
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_dict: dict[str, int] = dict()
        t_dict: dict[str, int] = dict()

        for i in range(len(s)):
            s_dict[s[i]] = s_dict.get(s[i], 0) + 1
            t_dict[t[i]] = t_dict.get(t[i], 0) + 1

        return s_dict == t_dict

# @lc code=end


#
# @lcpr case=start
# "anagram"\n"nagaram"\n
# @lcpr case=end

# @lcpr case=start
# "rat"\n"car"\n
# @lcpr case=end

# @lcpr case=start
# "aacc"\n"ccac"\n
# @lcpr case=end
#
