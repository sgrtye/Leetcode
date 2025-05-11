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

        l: int = 0
        max_frequency: int = 0

        for r in range(len(s)):
            new_count: int = 1 + count.get(s[r], 0)

            count[s[r]] = new_count
            if new_count > max_frequency:
                max_frequency = new_count

            while (r - l + 1) - max_frequency > k:
                count[s[l]] -= 1
                l += 1

            if (current_length := r - l + 1) > result:
                result = current_length

        return result


# @lc code=end
