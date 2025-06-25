#
# @lc app=leetcode id=981 lang=python3
#
# [981] Time Based Key-Value Store
#


# @lc code=start
class TimeMap:
    def __init__(self) -> None:
        self.values: dict[str, list[tuple[str, int]]] = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.values:
            self.values[key] = []
        self.values[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        values: list[tuple[str, int]] = self.values.get(key, [])

        left: int = 0
        right: int = len(values) - 1

        while left <= right:
            m: int = left + ((right - left) // 2)

            if values[m][1] <= timestamp:
                left = m + 1
            else:
                right = m - 1

        return values[right][0] if right >= 0 else ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
# @lc code=end
