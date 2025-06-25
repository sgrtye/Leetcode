#
# @lc app=leetcode id=763 lang=python3
#
# [763] Partition Labels
#


# @lc code=start
class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        last_occurence: dict[str, int] = dict()

        for i, c in enumerate(s):
            last_occurence[c] = i

        result: list[int] = []

        left: int = 0
        right: int = 0

        for i in range(len(s)):
            if (position := last_occurence[s[i]]) > right:
                right = position

            if i == right:
                result.append(right - left + 1)
                left = right + 1

        return result


# @lc code=end
