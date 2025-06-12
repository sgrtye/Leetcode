#
# @lc app=leetcode id=25 lang=python3
#
# [25] Reverse Nodes in k-Group
#


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val: int = val
        self.next: ListNode | None = next


# @lc code=start
class Solution:
    def longer_than_k(self, head: ListNode, k: int) -> bool:
        for _ in range(k):
            if not head.next:
                return False

            head = head.next

        return True

    def reverse(self, head: ListNode, k: int) -> ListNode:
        previous: ListNode = head
        assert head.next is not None
        current: ListNode | None = head.next
        reversed_head: ListNode | None = head.next

        for _ in range(k):
            assert current is not None
            tmp: ListNode | None = current.next
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

    def reverseKGroupRecursive(
        self, head: Optional[ListNode], k: int
    ) -> Optional[ListNode]:
        count: int = 0
        counting_node: ListNode | None = head

        while counting_node:
            count += 1
            if count == k:
                break

            counting_node = counting_node.next

        if count < k:
            return head

        previous: ListNode | None = None
        current: ListNode | None = head

        for _ in range(k):
            assert current is not None
            tmp: ListNode | None = current.next
            current.next = previous
            previous = current
            current = tmp

        if head:
            head.next = self.reverseKGroup(current, k)

        return previous


# @lc code=end
