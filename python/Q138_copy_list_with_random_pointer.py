#
# @lc app=leetcode id=138 lang=python3
#
# [138] Copy List with Random Pointer
#


# Definition for a Node.
class Node:
    def __init__(
        self, x: int, next: "Node | None" = None, random: "Node | None" = None
    ) -> None:
        self.val: int = x
        self.next: Node | None = next
        self.random: Node | None = random


# @lc code=start
class Solution:
    def copyRandomList(self, head: Node | None) -> Node | None:
        if not head:
            return head

        dummy: Node = Node(0)

        original_current: Node | None = head
        copy_current: Node = dummy
        while original_current:
            new_node: Node = Node(original_current.val)
            next_node: Node | None = original_current.next

            copy_current.next = new_node
            original_current.next = new_node
            new_node.random = original_current

            copy_current = new_node
            original_current = next_node

        current: Node | None = dummy.next
        while current:
            assert current.random is not None
            if current.random.random:
                current.random = current.random.random.next
            else:
                current.random = None

            current = current.next

        return dummy.next


# @lc code=end
