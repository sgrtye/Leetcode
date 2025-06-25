#
# @lc app=leetcode id=684 lang=python3
#
# [684] Redundant Connection
#


# @lc code=start
class UnionFind:
    def __init__(self, n: int) -> None:
        self.parents: list[int] = list(range(n))

    def find(self, n: int) -> int:
        if self.parents[n] != n:
            self.parents[n] = self.find(self.parents[n])

        return self.parents[n]

    def union(self, x: int, y: int) -> bool:
        x_parent: int = self.find(x)
        y_parent: int = self.find(y)

        if x_parent == y_parent:
            return False

        self.parents[x_parent] = y_parent
        return True


class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        union_find: UnionFind = UnionFind(len(edges) + 1)

        for x, y in edges:
            if not union_find.union(x, y):
                return [x, y]

        return []


# @lc code=end
