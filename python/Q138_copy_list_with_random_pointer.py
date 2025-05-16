#
# @lc app=leetcode id=138 lang=python3
#
# [138] Copy List with Random Pointer
#


# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        if not head:
            return head

        dummy: Node = Node(0)

        original_current: Node = head
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
            if current.random.random:
                current.random = current.random.random.next
            else:
                current.random = None

            current = current.next

        return dummy.next


# @lc code=end
