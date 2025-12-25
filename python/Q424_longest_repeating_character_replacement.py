#
# @lc app=leetcode id=424 lang=python3
#
# [424] Longest Repeating Character Replacement
#


# @lc code=start
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        result: int = 0
        count: dict[str, int] = {}

        left: int = 0
        max_frequency: int = 0

        for right in range(len(s)):
            new_count: int = 1 + count.get(s[right], 0)

            count[s[right]] = new_count
            if new_count > max_frequency:
                max_frequency = new_count

            while (right - left + 1) - max_frequency > k:
                count[s[left]] -= 1
                left += 1

            if (current_length := right - left + 1) > result:
                result = current_length

        return result


# @lc code=end
