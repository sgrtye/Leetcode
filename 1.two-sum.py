# @lcpr-before-debug-begin
from python3problem1 import *
from typing import *

# @lcpr-before-debug-end

#
# @lc app=leetcode id=1 lang=python3
# @lcpr version=30105
#
# [1] Two Sum
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_dict: dict[int, int] = dict()

        for i, n in enumerate(nums):
            remaining = target - n

            if remaining in index_dict:
                return [i, index_dict[remaining]]
            
            index_dict[n] = i


# @lc code=end


#
# @lcpr case=start
# [2,7,11,15]\n9\n
# @lcpr case=end

# @lcpr case=start
# [3,2,4]\n6\n
# @lcpr case=end

# @lcpr case=start
# [3,3]\n6\n
# @lcpr case=end

#
