#
# @lc app=leetcode id=217 lang=python3
# @lcpr version=30105
#
# [217] Contains Duplicate
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))


# @lc code=end


#
# @lcpr case=start
# [1,2,3,1]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4]\n
# @lcpr case=end

# @lcpr case=start
# [1,1,1,3,3,4,3,2,4,2]\n
# @lcpr case=end

#
