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
        node = Node(None, None)
        self.head = node
        self.tail = node
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.dict:
            node = self.dict[key]
            if node != self.tail:
                node.prev.next = node.next
                node.next.prev = node.prev

                self.tail.next = node
                node.prev = self.tail
                self.tail = node
            return self.dict[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            node = self.dict[key]
            node.val = value

            if node == self.tail:
                return
                
            node.prev.next = node.next
            node.next.prev = node.prev
        else:
            if len(self.dict) == self.capacity and self.capacity != 1:
                del self.dict[self.head.next.key]
                self.head.next.next.prev = self.head
                self.head.next = self.head.next.next
            elif len(self.dict) == self.capacity:
                del self.dict[self.head.next.key]
                self.tail = self.head
  
            node = Node(key, value)
            self.dict[key] = node

        self.tail.next = node
        node.prev = self.tail
        self.tail = node

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end



