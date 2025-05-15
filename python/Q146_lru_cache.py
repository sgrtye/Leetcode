#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#


# @lc code=start
class Node:
    def __init__(self, key: int, value: int) -> None:
        self.key: int = key
        self.value: int = value
        self.previous: Node | None = None
        self.next: Node | None = None

    def set_value(self, value: int) -> None:
        self.value = value

    def set_previous(self, other: "Node") -> None:
        self.previous = other

    def set_next(self, other: "Node") -> None:
        self.next = other


class LRUCache:

    def __init__(self, capacity: int) -> None:
        self.capacity: int = capacity
        self.dict: dict[int, Node] = dict()
        self.start: Node = Node(-1, -1)
        self.end: Node = Node(-1, -1)

        self.start.set_next(self.end)
        self.end.set_previous(self.start)

    def delete(self, key: int) -> None:
        if key not in self.dict:
            return

        node: Node = self.dict[key]
        del self.dict[key]

        previous: Node = node.previous
        next: Node = node.next

        next.set_previous(previous)
        previous.set_next(next)

    def insert(self, key: int, value: int) -> None:
        self.delete(key)

        new_node: Node = Node(key, value)
        self.dict[key] = new_node

        new_node.set_previous(self.end.previous)
        new_node.set_next(self.end)

        self.end.previous.set_next(new_node)
        self.end.set_previous(new_node)

    def get(self, key: int) -> int:
        if key not in self.dict:
            return -1

        value: int = self.dict[key].value
        self.insert(key, value)
        return value

    def put(self, key: int, value: int) -> None:
        if key not in self.dict and len(self.dict) == self.capacity:
            self.delete(self.start.next.key)

        self.insert(key, value)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end
