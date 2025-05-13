#
# @lc app=leetcode id=981 lang=python3
#
# [981] Time Based Key-Value Store
#


# @lc code=start
class TimeMap:

    def __init__(self):
        self.values: dict[str, list[tuple[str, int]]] = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.values:
            self.values[key] = []
        self.values[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        values: list[tuple[str, int]] = self.values.get(key, [])

        l: int = 0
        r: int = len(values) - 1

        while l <= r:
            m: int = l + ((r - l) // 2)

            if values[m][1] <= timestamp:
                l = m + 1
            else:
                r = m - 1

        return values[r][0] if r >= 0 else ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
# @lc code=end
