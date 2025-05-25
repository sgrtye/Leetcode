#
# @lc app=leetcode id=133 lang=python3
#
# [133] Clone Graph
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional


class Solution:
    def clone(self, node: "Node | None") -> "Node | None":
        if not node:
            return None

        if node.val in self.mapping:
            return self.mapping[node.val]

        new_node: "Node" = Node(node.val)
        self.mapping[node.val] = new_node

        for neighbor in node.neighbors:
            new_node.neighbors.append(self.clone(neighbor))

        return new_node

    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        self.mapping: dict[int, "Node"] = dict()

        return self.clone(node)


# @lc code=end
