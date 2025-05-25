#
# @lc app=leetcode id=332 lang=python3
#
# [332] Reconstruct Itinerary
#

# @lc code=start
class Solution:
    def dfs(self, source: str) -> None:
        while self.adjecent_dict.get(source, []):
            destination: str = self.adjecent_dict[source].pop()
            self.dfs(destination)

        self.result.append(source)

    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        self.target: int = len(tickets) + 1
        self.adjecent_dict: dict[str, list[str]] = dict()

        tickets.sort(reverse=True)

        for source, destination in tickets:
            if source not in self.adjecent_dict:
                self.adjecent_dict[source] = []

            self.adjecent_dict[source].append(destination)

        self.result: list[str] = []
        self.dfs("JFK")

        return self.result[::-1]


# @lc code=end
