# @lcpr-before-debug-begin
from python3problem33 import *
from typing import *

# @lcpr-before-debug-end

#
# @lc app=leetcode id=33 lang=python3
# @lcpr version=30109
#
# [33] Search in Rotated Sorted Array
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left: int = 0
        right: int = len(nums) - 1

        while left <= right:
            mid: int = (left + right) // 2
            value: int = nums[mid]
            change_left_pointer: bool = True

            if value == target:
                return mid

            # left is sorted
            if nums[left] <= value:
                if nums[left] <= target < value:
                    change_left_pointer = False
                else:
                    change_left_pointer = True
            # right is sorted
            else:
                if value < target <= nums[right]:
                    change_left_pointer = True
                else:
                    change_left_pointer = False

            if change_left_pointer:
                left = mid + 1
            else:
                right = mid - 1

        return -1


# @lc code=end


#
# @lcpr case=start
# [4,5,6,7,0,1,2]\n0\n
# @lcpr case=end

# @lcpr case=start
# [4,5,6,7,0,1,2]\n3\n
# @lcpr case=end

# @lcpr case=start
# [1]\n0\n
# @lcpr case=end

# @lcpr case=start
# [3,5,1]\n3\n
# @lcpr case=end

#
