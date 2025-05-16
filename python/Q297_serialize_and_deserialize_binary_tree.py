#
# @lc app=leetcode id=297 lang=python3
#
# [297] Serialize and Deserialize Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Codec:
    def preorder(self, root: TreeNode | None, node_list: list[str]) -> None:
        if not root:
            node_list.append("N")
            return

        node_list.append(str(root.val))
        self.preorder(root.left, node_list)
        self.preorder(root.right, node_list)

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        result: list[str] = []
        self.preorder(root, result)

        return ",".join(result)

    def create(self) -> TreeNode:
        value: str = self.node_list[self.index]
        if value == "N":
            self.index += 1
            return None

        new_node: TreeNode = TreeNode(int(value))
        self.index += 1

        new_node.left = self.create()
        new_node.right = self.create()

        return new_node

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        self.node_list: list[str] = data.split(",")
        self.index: int = 0
        return self.create()


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
# @lc code=end
