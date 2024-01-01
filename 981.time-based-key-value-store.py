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
        self.structure = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.structure:
            self.structure[key] = []
        self.structure[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        ans = ""
        temp = self.structure.get(key, [])

        l, r = 0, len(temp) - 1
        while l <= r:
            mid = (l + r) // 2

            if temp[mid][1] <= timestamp:
                ans = temp[mid][0]
                l = mid + 1
            else:
                r = mid - 1
        return ans


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
# @lc code=end
