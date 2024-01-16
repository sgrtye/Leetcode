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
        s1_dict = dict()
        for s in s1:
            s1_dict[s] = s1_dict.get(s, 0) + 1
        s1_length = len(s1)

        l = 0
        current = dict()
        for r in range(len(s2)):
            char = s2[r]
            current[char] = current.get(char, 0) + 1

            if r - l + 1 == s1_length and current == s1_dict:
                return True
            
            if char not in s1_dict:
                l = r + 1
                current = dict()
            elif current[char] > s1_dict[char]:
                while s2[l] != char:
                    current[s2[l]] = current[s2[l]] - 1
                    if current[s2[l]] == 0:
                        del current[s2[l]]
                    l += 1
                current[s2[l]] = current[s2[l]] - 1
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
