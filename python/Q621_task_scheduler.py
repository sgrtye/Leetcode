#
# @lc app=leetcode id=621 lang=python3
#
# [621] Task Scheduler
#

# @lc code=start
import heapq
from collections import deque


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        remaining: dict[str, int] = dict()
        for t in tasks:
            if t not in remaining:
                remaining[t] = 0

            remaining[t] += 1

        max_heap: list[int] = [-count for _, count in remaining.items()]
        heapq.heapify(max_heap)

        time: int = 0
        processing: deque[tuple[int, int]] = deque()

        while max_heap or processing:
            if max_heap:
                count = heapq.heappop(max_heap)

                if count + 1 < 0:
                    processing.append((count + 1, time + n))

            if processing and processing[0][1] == time:
                count, _ = processing.popleft()
                heapq.heappush(max_heap, count)

            time += 1

        return time


# @lc code=end
