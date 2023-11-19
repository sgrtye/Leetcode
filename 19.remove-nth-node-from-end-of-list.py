#
# @lc app=leetcode id=19 lang=python3
# @lcpr version=30110
#
# [19] Remove Nth Node From End of List
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
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node = ListNode()
        node.next = head
        head = node
        pointer = node
    
        for _ in range(n):
            pointer = pointer.next
        
        while pointer.next:
            pointer = pointer.next
            head = head.next
        
        head.next = head.next.next

        return node.next
# @lc code=end



#
# @lcpr case=start
# [1,2,3,4,5]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1]\n1\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n1\n
# @lcpr case=end

#

