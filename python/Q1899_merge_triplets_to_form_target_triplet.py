#
# @lc app=leetcode id=1899 lang=python3
#
# [1899] Merge Triplets to Form Target Triplet
#


# @lc code=start
class Solution:
    def mergeTriplets(self, triplets: list[list[int]], target: list[int]) -> bool:
        x: bool = False
        y: bool = False
        z: bool = False

        for i, j, k in triplets:
            x |= i == target[0] and j <= target[1] and k <= target[2]
            y |= i <= target[0] and j == target[1] and k <= target[2]
            z |= i <= target[0] and j <= target[1] and k == target[2]

            if x and y and z:
                return True

        return False


# @lc code=end
