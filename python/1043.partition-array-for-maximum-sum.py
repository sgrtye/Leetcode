# @lcpr-before-debug-begin
from python3problem1043 import *
from typing import *

# @lcpr-before-debug-end

#
# @lc app=leetcode id=1043 lang=python3
# @lcpr version=30122
#
# [1043] Partition Array for Maximum Sum
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        max_array = [0] * len(arr)

        for i in range(len(arr)):
            max_sum = 0
            max_element = 0
            for j in range(k):
                if i - j < 0:
                    break
                max_element = max(max_element, arr[i - j])
                sum = max_element * (j + 1) + max_array[i - j - 1]
                max_sum = max(max_sum, sum)

            max_array[i] = max_sum

        return max_array[-1]


# @lc code=end


#
# @lcpr case=start
# [1,15,7]\n3\n
# @lcpr case=end

#
# @lcpr case=start
# [1,15,7,9,2,5,10]\n3\n
# @lcpr case=end

# @lcpr case=start
# [1,4,1,5,7,3,6,1,9,9,3]\n4\n
# @lcpr case=end

# @lcpr case=start
# [1]\n1\n
# @lcpr case=end

#
