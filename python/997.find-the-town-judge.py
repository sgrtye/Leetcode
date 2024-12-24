# @lcpr-before-debug-begin
from python3problem997 import *
from typing import *

# @lcpr-before-debug-end

#
# @lc app=leetcode id=997 lang=python3
# @lcpr version=30204
#
# [997] Find the Town Judge
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        incoming = dict.fromkeys(range(1, n + 1), 0)
        outgoing = dict.fromkeys(range(1, n + 1), 0)

        for k, v in trust:
            outgoing[k] += 1
            incoming[v] += 1

        judge = -1
        for i in range(1, n + 1):
            if outgoing[i] == 0 and incoming[i] == n - 1:
                judge = i

        return judge


# @lc code=end


#
# @lcpr case=start
# 2\n[[1,2]]\n
# @lcpr case=end

# @lcpr case=start
# 3\n[[1,3],[2,3]]\n
# @lcpr case=end

# @lcpr case=start
# 3\n[[1,3],[2,3],[3,1]]\n
# @lcpr case=end

#
