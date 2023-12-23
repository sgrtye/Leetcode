#
# @lc app=leetcode id=3 lang=python3
# @lcpr version=30109
#
# [3] Longest Substring Without Repeating Characters
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        ans = 0
        current_set = set()

        while r < len(s):
            if s[r] not in current_set:
                current_set.add(s[r])
                ans = max(ans, len(current_set))
                r += 1
            else:
                while s[r] in current_set:
                    current_set.remove(s[l])
                    l += 1
                current_set.add(s[r])
                r += 1

        return ans


# @lc code=end


#
# @lcpr case=start
# "abcabcbb"\n
# @lcpr case=end

# @lcpr case=start
# "bbbbb"\n
# @lcpr case=end

# @lcpr case=start
# "pwwkew"\n
# @lcpr case=end

#
