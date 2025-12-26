#
# @lc app=leetcode id=460 lang=python3
#
# [460] LFU Cache
#

# @lc code=start
class Node:
    def __init__(self, key: int, value: int) -> None:
        self.key: int = key
        self.value: int = value
        self.count: int = 1

        self.previous: Node | None = None
        self.next: Node | None = None


class LinkedList:
    def __init__(self) -> None:
        self.start = Node(-1, -1)
        self.end = Node(-1, -1)

        self.start.next = self.end
        self.end.previous = self.start

        self.size = 0

    def add_to_head(self, node: Node) -> None:
        tmp = self.start.next
        assert tmp is not None

        self.start.next = node
        node.next = tmp

        node.previous = self.start
        tmp.previous = node

        self.size += 1

    def remove_node(self, node: Node) -> None:
        previous = node.previous
        next = node.next

        assert previous is not None
        assert next is not None

        previous.next = next
        next.previous = previous

        self.size -= 1

    def remove_from_tail(self) -> Node:
        node = self.end.previous
        assert node is not None

        self.remove_node(node)

        return node


class LFUCache:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity

        # key -> Node
        self.dict: dict[int, Node] = dict()

        # f -> LinkedList
        self.mapping: dict[int, LinkedList] = dict()

        self.min_f: int = 0

    def update_f(self, node: Node) -> None:
        self.mapping[node.count].remove_node(node)

        node.count += 1

        if node.count not in self.mapping:
            self.mapping[node.count] = LinkedList()
        self.mapping[node.count].add_to_head(node)

        if node.count == self.min_f + 1 and self.mapping[self.min_f].size == 0:
            self.min_f += 1

    def get(self, key: int) -> int:
        if key not in self.dict:
            return -1

        node = self.dict[key]
        self.update_f(node)

        return node.value

    def put(self, key: int, value: int) -> None:
        # key already exist
        if key in self.dict:
            node = self.dict[key]
            node.value = value
            self.update_f(node)
            return

        # remove LRU node if capacity is full
        if len(self.dict) == self.capacity:
            removed_node = self.mapping[self.min_f].remove_from_tail()
            del self.dict[removed_node.key]

        new_node = Node(key, value)
        self.dict[key] = new_node
        if 1 not in self.mapping:
            self.mapping[1] = LinkedList()

        self.mapping[1].add_to_head(new_node)
        self.min_f = 1


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end
