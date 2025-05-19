#
# @lc app=leetcode id=1046 lang=python3
#
# [1046] Last Stone Weight
#

# @lc code=start
import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones: list[int] = [-s for s in stones]

        heapq.heapify(stones)

        while len(stones) > 1:
            larger: int = heapq.heappop(stones)
            smaller: int = heapq.heappop(stones)

            if larger != smaller:
                heapq.heappush(stones, larger - smaller)

        return -stones[0] if stones else 0


# @lc code=end
