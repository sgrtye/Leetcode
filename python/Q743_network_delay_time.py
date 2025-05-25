#
# @lc app=leetcode id=743 lang=python3
#
# [743] Network Delay Time
#

# @lc code=start
import heapq


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjecent_list: list[list[tuple[int, int]]] = [[] for _ in range(n)]

        for source, target, time in times:
            adjecent_list[source - 1].append((target - 1, time))

        heap: list[tuple[int, int]] = [(0, k - 1)]
        visited: set[int] = set()
        result: int = 0

        while heap:
            time, node = heapq.heappop(heap)

            if node in visited:
                continue

            result = time
            visited.add(node)

            for adjecent_node, cost in adjecent_list[node]:
                if adjecent_node not in visited:
                    heapq.heappush(heap, (time + cost, adjecent_node))

        return result if len(visited) == n else -1


# @lc code=end
