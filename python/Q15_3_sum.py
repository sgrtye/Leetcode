#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#


# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result: list[list[int]] = []

        for i, n in enumerate(nums):
            if n > 0:
                break

            if i > 0 and n == nums[i - 1]:
                continue

            l: int = i + 1
            r: int = len(nums) - 1
            while l < r:
                sum: int = n + nums[l] + nums[r]

                if sum > 0:
                    r -= 1
                elif sum < 0:
                    l += 1
                else:
                    result.append([n, nums[l], nums[r]])

                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return result


# @lc code=end
