#
# @lc app=leetcode id=57 lang=python3
#
# [57] Insert Interval
#


# @lc code=start
class Solution:
    def insert(
        self, intervals: list[list[int]], newInterval: list[int]
    ) -> list[list[int]]:
        new_start, new_end = newInterval
        added: bool = False
        result: list[list[int]] = []

        for interval in intervals:
            if added:
                result.append(interval)
                continue

            current_start, current_end = interval

            if current_end < new_start:
                result.append(interval)
                continue

            if new_end < current_start:
                added = True
                result.extend([[new_start, new_end], interval])
                continue

            new_start = min(new_start, current_start)
            new_end = max(new_end, current_end)

        if not added:
            result.append([new_start, new_end])

        return result


# @lc code=end
