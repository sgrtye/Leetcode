#
# @lc app=leetcode id=424 lang=python3
# @lcpr version=30109
#
# [424] Longest Repeating Character Replacement
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        r = 0
        current_max = 0
        current_window = dict()

        while r < len(s):
            current_window[s[r]] = current_window.get(s[r], 0) + 1

            while max(current_window.values()) + k < r - l + 1:
                current_window[s[l]] -= 1
                l += 1

            current_max = max(current_max, r - l + 1)

            r += 1

        return current_max


# @lc code=end


#
# @lcpr case=start
# "ABAB"\n2\n
# @lcpr case=end

# @lcpr case=start
# "AABABBA"\n1\n
# @lcpr case=end

# @lcpr case=start
# "A"\n0\n
# @lcpr case=end

#
