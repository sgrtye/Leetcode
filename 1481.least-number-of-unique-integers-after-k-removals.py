# @lcpr-before-debug-begin
from python3problem1481 import *
from typing import *

# @lcpr-before-debug-end

#
# @lc app=leetcode id=1481 lang=python3
# @lcpr version=30204
#
# [1481] Least Number of Unique Integers after K Removals
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        arr_map = dict()

        for a in arr:
            arr_map[a] = arr_map.get(a, 0) + 1

        occurrence_list = sorted(arr_map.values(), reverse=True)
        removal_count = k

        while removal_count > 0:
            last_digit = occurrence_list.pop()

            if last_digit > removal_count:
                return len(occurrence_list) + 1

            removal_count -= last_digit

        return len(occurrence_list)


# @lc code=end


# @lcpr-div-debug-arg-start
# funName=findLeastNumOfUniqueInts
# paramTypes= ["number[]","number"]
# @lcpr-div-debug-arg-end


#
# @lcpr case=start
# [5,5,4]\n1\n
# @lcpr case=end

# @lcpr case=start
# [4,3,1,1,3,3,2]\n3\n
# @lcpr case=end

# @lcpr case=start
# [1]\n0\n
# @lcpr case=end

#
