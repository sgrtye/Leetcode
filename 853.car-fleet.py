# @lcpr-before-debug-begin
from python3problem853 import *
from typing import *

# @lcpr-before-debug-end

#
# @lc app=leetcode id=853 lang=python3
# @lcpr version=30108
#
# [853] Car Fleet
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        info: list[tuple[int, int]] = sorted(zip(position, speed), reverse=True)
        stack: list[float] = []

        for pos, spd in info:
            time: float = (target - pos) / spd

            if not stack or time > stack[-1]:
                stack.append(time)

        return len(stack)


# @lc code=end


#
# @lcpr case=start
# 12\n[10,8,0,5,3]\n[2,4,1,1,3]\n
# @lcpr case=end

# @lcpr case=start
# 10\n[3]\n[3]\n
# @lcpr case=end

# @lcpr case=start
# 100\n[0,2,4]\n[4,2,1]\n
# @lcpr case=end

#
