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

            short_left = (
                short[mid] if 0 <= mid <= len(short) - 1 else float("-infinity")
            )
            short_right = (
                short[mid + 1] if 0 <= mid + 1 <= len(short) - 1 else float("infinity")
            )
            long_left = (
                long[other] if 0 <= other <= len(long) - 1 else float("-infinity")
            )
            long_right = (
                long[other + 1]
                if 0 <= other + 1 <= len(long) - 1
                else float("infinity")
            )

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
