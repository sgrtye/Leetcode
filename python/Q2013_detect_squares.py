#
# @lc app=leetcode id=2013 lang=python3
#
# [2013] Detect Squares
#

# @lc code=start
class DetectSquares:
    def __init__(self):
        self.points: dict[tuple[int, int], int] = dict()

    def add(self, point: List[int]) -> None:
        self.points[(point[0], point[1])] = self.points.get((point[0], point[1]), 0) + 1

    def count(self, point: List[int]) -> int:
        x: int = point[0]
        y: int = point[1]

        result: int = 0

        for (i, j), count in self.points.items():
            if x == i or y == j or abs(x - i) != abs(y - j):
                continue

            result += count * self.points.get((x, j), 0) * self.points.get((i, y), 0)

        return result


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
# @lc code=end
