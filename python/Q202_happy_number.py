#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        table: list[int] = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
        result: set[int] = set()

        while n not in result:
            if n == 1:
                return True

            result.add(n)

            digits: list[int] = []

            while n:
                digit: int = n % 10
                n = n // 10

                digits.append(digit)

            n = sum(table[d] for d in digits)

        return False


# @lc code=end
