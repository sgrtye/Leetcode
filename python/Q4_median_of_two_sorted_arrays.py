#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#


# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        short: list[int] = nums1 if len(nums1) <= len(nums2) else nums2
        long: list[int] = nums2 if len(nums1) <= len(nums2) else nums1

        total: int = len(short) + len(long)
        half: int = total // 2

        l: int = 0
        r: int = len(short)
        result: float = 0.0

        while l <= r:
            m: int = l + ((r - l) // 2)
            n: int = half - m

            short_left: int = short[m - 1] if m > 0 else -(10**6) - 1
            short_right: int = short[m] if m < len(short) else (10**6) + 1
            long_left: int = long[n - 1] if n > 0 else -(10**6) - 1
            long_right: int = long[n] if n < len(long) else (10**6) + 1

            if short_left <= long_right and long_left <= short_right:
                if total % 2 == 1:
                    result = min(short_right, long_right)
                else:
                    max_left: int = max(short_left, long_left)
                    min_right: int = min(short_right, long_right)
                    result = (max_left + min_right) / 2

                break

            if short_left > long_right:
                r = m - 1
            else:
                l = m + 1

        return result


# @lc code=end
