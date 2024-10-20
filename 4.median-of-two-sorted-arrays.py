# @lcpr-before-debug-begin
from python3problem4 import *
from typing import *

# @lcpr-before-debug-end

#
# @lc app=leetcode id=4 lang=python3
# @lcpr version=30109
#
# [4] Median of Two Sorted Arrays
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        short: list[int] = nums1 if len(nums1) <= len(nums2) else nums2
        long: list[int] = nums2 if len(nums1) <= len(nums2) else nums1
        total_size: int = len(short) + len(long)
        half_size: int = (total_size + 1) // 2

        left: int = 0
        right: int = len(short)

        while left <= right:
            mid: int = (left + right) // 2
            other: int = half_size - mid

            short_left = short[mid - 1] if mid > 0 else -10**6 - 1
            short_right = short[mid] if mid < len(short) else 10**6 + 1

            long_left = long[other - 1] if other > 0 else -10**6 - 1
            long_right = long[other] if other < len(long) else 10**6 + 1

            if short_left <= long_right and long_left <= short_right:
                if total_size % 2 == 1:
                    return max(short_left, long_left)
                else:
                    return (
                        max(short_left, long_left) + min(short_right, long_right)
                    ) / 2
            elif short_left > long_right:
                right = mid - 1
            else:
                left = mid + 1


# @lc code=end


#
# @lcpr case=start
# [1,3]\n[2]\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n[3,4]\n
# @lcpr case=end

#
