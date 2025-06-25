#
# @lc app=leetcode id=84 lang=python3
#
# [84] Largest Rectangle in Histogram
#


# @lc code=start
class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        max_area: int = 0
        stack: list[tuple[int, int]] = []  # (index, height)

        for i, h in enumerate(heights):
            start: int = i

            while stack and h < stack[-1][1]:
                index, height = stack.pop()
                max_area = max(max_area, height * (i - index))
                start = index

            stack.append((start, h))

        for i, h in stack:
            max_area = max(max_area, h * (len(heights) - i))

        return max_area


# @lc code=end
