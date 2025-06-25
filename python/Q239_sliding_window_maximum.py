#
# @lc app=leetcode id=239 lang=python3
#
# [239] Sliding Window Maximum
#


# @lc code=start
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        queue: deque[int] = deque()
        result: list[int] = [0] * (len(nums) - k + 1)

        left: int = 0
        for right in range(len(nums)):
            if queue and queue[0] < left:
                queue.popleft()

            while queue and nums[right] >= nums[queue[-1]]:
                queue.pop()

            queue.append(right)

            if right - left + 1 == k:
                result[left] = nums[queue[0]]
                left += 1

        return result


# @lc code=end
