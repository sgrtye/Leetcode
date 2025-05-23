#
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#

# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        left: int = 0
        right: int = 0
        result: int = 0

        while right < len(nums) - 1:
            max_length: int = 0
            for i in range(left, right + 1):
                if (new_length := i + nums[i]) > max_length:
                    max_length = new_length

            left = right + 1
            right = max_length
            result += 1

        return result


# @lc code=end
