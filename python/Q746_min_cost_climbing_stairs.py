#
# @lc app=leetcode id=746 lang=python3
#
# [746] Min Cost Climbing Stairs
#


# @lc code=start
class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        n: int = len(cost)
        steps: list[int] = [0] * n
        steps[n - 1] = cost[n - 1]
        steps[n - 2] = cost[n - 2]

        for i in range(n - 3, -1, -1):
            steps[i] = min(steps[i + 1], steps[i + 2]) + cost[i]

        return min(steps[0], steps[1])


# @lc code=end
