#
# @lc app=leetcode id=875 lang=python3
# @lcpr version=30109
#
# [875] Koko Eating Bananas
#

# @lc code=start
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = r

        while l <= r:
            mid = l + ((r - l) // 2)

            totalTime = 0

            for p in piles:
                totalTime += p // mid if p % mid == 0 else (p // mid) + 1
                
            if totalTime <= h:
                res = mid
                r = mid - 1
            else:
                l = mid + 1

        return res

# @lc code=end



#
# @lcpr case=start
# [3,6,7,11]\n8\n
# @lcpr case=end

# @lcpr case=start
# [30,11,23,4,20]\n5\n
# @lcpr case=end

# @lcpr case=start
# [30,11,23,4,20]\n6\n
# @lcpr case=end

#

