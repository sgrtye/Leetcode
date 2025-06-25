#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#


# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        formated: list[str] = [c for c in s.lower() if c.isalnum()]

        left: int = 0
        right: int = len(formated) - 1

        while left < right:
            if formated[left] != formated[right]:
                return False

            left += 1
            right -= 1

        return True


# @lc code=end
