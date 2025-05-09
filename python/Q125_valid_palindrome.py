#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#


# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        formated: list[str] = [c for c in s.lower() if c.isalnum()]

        l: int = 0
        r: int = len(formated) - 1

        while l < r:
            if formated[l] != formated[r]:
                return False

            l += 1
            r -= 1

        return True


# @lc code=end
