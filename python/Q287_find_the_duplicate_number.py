#
# @lc app=leetcode id=287 lang=python3
#
# [287] Find the Duplicate Number
#


# @lc code=start
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow: int = 0
        fast: int = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow2: int = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow


# @lc code=end
