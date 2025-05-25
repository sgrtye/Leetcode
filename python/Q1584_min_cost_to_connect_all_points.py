#
# @lc app=leetcode id=1584 lang=python3
#
# [1584] Min Cost to Connect All Points
#

# @lc code=start
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        target: int = len(points)
        connected: list[bool] = [False] * target
        distances: list[int] = [4 * 10**6 + 1] * target

        node: int = 0
        count: int = 0
        result: int = 0

        while count < target - 1:
            connected[node] = True
            next_node: int | None = None

            for i in range(target):
                if connected[i]:
                    continue

                x1, y1 = points[node]
                x2, y2 = points[i]

                distance: int = abs(x1 - x2) + abs(y1 - y2)
                if distance < distances[i]:
                    distances[i] = distance

                if next_node is None or distances[i] < distances[next_node]:
                    next_node = i

            if next_node is None:
                raise Exception()

            result += distances[next_node]
            node = next_node
            count += 1

        return result


# @lc code=end
