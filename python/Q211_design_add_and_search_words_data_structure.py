#
# @lc app=leetcode id=211 lang=python3
#
# [211] Design Add and Search Words Data Structure
#


# @lc code=start
class TrieNode:
    def __init__(self) -> None:
        self.children: dict[str, TrieNode] = dict()
        self.end: bool = False


class WordDictionary:
    def __init__(self) -> None:
        self.root: TrieNode = TrieNode()

    def addWord(self, word: str) -> None:
        current: TrieNode = self.root

        for c in word:
            if c not in current.children:
                current.children[c] = TrieNode()

            current = current.children[c]

        current.end = True

    def search_with_node(self, word: str, node: TrieNode, index: int) -> bool:
        if index != len(word):
            if word[index] == ".":
                return any(
                    self.search_with_node(word, child, index + 1)
                    for child in node.children.values()
                )

            if word[index] in node.children:
                return self.search_with_node(
                    word, node.children[word[index]], index + 1
                )
            else:
                return False
        else:
            return node.end

    def search(self, word: str) -> bool:
        return self.search_with_node(word, self.root, 0)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
# @lc code=end
