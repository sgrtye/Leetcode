#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#


# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_dict: dict[str, int] = dict.fromkeys(set(s), 0)
        t_dict: dict[str, int] = dict.fromkeys(set(t), 0)

        for i, j in zip(s, t):
            s_dict[i] += 1
            t_dict[j] += 1

        return s_dict == t_dict


# @lc code=end
