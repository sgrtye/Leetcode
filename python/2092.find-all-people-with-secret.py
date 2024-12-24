# @lcpr-before-debug-begin
from python3problem2092 import *
from typing import *

# @lcpr-before-debug-end

#
# @lc app=leetcode id=2092 lang=python3
# @lcpr version=30204
#
# [2092] Find All People With Secret
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def findAllPeople(
        self, n: int, meetings: List[List[int]], firstPerson: int
    ) -> List[int]:
        meetings = sorted(meetings, key=lambda x: x[2])
        result = set([0, firstPerson])

        index = 0
        groups = []
        time = meetings[0][2]

        while index <= len(meetings):
            first, second, t = (
                meetings[index] if index < len(meetings) else (None, None, None)
            )

            if time != t:
                meeting_graph = dict()

                for person1, person2 in groups:
                    meeting_graph.setdefault(person1, []).append(person2)
                    meeting_graph.setdefault(person2, []).append(person1)

                visited = dict.fromkeys(meeting_graph.keys(), False)

                for i in meeting_graph.keys():
                    if i not in result:
                        continue

                    if visited[i]:
                        continue

                    stack = [i]
                    member = set()

                    while stack:
                        person = stack.pop()
                        visited[person] = True
                        member.add(person)

                        for neighbor in meeting_graph[person]:
                            if not visited[neighbor]:
                                stack.append(neighbor)

                    result.update(member)

                groups = []

            index += 1
            time = t
            groups.append((first, second))

        return list(result)


# @lc code=end


# @lcpr-div-debug-arg-start
# funName=findAllPeople
# paramTypes= ["number","number[][]","number"]
# @lcpr-div-debug-arg-end


#
# @lcpr case=start
# 6\n[[1,2,5],[2,3,8],[1,5,10]]\n1\n
# @lcpr case=end

# @lcpr case=start
# 4\n[[3,1,3],[1,2,2],[0,3,3]]\n3\n
# @lcpr case=end

# @lcpr case=start
# 5\n[[3,4,2],[1,2,1],[2,3,1]]\n1\n
# @lcpr case=end

# @lcpr case=start
# 5\n[[1,3,3],[2,0,3],[2,3,3]]\n4\n
# @lcpr case=end

#
