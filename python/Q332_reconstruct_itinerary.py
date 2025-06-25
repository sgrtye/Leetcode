#
# @lc app=leetcode id=332 lang=python3
#
# [332] Reconstruct Itinerary
#


# @lc code=start
class Solution:
    def dfs(self, source: str) -> None:
        while self.adjacent_dict.get(source, []):
            destination: str = self.adjacent_dict[source].pop()
            self.dfs(destination)

        self.result.append(source)

    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        self.target: int = len(tickets) + 1
        self.adjacent_dict: dict[str, list[str]] = dict()

        tickets.sort(reverse=True)

        for source, destination in tickets:
            if source not in self.adjacent_dict:
                self.adjacent_dict[source] = []

            self.adjacent_dict[source].append(destination)

        self.result: list[str] = []
        self.dfs("JFK")

        return self.result[::-1]


# @lc code=end
