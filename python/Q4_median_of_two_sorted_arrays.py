#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#


# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        short: list[int] = nums1 if len(nums1) <= len(nums2) else nums2
        long: list[int] = nums2 if len(nums1) <= len(nums2) else nums1

        total: int = len(short) + len(long)
        half: int = total // 2

        left: int = 0
        right: int = len(short)
        result: float = 0.0

        while left <= right:
            mid: int = left + ((right - left) // 2)
            other_mid: int = half - mid

            short_left: int = short[mid - 1] if mid > 0 else -(10**6) - 1
            short_right: int = short[mid] if mid < len(short) else (10**6) + 1
            long_left: int = long[other_mid - 1] if other_mid > 0 else -(10**6) - 1
            long_right: int = long[other_mid] if other_mid < len(long) else (10**6) + 1

            if short_left <= long_right and long_left <= short_right:
                max_left: int = max(short_left, long_left)
                min_right: int = min(short_right, long_right)

                if total % 2 != 0:
                    result = min_right
                else:
                    result = (max_left + min_right) / 2.0

                break

            if short_left > long_right:
                right = mid - 1
            else:
                left = mid + 1

        return result


# @lc code=end
