#
# @lc app=leetcode id=435 lang=python3
#
# [435] Non-overlapping Intervals
#

# @lc code=start
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        result: int = 0
        current_end: int = intervals[0][1]

        for i in range(1, len(intervals)):
            start: int = intervals[i][0]
            end: int = intervals[i][1]

            if start >= current_end:
                current_end = end
            else:
                result += 1
                current_end = min(current_end, end)

        return result


# @lc code=end
