#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#


# @lc code=start
class Solution:
    def in_place(self, nums: list[int]) -> list[int]:
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

    def prefix_and_suffix(self, nums: list[int]) -> list[int]:
        prefix: list[int] = [1] * len(nums)

        for i in range(1, len(nums)):
            prefix[i] = prefix[i - 1] * nums[i - 1]

        suffix: list[int] = [1] * len(nums)

        for i in range(len(nums) - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]

        result: list[int] = [prefix[i] * suffix[i] for i in range(len(nums))]

        return result

    def productExceptSelf(self, nums: list[int]) -> list[int]:
        return self.in_place(nums)


# @lc code=end
