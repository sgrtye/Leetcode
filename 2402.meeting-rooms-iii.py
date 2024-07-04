# @lcpr-before-debug-begin
from python3problem2402 import *
from typing import *
import heapq

# @lcpr-before-debug-end

#
# @lc app=leetcode id=2402 lang=python3
# @lcpr version=30204
#
# [2402] Meeting Rooms III
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()

        available_rooms = [i for i in range(n)]
        heapq.heapify(available_rooms)
        used_rooms = []
        count = [0] * n

        for start, end in meetings:
            while used_rooms and start >= used_rooms[0][0]:
                _, room = heapq.heappop(used_rooms)
                heapq.heappush(available_rooms, room)

            time = start
            if not available_rooms:
                time, room = heapq.heappop(used_rooms)
                heapq.heappush(available_rooms, room)

            room = heapq.heappop(available_rooms)
            heapq.heappush(used_rooms, (time + (end - start), room))
            count[room] += 1

        return count.index(max(count))


# @lc code=end


# @lcpr-div-debug-arg-start
# funName=mostBooked
# paramTypes= ["number","number[][]"]
# @lcpr-div-debug-arg-end


#
# @lcpr case=start
# 2\n[[0,10],[1,5],[2,7],[3,4]]\n
# @lcpr case=end

# @lcpr case=start
# 3\n[[1,20],[2,10],[3,5],[4,9],[6,8]]\n
# @lcpr case=end

#
