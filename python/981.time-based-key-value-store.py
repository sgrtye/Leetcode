# @lcpr-before-debug-begin
from python3problem981 import *
from typing import *

# @lcpr-before-debug-end

#
# @lc app=leetcode id=981 lang=python3
# @lcpr version=30109
#
# [981] Time Based Key-Value Store
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class TimeMap:
    def __init__(self):
        self.dict: dict[str, list[tuple[int, str]]] = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not key in self.dict:
            self.dict[key] = [(timestamp, value)]
        else:
            self.dict[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if not key in self.dict:
            return ""

        values: list[tuple[int, str]] = self.dict[key]

        left: int = 0
        right: int = len(values) - 1

        while left <= right:
            mid: int = (left + right) // 2

            if values[mid][0] < timestamp:
                left = mid + 1
            elif values[mid][0] > timestamp:
                right = mid - 1
            else:
                return values[mid][1]

        if values[right][0] > timestamp:
            return ""
        else:
            return values[right][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
# @lc code=end
