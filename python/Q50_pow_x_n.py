#
# @lc app=leetcode id=50 lang=python3
#
# [50] Pow(x, n)
#


# @lc code=start
class Solution:
    def power(self, x: float, n: int) -> float:
        if x == 0:
            return 0

        if n == 0:
            return 1

        result: float = self.power(x * x, n // 2)

        return result if n % 2 == 0 else x * result

    def myPow(self, x: float, n: int) -> float:
        result: float = self.power(x, abs(n))

        return result if n > 0 else 1 / result


# @lc code=end
