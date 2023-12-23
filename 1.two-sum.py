#
# @lc app=leetcode id=1 lang=python3
# @lcpr version=30105
#
# [1] Two Sum
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = dict()

        for i, n in enumerate(nums):
            if n not in result.keys():
                result[target - n] = i
            else:
                return [i, result[n]]

        return None


# @lc code=end


#
# @lcpr case=start
# [2,7,11,15]\n9\n
# @lcpr case=end

# @lcpr case=start
# [3,2,4]\n6\n
# @lcpr case=end

# @lcpr case=start
# [3,3]\n6\n
# @lcpr case=end

#
