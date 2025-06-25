#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input Array Is Sorted
#


# @lc code=start
class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left: int = 0
        right: int = len(numbers) - 1
        result: list[int] = []

        while left < right:
            current: int = numbers[left] + numbers[right]

            if current < target:
                left += 1
            elif current > target:
                right -= 1
            else:
                result = [left + 1, right + 1]
                break

        return result


# @lc code=end
