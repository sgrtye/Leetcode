#
# @lc app=leetcode id=91 lang=python3
#
# [91] Decode Ways
#

# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s) == 1:
            return 0 if s == "0" else 1

        dp: list[int] = [0] * len(s)
        dp[0] = 0 if s[0] == "0" else 1
        if s[1] != "0":
            dp[1] += dp[0]
        if 10 <= int(s[0:2]) <= 26:
            dp[1] += 1

        for i in range(2, len(s)):
            char: str = s[i]
            previous_one: bool = s[i - 1] == "1"
            previous_two: bool = s[i - 1] == "2"

            match char:
                case "0":
                    if not (previous_one or previous_two):
                        return 0

                    dp[i] = dp[i - 2]

                case "1" | "2" | "3" | "4" | "5" | "6":
                    if previous_one or previous_two:
                        dp[i] = dp[i - 1] + dp[i - 2]
                    else:
                        dp[i] = dp[i - 1]

                case "7" | "8" | "9":
                    if previous_one:
                        dp[i] = dp[i - 1] + dp[i - 2]
                    else:
                        dp[i] = dp[i - 1]

        return dp[-1]


# @lc code=end
