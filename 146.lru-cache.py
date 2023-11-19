#
# @lc app=leetcode id=146 lang=python3
# @lcpr version=30110
#
# [146] LRU Cache
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.dict = dict()
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.capacity = capacity

        self.head.next = self.tail
        self.tail.prev = self.head
    
    def insert(self, node: Node) -> None:
        node.next = self.tail
        node.prev = self.tail.prev
        self.tail.prev.next = node
        self.tail.prev = node
    
    def remove(self, node: Node) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev

    def get(self, key: int) -> int:
        if key in self.dict:
            node = self.dict[key]

            self.remove(node)
            self.insert(node)

            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            node = self.dict[key]
            node.val = value
                
            self.remove(node)
        else:
            if len(self.dict) == self.capacity:
                del self.dict[self.head.next.key]
                self.remove(self.head.next)
  
            node = Node(key, value)
            self.dict[key] = node

        self.insert(node)
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end



