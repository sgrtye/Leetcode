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
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = l + ((r - l) // 2)

            if nums[mid] == target:
                return mid

            # if left half is sorted
            if nums[mid] > nums[r]:
                if nums[l] <= target < nums[mid]:
                    change_left_pointer = False
                else:
                    change_left_pointer = True
            else:
                if nums[mid] < target <= nums[r]:
                    change_left_pointer = True
                else:
                    change_left_pointer = False

            if change_left_pointer:
                l = mid + 1
            else:
                r = mid - 1

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

#
