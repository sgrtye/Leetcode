# @lcpr-before-debug-begin
from python3problem239 import *
from typing import *

# @lcpr-before-debug-end

#
# @lc app=leetcode id=239 lang=python3
# @lcpr version=30109
#
# [239] Sliding Window Maximum
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue: Deque[int] = Deque()
        result: list[int] = []

        for i in range(len(nums)):
            while queue and nums[queue[-1]] < nums[i]:
                queue.pop()

            queue.append(i)

            if queue[0] <= i - k:
                queue.popleft()

            if i + 1 >= k:
                result.append(nums[queue[0]])

        return result


# @lc code=end


#
# @lcpr case=start
# [1,3,-1,-3,5,3,6,7]\n3\n
# @lcpr case=end

# @lcpr case=start
# [1]\n1\n
# @lcpr case=end

#
