#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#


# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 2:
            return 0

        l: int = 0
        r: int = len(height) - 1

        l_max: int = height[0]
        r_max: int = height[-1]
        volumn: int = 0

        while l <= r:
            if l_max < r_max:
                if (water := l_max - (new_max := height[l])) > 0:
                    volumn += water
                else:
                    l_max = new_max

                l += 1
            else:
                if (water := r_max - (new_max := height[r])) > 0:
                    volumn += water
                else:
                    r_max = new_max

                r -= 1

        return volumn


# @lc code=end
