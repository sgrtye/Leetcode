#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input Array Is Sorted
#


# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l: int = 0
        r: int = len(numbers) - 1

        while l < r:
            result: int = numbers[l] + numbers[r]

            if result < target:
                l += 1
            elif result > target:
                r -= 1
            else:
                return [l + 1, r + 1]


# @lc code=end
