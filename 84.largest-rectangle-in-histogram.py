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
        stack = []
        max_area = 0

        for i, h in enumerate(heights):
            if not stack:
                stack.append((h, i))
            else:
                if h > stack[-1][0]:
                    stack.append((h, i))
                elif h == stack[-1][0]:
                    continue
                else:
                    while stack and h < stack[-1][0]:
                        tmp = stack.pop()
                        max_area = max(max_area, (i - tmp[1]) * tmp[0])
                    stack.append((h, tmp[1]))

        for h, i in stack:
            max_area = max(max_area, (len(heights) - i) * h)

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
