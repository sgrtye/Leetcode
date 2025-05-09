#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#


# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l: int = 0
        r: int = len(height) - 1
        max_area: int = 0

        while l < r:
            max_area = max(max_area, (r - l) * min(height[l], height[r]))

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return max_area


# @lc code=end
