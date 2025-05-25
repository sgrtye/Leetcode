#
# @lc app=leetcode id=787 lang=python3
#
# [787] Cheapest Flights Within K Stops
#

# @lc code=start
class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        prices: list[int | None] = [None for _ in range(n)]
        prices[src] = 0

        for _ in range(k + 1):
            new_prices: list[int | None] = prices.copy()

            for source, destination, price in flights:
                if prices[source] is None:
                    continue

                if (
                    new_prices[destination] is None
                    or new_prices[destination] > prices[source] + price
                ):
                    new_prices[destination] = prices[source] + price

            prices = new_prices

        return prices[dst] if prices[dst] is not None else -1


# @lc code=end
