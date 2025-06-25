#
# @lc app=leetcode id=208 lang=python3
#
# [208] Implement Trie (Prefix Tree)
#


# @lc code=start
class TrieNode:
    def __init__(self) -> None:
        self.children: dict[str, TrieNode] = dict()
        self.end: bool = False


class Trie:
    def __init__(self) -> None:
        self.words: TrieNode = TrieNode()

    def insert(self, word: str) -> None:
        current: TrieNode = self.words

        for c in word:
            if c not in current.children:
                current.children[c] = TrieNode()

            current = current.children[c]

        current.end = True

    def search(self, word: str) -> bool:
        current: TrieNode = self.words

        for c in word:
            if c not in current.children:
                return False

            current = current.children[c]

        return current.end

    def startsWith(self, prefix: str) -> bool:
        current: TrieNode = self.words

        for c in prefix:
            if c not in current.children:
                return False

            current = current.children[c]

        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end
