#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#


# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        t: str = "@#" + "#".join(s) + "#$"
        p: list[int] = [0] * len(t)

        center: int = 0
        right: int = 0

        result: int = 0
        length: int = 0

        for i in range(1, len(t) - 1):
            if i <= right:
                p[i] = right - i if right - i < p[2 * center - i] else p[2 * center - i]

            while t[i - p[i] - 1] == t[i + p[i] + 1]:
                p[i] += 1

            if i + p[i] > right:
                right = i + p[i]
                center = i

            if p[i] > length:
                length = p[i]
                result = i

        palindrome_in_t: str = t[result - length : result + length + 1]
        return palindrome_in_t.replace("#", "").replace("@", "").replace("$", "")


# @lc code=end
