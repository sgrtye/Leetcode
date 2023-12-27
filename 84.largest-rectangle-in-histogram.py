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
        max_area = 0
        stack = []

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                max_area = max(max_area, height * (i - index))
                start = index
            stack.append((start, h))

        for i, h in stack:
            max_area = max(max_area, h * (len(heights) - i))

        return max_area


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
