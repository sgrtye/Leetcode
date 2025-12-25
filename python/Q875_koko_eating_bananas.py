#
# @lc app=leetcode id=875 lang=python3
#
# [875] Koko Eating Bananas
#


# @lc code=start
class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        left: int = 1
        right: int = max(piles)
        result: int = right

        while left <= right:
            speed: int = left + ((right - left) // 2)
            time: int = sum((p // speed) + (p % speed > 0) for p in piles)

            if time <= h:
                right = speed - 1
                result = speed
            else:
                left = speed + 1

        return result


# @lc code=end
