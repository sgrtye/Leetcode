# @lcpr-before-debug-begin
from python3problem153 import *
from typing import *

# @lcpr-before-debug-end

#
# @lc app=leetcode id=153 lang=python3
# @lcpr version=30109
#
# [153] Find Minimum in Rotated Sorted Array
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left: int = 0
        right: int = len(nums) - 1

        while left <= right:
            if nums[left] <= nums[right]:
                return nums[left]

            mid: int = (left + right) // 2

            if nums[mid] <= nums[right]:
                right = mid
            else:
                left = mid + 1


# @lc code=end


#
# @lcpr case=start
# [3,4,5,1,2]\n
# @lcpr case=end

# @lcpr case=start
# [4,5,6,7,0,1,2]\n
# @lcpr case=end

# @lcpr case=start
# [11,13,15,17]\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

# @lcpr case=start
# [3,1,2]\n
# @lcpr case=end

#
