#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#


# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ROWS: int = len(matrix)
        COLS: int = len(matrix[0])

        current_direction: int = 0
        directions: list[tuple[int, int]] = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        visited: list[list[bool]] = [[False] * COLS for _ in range(ROWS)]
        result: list[int] = []

        x: int = 0
        y: int = 0
        dx: int = directions[current_direction][0]
        dy: int = directions[current_direction][1]

        while True:
            if (
                x + dx < 0
                or x + dx >= ROWS
                or y + dy < 0
                or y + dy >= COLS
                or visited[x + dx][y + dy]
            ):
                current_direction = (current_direction + 1) % 4
                dx = directions[current_direction][0]
                dy = directions[current_direction][1]

            result.append(matrix[x][y])
            visited[x][y] = True

            x = x + dx
            y = y + dy

            if x < 0 or x >= ROWS or y < 0 or y >= COLS or visited[x][y]:
                return result


# @lc code=end
