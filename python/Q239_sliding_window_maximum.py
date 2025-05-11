#
# @lc app=leetcode id=239 lang=python3
#
# [239] Sliding Window Maximum
#

# @lc code=start
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue: deque[int] = deque()
        result: list[int] = [0] * (len(nums) - k + 1)

        l: int = 0
        for r in range(len(nums)):
            if queue and queue[0] < l:
                queue.popleft()

            while queue and nums[r] >= nums[queue[-1]]:
                queue.pop()

            queue.append(r)

            if r - l + 1 == k:
                result[l] = nums[queue[0]]
                l += 1

        return result


# @lc code=end
