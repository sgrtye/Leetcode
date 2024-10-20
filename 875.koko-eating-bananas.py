# @lcpr-before-debug-begin
from python3problem875 import *
from typing import *

# @lcpr-before-debug-end

#
# @lc app=leetcode id=875 lang=python3
# @lcpr version=30109
#
# [875] Koko Eating Bananas
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left: int = 1
        right: int = max(piles)
        min_speed: int = 0

        while left <= right:
            mid: int = (left + right) // 2
            time: int = sum(
                [p // mid if p % mid == 0 else (p // mid) + 1 for p in piles]
            )

            if time <= h:
                right = mid - 1
                min_speed = mid
            else:
                left = mid + 1

        return min_speed


# @lc code=end


#
# @lcpr case=start
# [3,6,7,11]\n8\n
# @lcpr case=end

# @lcpr case=start
# [30,11,23,4,20]\n5\n
# @lcpr case=end

# @lcpr case=start
# [30,11,23,4,20]\n6\n
# @lcpr case=end


# @lcpr case=start
# [1,1,1,1,1,11]\n7\n
# @lcpr case=end

#
