#
# @lc app=leetcode id=1046 lang=python3
#
# [1046] Last Stone Weight
#


# @lc code=start
import heapq


class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        stone_list: list[int] = [-s for s in stones]

        heapq.heapify(stone_list)

        while len(stone_list) > 1:
            larger: int = heapq.heappop(stone_list)
            smaller: int = heapq.heappop(stone_list)

            if larger != smaller:
                heapq.heappush(stone_list, larger - smaller)

        return -stone_list[0] if stone_list else 0


# @lc code=end
