#
# @lc app=leetcode id=57 lang=python3
#
# [57] Insert Interval
#


# @lc code=start
class Solution:
    def find_non_lapping_start(self) -> int | None:
        left: int = 0
        right: int = len(self.intervals) - 1

        target: int = self.new_interval[0]

        while left <= right:
            mid: int = left + ((right - left) // 2)

            if self.intervals[mid][1] < target:
                left = mid + 1
            elif self.intervals[mid][1] > target:
                right = mid - 1
            else:
                right = mid - 1

        return right if right > -1 else None

    def find_non_lapping_end(self) -> int | None:
        left: int = 0
        right: int = len(self.intervals) - 1

        target: int = self.new_interval[1]

        while left <= right:
            mid: int = left + ((right - left) // 2)

            if self.intervals[mid][0] < target:
                left = mid + 1
            elif self.intervals[mid][0] > target:
                right = mid - 1
            else:
                left = mid + 1

        return left if left < len(self.intervals) else None

    def insert(
        self, intervals: list[list[int]], newInterval: list[int]
    ) -> list[list[int]]:
        if not intervals:
            return [newInterval]

        self.intervals: list[list[int]] = intervals
        self.new_interval: list[int] = newInterval

        new_interval_start: int = newInterval[0]
        new_interval_end: int = newInterval[1]

        result: list[list[int]] = []

        if (start := self.find_non_lapping_start()) is not None:
            if start == len(intervals) - 1:
                return intervals + [newInterval]

            result.extend(intervals[: start + 1])
            new_interval_start = min(new_interval_start, intervals[start + 1][0])
        else:
            new_interval_start = min(new_interval_start, intervals[0][0])

        if (end := self.find_non_lapping_end()) is not None:
            if end == 0:
                return [newInterval] + intervals

            new_interval_end = max(new_interval_end, intervals[end - 1][1])
            result.append([new_interval_start, new_interval_end])
            result.extend(intervals[end:])
        else:
            new_interval_end = max(new_interval_end, intervals[-1][1])
            result.append([new_interval_start, new_interval_end])

        return result


# @lc code=end
