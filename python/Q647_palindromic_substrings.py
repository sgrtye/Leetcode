#
# @lc app=leetcode id=647 lang=python3
#
# [647] Palindromic Substrings
#

# @lc code=start
class Solution:
    def countSubstrings(self, s: str) -> int:
        t: str = "@#" + "#".join(s) + "#$"
        p: list[int] = [0] * len(t)

        center: int = 0
        right: int = 0

        for i in range(1, len(t) - 1):
            if i <= right:
                p[i] = right - i if right - i < p[2 * center - i] else p[2 * center - i]

            while t[i - p[i] - 1] == t[i + p[i] + 1]:
                p[i] += 1

            if i + p[i] > right:
                right = i + p[i]
                center = i

        return sum(((x + 1) // 2 for x in p))


# @lc code=end
