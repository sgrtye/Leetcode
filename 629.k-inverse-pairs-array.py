# @lcpr-before-debug-begin
from python3problem629 import *
from typing import *

# @lcpr-before-debug-end

#
# @lc app=leetcode id=629 lang=python3
# @lcpr version=30122
#
# [629] K Inverse Pairs Array
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        dp = [0] * (k + 1)
        dp[0] = 1

        for N in range(1, n + 1):
            current = [0] * (k + 1)
            total = 0
            for K in range(k + 1):
                total += dp[K]
                if K >= N:
                    total -= dp[K - N]
                current[K] = total
            dp = current

        return dp[k] % (10**9 + 7)


# @lc code=end


#
# @lcpr case=start
# 3\n0\n
# @lcpr case=end

# @lcpr case=start
# 3\n1\n
# @lcpr case=end

# @lcpr case=start
# 1000\n1000\n
# @lcpr case=end

#
