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
        long = nums1 if len(nums1) >= len(nums2) else nums2
        short = nums1 if len(nums1) < len(nums2) else nums2

        half_size = (len(long) + len(short)) // 2

        l = -1
        r = len(short)

        while l <= r:
            mid = l + ((r - l) // 2)
            other = half_size - mid - 2

            short_left = float("-infinity") if mid < 0 else short[mid]
            short_right = float("infinity") if mid > len(short) - 2 else short[mid + 1]

            long_left = float("-infinity") if other < 0 else long[other]
            long_right = float("infinity") if other > len(long) - 2 else long[other + 1]

            if short_left <= long_right and long_left <= short_right:
                if (len(long) + len(short)) % 2 == 1:
                    return min(short_right, long_right)
                else:
                    return (
                        max(short_left, long_left) + min(short_right, long_right)
                    ) / 2
            elif short_left > long_right:
                r = mid - 1
            else:
                l = mid + 1


# @lc code=end


#
# @lcpr case=start
# [1,3]\n[2]\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n[3,4]\n
# @lcpr case=end

#
