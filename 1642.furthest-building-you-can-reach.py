# @lcpr-before-debug-begin
from python3problem1642 import *
from typing import *
import heapq

# @lcpr-before-debug-end

#
# @lc app=leetcode id=1642 lang=python3
# @lcpr version=30204
#
# [1642] Furthest Building You Can Reach
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        previous = heights[0]
        result = -1
        ladders_heap = []
        remained_bricks = bricks

        for h in heights:
            diff = h - previous
            previous = h

            if diff > 0:
                heapq.heappush(ladders_heap, diff)

                if len(ladders_heap) > ladders:
                    ladder_min = heapq.heappop(ladders_heap)

                    if remained_bricks < ladder_min:
                        break
                    
                    remained_bricks -= ladder_min

            result += 1

        return result


# @lc code=end


# @lcpr-div-debug-arg-start
# funName=furthestBuilding
# paramTypes= ["number[]","number","number"]
# @lcpr-div-debug-arg-end


#
# @lcpr case=start
# [4,2,7,6,9,14,12]\n5\n1\n
# @lcpr case=end

# @lcpr case=start
# [4,12,2,7,3,18,20,3,19]\n10\n2\n
# @lcpr case=end

# @lcpr case=start
# [14,3,19,3]\n17\n0\n
# @lcpr case=end

#
