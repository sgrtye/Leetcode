#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#

# @lc code=start
import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap: list[int] = []

        for n in nums:
            heapq.heappush(min_heap, n)

        while len(min_heap) > k:
            heapq.heappop(min_heap)

        return min_heap[0]


# @lc code=end
