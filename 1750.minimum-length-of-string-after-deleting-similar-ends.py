#
# @lc app=leetcode id=1750 lang=python3
# @lcpr version=30204
#
# [1750] Minimum Length of String After Deleting Similar Ends
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def minimumLength(self, s: str) -> int:
        left = 0
        right = len(s) - 1

        while left < right and s[left] == s[right]:
            character = s[left]
            while left <= right and s[left] == character:
                left += 1
            while left <= right and s[right] == character:
                right -= 1

        return right - left + 1


# @lc code=end


#
# @lcpr case=start
# "ca"\n
# @lcpr case=end

# @lcpr case=start
# "cabaabac"\n
# @lcpr case=end

# @lcpr case=start
# "aabccabba"\n
# @lcpr case=end

#
