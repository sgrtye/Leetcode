#
# @lc app=leetcode id=1463 lang=python3
# @lcpr version=30122
#
# [1463] Cherry Pickup II
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        cache = [[0] * COLS for _ in range(COLS)]

        for i in range(COLS):
            for j in range(COLS):
                cache[i][j] = grid[-1][i] + grid[-1][j]

        for level in reversed(range(ROWS - 1)):
            tmp_cache = [[0] * COLS for _ in range(COLS)]

            for i in range(COLS):
                for j in range(COLS):
                    maximum = 0

                    for i_delta in range(-1, 2):
                        for j_delta in range(-1, 2):
                            c1 = i + i_delta
                            c2 = j + j_delta
                            if c1 >= c2 or c1 == -1 or c2 == COLS:
                                continue

                            maximum = max(maximum, cache[c1][c2])

                    tmp_cache[i][j] = maximum + grid[level][i] + grid[level][j]

            cache = tmp_cache

        return cache[0][COLS - 1]


# @lc code=end


#
# @lcpr case=start
# [[3,1,1],[2,5,1],[1,5,5],[2,1,1]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,0,0,0,0,0,1],[2,0,0,0,0,3,0],[2,0,9,0,0,0,0],[0,3,0,5,4,0,0],[1,0,2,3,0,0,6]]\n
# @lcpr case=end

#
