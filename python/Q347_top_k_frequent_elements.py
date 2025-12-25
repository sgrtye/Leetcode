#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#


# @lc code=start
import heapq


class Solution:
    def sorting(self, nums: list[int], k: int) -> list[int]:
        frequent_count: dict[int, int] = dict()

        for n in nums:
            frequent_count[n] = frequent_count.get(n, 0) + 1

        result: list[tuple[int, int]] = sorted(
            frequent_count.items(), key=lambda x: x[1], reverse=True
        )

        return [n for n, c in result[:k]]

    def min_heap(self, nums: list[int], k: int) -> list[int]:
        frequent_count: dict[int, int] = dict()

        for n in nums:
            frequent_count[n] = frequent_count.get(n, 0) + 1

        heap: list[tuple[int, int]] = []

        for n, c in frequent_count.items():
            heapq.heappush(heap, (-c, n))

        result: list[int] = []
        for _ in range(k):
            if not heap:
                break

            result.append(heapq.heappop(heap)[1])

        return result

    def bucket_sort(self, nums: list[int], k: int) -> list[int]:
        frequent_count: dict[int, int] = dict()

        for n in nums:
            frequent_count[n] = frequent_count.get(n, 0) + 1

        buckets: list[list[int]] = [[] for _ in range(len(nums) + 1)]

        for n, c in frequent_count.items():
            buckets[c].append(n)

        result: list[int] = []

        for i in range(len(buckets) - 1, -1, -1):
            while len(result) < k and buckets[i]:
                result.append(buckets[i].pop())

        return result

    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        return self.bucket_sort(nums, k)


# @lc code=end
