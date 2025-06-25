#
# @lc app=leetcode id=133 lang=python3
#
# [133] Clone Graph
#


# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None) -> None:
        self.val: int = val
        self.neighbors: list[Node] = neighbors if neighbors is not None else []


# @lc code=start
class Solution:
    def clone(self, node: Node | None) -> Node | None:
        if not node:
            return None

        if node.val in self.mapping:
            return self.mapping[node.val]

        new_node: Node = Node(node.val)
        self.mapping[node.val] = new_node

        for neighbor in node.neighbors:
            n: Node | None = self.clone(neighbor)
            assert n is not None
            new_node.neighbors.append(n)

        return new_node

    def cloneGraph(self, node: Node | None) -> Node | None:
        self.mapping: dict[int, Node] = dict()

        return self.clone(node)


# @lc code=end
