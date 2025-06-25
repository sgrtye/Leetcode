#
# @lc app=leetcode id=97 lang=python3
#
# [97] Interleaving String
#


# @lc code=start
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        dp: list[list[bool]] = [[False] * (len(s2) + 1) for _ in range(len(s1) + 1)]
        dp[0][0] = True

        for i in range(len(s1) + 1):
            for j in range(len(s2) + 1):
                if i != 0 and dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]:
                    dp[i][j] = True
                if j != 0 and dp[i][j - 1] and s2[j - 1] == s3[i + j - 1]:
                    dp[i][j] = True

        return dp[-1][-1]


# @lc code=end
