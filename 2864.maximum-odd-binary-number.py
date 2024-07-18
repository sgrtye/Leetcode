# @lcpr-before-debug-begin
from python3problem2864 import *
from typing import *

# @lcpr-before-debug-end

#
# @lc app=leetcode id=2864 lang=python3
# @lcpr version=30204
#
# [2864] Maximum Odd Binary Number
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        zero_count = 0
        one_count = 0

        for digit in s:
            if digit == "0":
                zero_count += 1
            else:
                one_count += 1

        if one_count == 1:
            return "0" * zero_count + "1"

        return "1" * (one_count - 1) + "0" * zero_count + "1"


# @lc code=end


# @lcpr-div-debug-arg-start
# funName=maximumOddBinaryNumber
# paramTypes= ["string"]
# @lcpr-div-debug-arg-end


#
# @lcpr case=start
# "010"\n
# @lcpr case=end

# @lcpr case=start
# "0101"\n
# @lcpr case=end

#
