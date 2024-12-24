# @lcpr-before-debug-begin
from python3problem231 import *
from typing import *

# @lcpr-before-debug-end

#
# @lc app=leetcode id=231 lang=python3
# @lcpr version=30204
#
# [231] Power of Two
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and (n & (n - 1)) == 0


# @lc code=end


#
# @lcpr case=start
# 1\n
# @lcpr case=end

# @lcpr case=start
# 16\n
# @lcpr case=end

# @lcpr case=start
# 3\n
# @lcpr case=end

#
