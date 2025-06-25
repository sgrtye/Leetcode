#
# @lc app=leetcode id=853 lang=python3
#
# [853] Car Fleet
#


# @lc code=start
class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        count: int = 0
        previous_time: float = 0.0
        required_time: list[float] = [
            (target - p) / s for p, s in sorted(zip(position, speed), reverse=True)
        ]

        for time in required_time:
            if time > previous_time or count == 0:
                count += 1
                previous_time = time

        return count


# @lc code=end
