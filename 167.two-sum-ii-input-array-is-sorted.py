#
# @lc app=leetcode id=167 lang=python3
# @lcpr version=30106
#
# [167] Two Sum II - Input Array Is Sorted
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1

        while l < r:
            result = numbers[l] + numbers[r]
            if result > target:
                r -= 1
            elif result < target:
                l += 1
            else:
                return [l + 1, r + 1]


# @lc code=end


#
# @lcpr case=start
# [2,7,11,15]\n9\n
# @lcpr case=end

# @lcpr case=start
# [2,3,4]\n6\n
# @lcpr case=end

# @lcpr case=start
# [-1,0]\n-1\n
# @lcpr case=end

#
