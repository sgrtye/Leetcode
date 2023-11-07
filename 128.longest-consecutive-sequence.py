#
# @lc app=leetcode id=128 lang=python3
# @lcpr version=30105
#
# [128] Longest Consecutive Sequence
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        result = 0

        for num in num_set:
            if num - 1 in num_set:
                continue
            else:
                current = 1
                while num + current in num_set:
                    current += 1
                result = max(result, current)
        
        return result
# @lc code=end



#
# @lcpr case=start
# [100,4,200,1,3,2]\n
# @lcpr case=end

# @lcpr case=start
# [0,3,7,2,5,8,4,6,0,1]\n
# @lcpr case=end

#

