#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#

# @lc code=start
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegrees: list[int] = [0] * numCourses
        adjecent_list: dict[int, list[int]] = {i: [] for i in range(numCourses)}

        for i, j in prerequisites:
            adjecent_list[j].append(i)
            indegrees[i] += 1

        leaves: list[int] = [i for i, v in enumerate(indegrees) if v == 0]

        finished: int = 0
        while leaves:
            finished += 1
            node: int = leaves.pop()

            for n in adjecent_list[node]:
                indegrees[n] -= 1
                if indegrees[n] == 0:
                    leaves.append(n)

        return finished == numCourses


# @lc code=end
