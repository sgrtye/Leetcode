# @lcpr-before-debug-begin
from python3problem2971 import *
from typing import *

# @lcpr-before-debug-end

#
# @lc app=leetcode id=2971 lang=python3
# @lcpr version=30204
#
# [2971] Find Polygon With the Largest Perimeter
#


# @lc code=start
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        result = -1
        total = 0

        for n in nums:
            if total > n:
                result = total + n
            total += n

        return result


# @lc code=end


# @lcpr-div-debug-arg-start
# funName=largestPerimeter
# paramTypes= ["number[]"]
# @lcpr-div-debug-arg-end


#
# @lcpr case=start
# [5,5,5]\n
# @lcpr case=end

# @lcpr case=start
# [1,12,1,2,5,50,3]\n
# @lcpr case=end

# @lcpr case=start
# [5,5,50]\n
# @lcpr case=end

#
