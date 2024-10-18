# @lcpr-before-debug-begin
from python3problem167 import *
from typing import *

# @lcpr-before-debug-end

#
# @lc app=leetcode id=167 lang=python3
# @lcpr version=30106
#
# [167] Two Sum II - Input Array Is Sorted
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left: int = 0
        right: int = len(numbers) - 1

        while left < right:
            n: int = numbers[left] + numbers[right]

            if n == target:
                return [left + 1, right + 1]
            elif n > target:
                right -= 1
            else:
                left += 1


# @lc code=end


#
# @lcpr case=start
# [2,7,11,15]\n9\n
# @lcpr case=end

# @lcpr case=start
# [2,3,4]\n6\n
# @lcpr case=end

# @lcpr case=start
# [-1,0]\n-1\n
# @lcpr case=end

#
