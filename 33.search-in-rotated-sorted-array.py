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
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = l + ((r - l) // 2)

            # left is sorted
            if nums[l] <= nums[mid]:
                if nums[l] <= target <= nums[mid]:
                    r = mid
                    break
                else:
                    l = mid + 1
            # right is sorted
            else:
                if nums[mid] <= target <= nums[r]:
                    l = mid
                    break
                else:
                    r = mid - 1
        
        while l <= r:
            mid = l + ((r - l) // 2)

            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
        
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

