#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        steps: list[int] = [2] * n
        steps[n - 1] = 1

        for i in range(n - 3, -1, -1):
            steps[i] = steps[i + 1] + steps[i + 2]

        return steps[0]


# @lc code=end
