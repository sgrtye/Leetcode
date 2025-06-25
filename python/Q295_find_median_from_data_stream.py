#
# @lc app=leetcode id=295 lang=python3
#
# [295] Find Median from Data Stream
#


# @lc code=start
import heapq


class MedianFinder:
    def __init__(self) -> None:
        self.small: list[int] = []
        self.large: list[int] = []

    def addNum(self, num: int) -> None:
        if len(self.small) == len(self.large):
            if not self.small:
                self.small.append(-num)
                return

            if num <= -self.small[0]:
                heapq.heappush(self.small, -num)
            else:
                heapq.heappush(self.large, num)

        else:
            if len(self.small) > len(self.large):
                value: int = heapq.heappushpop(self.small, -num)
                heapq.heappush(self.large, -value)
            else:
                value: int = heapq.heappushpop(self.large, num)
                heapq.heappush(self.small, -value)

    def findMedian(self) -> float:
        if len(self.small) == len(self.large):
            return (-self.small[0] + self.large[0]) / 2
        elif len(self.small) > len(self.large):
            return -self.small[0]
        else:
            return self.large[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# @lc code=end
