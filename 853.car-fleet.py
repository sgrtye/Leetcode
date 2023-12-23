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
        info = list(zip(position, speed))
        info.sort(key=lambda x: x[0], reverse=True)

        count = 0
        previous_time = None
        for p, s in info:
            required_time = (target - p) / s
            if not previous_time:
                previous_time = required_time
                count += 1
            elif previous_time < required_time:
                previous_time = required_time
                count += 1
            else:
                # In this case, the current cat catches to the front car
                pass

        return count


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
