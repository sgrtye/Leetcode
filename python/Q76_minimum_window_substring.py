#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#


# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_dict: dict[str, int] = dict()
        result: str | None = None
        for c in t:
            t_dict[c] = t_dict.get(c, 0) + 1

        left: int = 0
        remained: int = len(t_dict)
        counter: dict[str, int] = dict()

        for right in range(len(s)):
            letter: str = s[right]
            counter[letter] = counter.get(letter, 0) + 1

            if letter not in t_dict:
                continue

            if counter[letter] == t_dict[letter]:
                remained -= 1

            if remained == 0:
                while remained == 0:
                    l_letter: str = s[left]
                    if l_letter in t_dict and counter[l_letter] == t_dict[l_letter]:
                        remained += 1

                    counter[l_letter] -= 1
                    left += 1

                if result is None or len(result) > right - left + 2:
                    result = s[left - 1 : right + 1]

        return result if result is not None else ""


# @lc code=end
