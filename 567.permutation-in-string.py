# @lcpr-before-debug-begin
from python3problem567 import *
from typing import *

# @lcpr-before-debug-end

#
# @lc app=leetcode id=567 lang=python3
# @lcpr version=30109
#
# [567] Permutation in String
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        r = 0
        current = dict()

        s1_dict = dict()
        for s in s1:
            s1_dict[s] = s1_dict.get(s, 0) + 1

        while r < len(s2):
            char = s2[r]
            current[char] = current.get(char, 0) + 1
            r += 1

            if current == s1_dict:
                return True

            while current.get(char, 0) > s1_dict.get(char, 0):
                tmp = s2[l]

                current[tmp] = current[tmp] - 1
                if current[tmp] == 0:
                    del current[tmp]

                l += 1

        return False


# @lc code=end


#
# @lcpr case=start
# "ab"\n"eidbaooo"\n
# @lcpr case=end

# @lcpr case=start
# "ab"\n"eidboaoo"\n
# @lcpr case=end

#
