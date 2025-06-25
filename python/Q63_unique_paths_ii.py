#
# @lc app=leetcode id=63 lang=python3
#
# [63] Unique Paths II
#


# @lc code=start
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        ROWS: int = len(obstacleGrid)
        COLS: int = len(obstacleGrid[0])
        dp: list[list[int]] = [[1] * COLS for _ in range(ROWS)]

        for i in range(ROWS):
            for j in range(COLS):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                    continue

                if i > 0 or j > 0:
                    up_blocked: bool = i == 0 or obstacleGrid[i - 1][j] == 1
                    left_blocked: bool = j == 0 or obstacleGrid[i][j - 1] == 1

                    match (up_blocked, left_blocked):
                        case True, True:
                            dp[i][j] = 0
                        case True, False:
                            dp[i][j] = dp[i][j - 1]
                        case False, True:
                            dp[i][j] = dp[i - 1][j]
                        case False, False:
                            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[ROWS - 1][COLS - 1]


# @lc code=end
