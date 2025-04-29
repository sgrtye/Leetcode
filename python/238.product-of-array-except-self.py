#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#


# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length: int = len(nums)
        result: list[int] = [1] * length

        number: int = 1
        for i in range(1, length):
            number *= nums[i - 1]
            result[i] *= number

        number = 1
        for i in range(length - 2, -1, -1):
            number *= nums[i + 1]
            result[i] *= number

        return result


# @lc code=end
