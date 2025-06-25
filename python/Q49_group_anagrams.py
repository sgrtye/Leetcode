#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#


# @lc code=start
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        result: dict[str, list[str]] = dict()

        for s in strs:
            key: str = "".join(sorted(s))

            if key not in result:
                result[key] = []

            result[key].append(s)

        return list(result.values())


# @lc code=end
