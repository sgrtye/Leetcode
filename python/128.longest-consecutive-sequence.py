# @lcpr-before-debug-begin
from python3problem128 import *
from typing import *

# @lcpr-before-debug-end

#
# @lc app=leetcode id=128 lang=python3
# @lcpr version=30105
#
# [128] Longest Consecutive Sequence
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set: set[int] = set(nums)
        max_length: int = 0

        for num in nums_set:
            if num - 1 in nums_set:
                continue

            count: int = 1
            while num + count in nums_set:
                count += 1

            max_length = max(count, max_length)

        return max_length


# @lc code=end


#
# @lcpr case=start
# [100,4,200,1,3,2]\n
# @lcpr case=end

# @lcpr case=start
# [0,3,7,2,5,8,4,6,0,1]\n
# @lcpr case=end

# @lcpr case=start
# [0]\n
# @lcpr case=end

#
