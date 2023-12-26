# @lcpr-before-debug-begin
from python3problem217 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode id=217 lang=python3
# @lcpr version=30105
#
# [217] Contains Duplicate
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        number_set = set()
        
        for n in nums:
            if n in number_set:
                return True
            number_set.add(n)
        
        return False


# @lc code=end


#
# @lcpr case=start
# [1,2,3,1]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4]\n
# @lcpr case=end

# @lcpr case=start
# [1,1,1,3,3,4,3,2,4,2]\n
# @lcpr case=end

#
