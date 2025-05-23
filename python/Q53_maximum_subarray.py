#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current: int = 0
        result: int = nums[0]

        for n in nums:
            if current < 0:
                current = 0

            current += n
            if current > result:
                result = current

        return result


# @lc code=end
