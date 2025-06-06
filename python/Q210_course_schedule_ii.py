#
# @lc app=leetcode id=210 lang=python3
#
# [210] Course Schedule II
#

# @lc code=start
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegrees: list[int] = [0] * numCourses
        adjecent_list: dict[int, list[int]] = {i: [] for i in range(numCourses)}

        for i, j in prerequisites:
            adjecent_list[j].append(i)
            indegrees[i] += 1

        leaves: list[int] = [i for i, v in enumerate(indegrees) if v == 0]

        finished: list[int] = []
        while leaves:
            node: int = leaves.pop()
            finished.append(node)

            for n in adjecent_list[node]:
                indegrees[n] -= 1
                if indegrees[n] == 0:
                    leaves.append(n)

        return finished if len(finished) == numCourses else []


# @lc code=end
