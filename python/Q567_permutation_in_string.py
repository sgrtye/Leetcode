#
# @lc app=leetcode id=567 lang=python3
#
# [567] Permutation in String
#


# @lc code=start
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_dict: dict[str, int] = dict()
        for s in s1:
            s1_dict[s] = s1_dict.get(s, 0) + 1

        l: int = 0
        remained: int = len(s1_dict)
        counter: dict[str, int] = dict()

        for r in range(len(s2)):
            letter: str = s2[r]

            if letter not in s1_dict:
                remained = len(s1_dict)
                counter.clear()
                l = r + 1
                continue

            counter[letter] = counter.get(letter, 0) + 1

            if letter in s1_dict and counter[letter] == s1_dict[letter]:
                remained -= 1

            while l <= r and counter[letter] > s1_dict[letter]:
                l_letter: str = s2[l]
                if l_letter in s1_dict and counter[l_letter] == s1_dict[l_letter]:
                    remained += 1

                counter[l_letter] -= 1
                l += 1

            if remained == 0:
                return True

        return False


# @lc code=end
