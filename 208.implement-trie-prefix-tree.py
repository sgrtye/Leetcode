#
# @lc app=leetcode id=208 lang=python3
# @lcpr version=30110
#
# [208] Implement Trie (Prefix Tree)
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.end = False

class Trie:
    def __init__(self):
        self.start = TrieNode()

    def insert(self, word: str) -> None:
        current = self.start
        for c in word:
            i = ord(c) - ord('a')
            if not current.children[i]:
                current.children[i] = TrieNode()
            current = current.children[i]
        current.end = True

    def search(self, word: str) -> bool:
        current = self.start
        for c in word:
            i = ord(c) - ord('a')
            if not current.children[i]:
                return False
            current = current.children[i]
        return current.end

    def startsWith(self, prefix: str) -> bool:
        current = self.start
        for c in prefix:
            i = ord(c) - ord('a')
            if not current.children[i]:
                return False
            current = current.children[i]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end



