#
# @lc app=leetcode id=211 lang=python3
# @lcpr version=30110
#
# [211] Design Add and Search Words Data Structure
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class TrieNode:
    def __init__(self):
        self.children = dict()
        self.end = False


class WordDictionary:
    def __init__(self):
        self.start = TrieNode()

    def addWord(self, word: str) -> None:
        current = self.start
        for c in word:
            if c not in current.children:
                current.children[c] = TrieNode()
            current = current.children[c]
        current.end = True

    def search(self, word: str) -> bool:
        current = [self.start]

        for c in word:
            new_list = []

            if c == ".":
                for d in current:
                    new_list.extend(d.children.values())
                current = new_list
            else:
                for d in current:
                    if d.children.get(c):
                        new_list.append(d.children[c])
                current = new_list

            if not new_list:
                return False

        for d in current:
            if d.end:
                return True

        return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
# @lc code=end
