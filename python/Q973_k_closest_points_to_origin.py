#
# @lc app=leetcode id=973 lang=python3
#
# [973] K Closest Points to Origin
#


# @lc code=start
import heapq


class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        min_heap: list[tuple[int, int, int]] = []

        for x, y in points:
            heapq.heappush(min_heap, (x**2 + y**2, x, y))

        result: list[list[int]] = []

        for _ in range(k):
            _, x, y = heapq.heappop(min_heap)
            result.append([x, y])

        return result


# @lc code=end
