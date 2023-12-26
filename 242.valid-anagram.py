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

        s_dict = dict()
        t_dict = dict()

        for i, j in zip(s, t):
            s_dict[i] = s_dict.get(i, 0) + 1
            t_dict[j] = t_dict.get(j, 0) + 1

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
