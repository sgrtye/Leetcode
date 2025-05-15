#
# @lc app=leetcode id=25 lang=python3
#
# [25] Reverse Nodes in k-Group
#


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def longer_than_k(self, head: ListNode, k: int) -> bool:
        for _ in range(k):
            if not head.next:
                return False

            head = head.next

        return True

    def reverse(self, head: ListNode, k: int) -> ListNode:
        previous: ListNode = head
        current: ListNode = head.next
        reversed_head: ListNode = head.next

        for _ in range(k):
            tmp: ListNode = current.next
            current.next = previous
            previous = current
            current = tmp

        head.next = previous
        reversed_head.next = current
        return reversed_head

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy: ListNode = ListNode(next=head)
        current: ListNode = dummy

        while self.longer_than_k(current, k):
            current = self.reverse(current, k)

        return dummy.next


# @lc code=end
