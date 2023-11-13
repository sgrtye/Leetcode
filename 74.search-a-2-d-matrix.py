# @lcpr-before-debug-begin
from python3problem74 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode id=74 lang=python3
# @lcpr version=30109
#
# [74] Search a 2D Matrix
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])

        l = 0
        r = row * col - 1

        while l <= r:
            mid = l + ((r - l) // 2)

            value = matrix[mid // col][mid % col]
            
            if value < target:
                l = mid + 1
            elif value > target:
                r = mid - 1
            else:
                return True
        
        return False
            
        
# @lc code=end



#
# @lcpr case=start
# [[1,3,5,7],[10,11,16,20],[23,30,34,60]]\n3\n
# @lcpr case=end

# @lcpr case=start
# [[1,3,5,7],[10,11,16,20],[23,30,34,60]]\n13\n
# @lcpr case=end

# @lcpr case=start
# [[1,3,5,7],[10,11,16,20],[23,30,34,50]]\n5\n
# @lcpr case=end

#

