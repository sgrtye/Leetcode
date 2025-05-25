#
# @lc app=leetcode id=778 lang=python3
#
# [778] Swim in Rising Water
#

# @lc code=start
import heapq


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        ROWS: int = len(grid)
        COLS: int = len(grid[0])
        directions: list[tuple[int, int]] = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        heap: list[tuple[int, int, int]] = [(grid[0][0], 0, 0)]
        visited: set[tuple[int, int]] = set()

        while heap:
            height, row, col = heapq.heappop(heap)

            if row == ROWS - 1 and col == COLS - 1:
                return height

            for x, y in directions:
                new_row: int = row + x
                new_col: int = col + y

                if (
                    0 <= new_row < ROWS
                    and 0 <= new_col < COLS
                    and (new_row, new_col) not in visited
                ):
                    visited.add((new_row, new_col))

                    if height > grid[new_row][new_col]:
                        heapq.heappush(heap, (height, new_row, new_col))
                    else:
                        heapq.heappush(heap, (grid[new_row][new_col], new_row, new_col))

        return -1


# @lc code=end
