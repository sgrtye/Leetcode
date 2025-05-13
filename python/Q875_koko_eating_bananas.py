#
# @lc app=leetcode id=875 lang=python3
#
# [875] Koko Eating Bananas
#


# @lc code=start
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l: int = 1
        r: int = max(piles)
        result: int = r

        while l <= r:
            speed: int = l + ((r - l) // 2)
            time: int = sum((p // speed) + (p % speed > 0) for p in piles)

            if time <= h:
                r = speed - 1
                result = speed
            else:
                l = speed + 1

        return result


# @lc code=end
