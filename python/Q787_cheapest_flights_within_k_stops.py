#
# @lc app=leetcode id=787 lang=python3
#
# [787] Cheapest Flights Within K Stops
#


# @lc code=start
class Solution:
    def findCheapestPrice(
        self, n: int, flights: list[list[int]], src: int, dst: int, k: int
    ) -> int:
        prices: list[int] = [10**5 for _ in range(n)]
        prices[src] = 0

        for _ in range(k + 1):
            new_prices: list[int] = prices.copy()

            for source, destination, price in flights:
                if prices[source] == 10**5:
                    continue

                if (
                    new_prices[destination] == 10**5
                    or new_prices[destination] > prices[source] + price
                ):
                    new_prices[destination] = prices[source] + price

            prices = new_prices

        return prices[dst] if prices[dst] != 10**5 else -1


# @lc code=end
