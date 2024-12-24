#
# @lc app=leetcode id=287 lang=python3
# @lcpr version=30110
#
# [287] Find the Duplicate Number
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        slow = 0
        while True:
            slow = nums[slow]
            fast = nums[fast]

            if slow == fast:
                return slow


# @lc code=end


#
# @lcpr case=start
# [1,3,4,2,2]\n
# @lcpr case=end

# @lcpr case=start
# [3,1,3,4,2]\n
# @lcpr case=end

#
