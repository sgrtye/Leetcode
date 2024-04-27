#
# @lc app=leetcode id=387 lang=python3
# @lcpr version=30122
#
# [387] First Unique Character in a String
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = dict()

        for c in s:
            count[c] = count.get(c, 0) + 1

        for i, c in enumerate(s):
            if count[c] == 1:
                return i

        return -1


# @lc code=end


#
# @lcpr case=start
# "leetcode"\n
# @lcpr case=end

# @lcpr case=start
# "loveleetcode"\n
# @lcpr case=end

# @lcpr case=start
# "aabb"\n
# @lcpr case=end

#
