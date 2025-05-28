#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#

# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp: list[bool] = [False] * len(s)
        sorted_word_dict: list[srt] = sorted(wordDict, key=lambda w: len(w))

        for i in range(len(s)):
            for word in sorted_word_dict:
                if (
                    i + 1 - len(word) == 0 or (i >= len(word) and dp[i - len(word)])
                ) and s[i - len(word) + 1 : i + 1] == word:
                    dp[i] = True
                    break

        return dp[-1]


# @lc code=end
