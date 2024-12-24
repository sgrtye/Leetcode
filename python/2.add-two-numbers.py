#
# @lc app=leetcode id=2 lang=python3
# @lcpr version=30109
#
# [2] Add Two Numbers
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = result = ListNode()
        carry = 0

        while l1 or l2 or carry:
            num1 = l1.val if l1 else 0
            num2 = l2.val if l2 else 0

            sum = num1 + num2 + carry
            result.next = ListNode(sum % 10)
            result = result.next
            carry = sum // 10

            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2

        return dummy.next


# @lc code=end


#
# @lcpr case=start
# [2,4,3]\n[5,6,4]\n
# @lcpr case=end

# @lcpr case=start
# [0]\n[0]\n
# @lcpr case=end

# @lcpr case=start
# [9,9,9,9,9,9,9]\n[9,9,9,9]\n
# @lcpr case=end

#
