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
        new_nums = set(nums)
        result = 0

        for n in nums:
            if n - 1 not in new_nums:
                tmp = n
                tmp_result = 1
                while tmp + 1 in new_nums:
                    tmp += 1
                    tmp_result += 1
                result = max(result, tmp_result)

        return result


# @lc code=end


#
# @lcpr case=start
# [100,4,200,1,3,2]\n
# @lcpr case=end

# @lcpr case=start
# [0,3,7,2,5,8,4,6,0,1]\n
# @lcpr case=end

#
