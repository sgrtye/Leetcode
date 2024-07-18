# @lcpr-before-debug-begin
from python3problem201 import *
from typing import *

# @lcpr-before-debug-end

#
# @lc app=leetcode id=201 lang=python3
# @lcpr version=30204
#
# [201] Bitwise AND of Numbers Range
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        i = 0

        while left != right:
            left >>= 1
            right >>= 1
            i += 1

        return right << i


# @lc code=end


#
# @lcpr case=start
# 5\n7\n
# @lcpr case=end

# @lcpr case=start
# 0\n0\n
# @lcpr case=end

# @lcpr case=start
# 1\n2147483647\n
# @lcpr case=end

#
# @lcpr case=start
# 4\n7\n
# @lcpr case=end

#
# @lcpr case=start
# 5\n8\n
# @lcpr case=end

#
