# @lcpr-before-debug-begin
from python3problem84 import *
from typing import *

# @lcpr-before-debug-end

#
# @lc app=leetcode id=84 lang=python3
# @lcpr version=30108
#
# [84] Largest Rectangle in Histogram
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_Area: int = 0
        # list[(index, height)]
        stack: list[tuple[int, int]] = []

        for i, h in enumerate(heights):
            start: int = i

            while stack and h < stack[-1][1]:
                index, height = stack.pop()
                max_Area = max(max_Area, height * (i - index))
                start = index

            stack.append((start, h))

        for i, h in stack:
            max_Area = max(max_Area, h * (len(heights) - i))

        return max_Area


# @lc code=end


#
# @lcpr case=start
# [2,1,5,6,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [2,4]\n
# @lcpr case=end

# @lcpr case=start
# [2,1,2]\n
# @lcpr case=end

# @lcpr case=start
# [0,0]\n
# @lcpr case=end

#
