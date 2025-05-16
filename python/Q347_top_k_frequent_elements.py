#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#


# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequent_count: dict[int, int] = dict()

        for n in nums:
            frequent_count[n] = frequent_count.get(n, 0) + 1

        result: list[tuple[int, int]] = sorted(
            frequent_count.items(), key=lambda x: x[1], reverse=True
        )

        return [k for k, v in result[:k]]


# @lc code=end
