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
        self.values = dict()
        self.times = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.values[key + str(timestamp)] = value
        self.times[key] = self.times.get(key, [])
        self.times[key].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:  
        timestamps = self.times.get(key, [])
        
        l = 0
        r = len(timestamps) - 1
        res = ""

        while l <= r:
            mid = l + ((r - l) // 2)

            if timestamps[mid] <= timestamp:
                l = mid + 1
                res = self.values[key + str(timestamps[mid])]
            else:
                r = mid - 1
        
        return res
# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
# @lc code=end



