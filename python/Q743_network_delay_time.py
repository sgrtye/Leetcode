#
# @lc app=leetcode id=743 lang=python3
#
# [743] Network Delay Time
#


# @lc code=start
import heapq


class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        adjacent_list: list[list[tuple[int, int]]] = [[] for _ in range(n)]

        for source, target, time in times:
            adjacent_list[source - 1].append((target - 1, time))

        heap: list[tuple[int, int]] = [(0, k - 1)]
        visited: set[int] = set()
        result: int = 0

        while heap:
            time, node = heapq.heappop(heap)

            if node in visited:
                continue

            result = time
            visited.add(node)

            for adjacent_node, cost in adjacent_list[node]:
                if adjacent_node not in visited:
                    heapq.heappush(heap, (time + cost, adjacent_node))

        return result if len(visited) == n else -1


# @lc code=end
