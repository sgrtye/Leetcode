#
# @lc app=leetcode id=338 lang=python3
#
# [338] Counting Bits
#

# @lc code=start
class Solution:
    def countBits(self, n: int) -> List[int]:
        result: list[int] = [0, 1]

        while len(result) < n + 1:
            result += [n + 1 for n in result]

        return result[: n + 1]


# @lc code=end
