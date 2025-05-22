#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        all_times: dict[int, int] = dict()

        for start, end in intervals:
            if start not in all_times:
                all_times[start] = 0

            if end not in all_times:
                all_times[end] = 0

            all_times[start] += 1
            all_times[end] -= 1

        processing: int = 0
        current_start: int | None = None

        result: list[list[int]] = []

        for t in sorted(all_times.keys()):
            if current_start is None:
                current_start = t

            processing += all_times[t]

            if processing == 0:
                result.append([current_start, t])
                current_start = None

        return result


# @lc code=end
