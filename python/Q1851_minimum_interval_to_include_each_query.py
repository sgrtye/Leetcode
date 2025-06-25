#
# @lc app=leetcode id=1851 lang=python3
#
# [1851] Minimum Interval to Include Each Query
#


# @lc code=start
import heapq


class Solution:
    def minInterval(self, intervals: list[list[int]], queries: list[int]) -> list[int]:
        intervals.sort()
        sorted_queries: list[int] = sorted(set(queries))

        pointer: int = 0
        active: list[tuple[int, int]] = []
        query_result: dict[int, int] = dict()

        for q in sorted_queries:
            while pointer < len(intervals) and (interval := intervals[pointer])[0] <= q:
                heapq.heappush(active, (interval[1] - interval[0] + 1, interval[1]))
                pointer += 1

            while active and active[0][1] < q:
                heapq.heappop(active)

            query_result[q] = active[0][0] if active else -1

        return [query_result[q] for q in queries]


# @lc code=end
