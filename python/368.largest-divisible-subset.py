#
# @lc app=leetcode id=368 lang=python3
# @lcpr version=30122
#
# [368] Largest Divisible Subset
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()

        dp = [[n] for n in nums]
        result = []

        for i in reversed(range(len(nums))):
            for j in range(i + 1, len(nums)):
                if nums[j] % nums[i] != 0:
                    continue

                tmp = [nums[i]] + dp[j]
                dp[i] = tmp if len(tmp) > len(dp[i]) else dp[i]
            result = dp[i] if len(dp[i]) > len(result) else result

        return result


# @lc code=end


#
# @lcpr case=start
# [1,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,4,8]\n
# @lcpr case=end

#
# @lcpr case=start
# [3,4,16,8]\n
# @lcpr case=end

#
# @lcpr case=start
# [1]\n
# @lcpr case=end

#
