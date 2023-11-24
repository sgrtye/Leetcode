# @lcpr-before-debug-begin
from python3problem212 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode id=212 lang=python3
# @lcpr version=30110
#
# [212] Word Search II
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class Trie:
    def __init__(self):
        self.start = TrieNode()

    def insert(self, word: str) -> None:
        current = self.start
        for c in word:
            if c not in current.children:
                current.children[c] = TrieNode()
            current = current.children[c]
        current.end = True

class Solution:
    def dfs(self, row: int, col: int, node: TrieNode, word: str) -> None:
        if row < 0 or col < 0: return
        if row == self.ROWS or col == self.COLS: return
        if self.board[row][col] not in node.children: return
        if (row, col) in self.visit: return

        word = word + self.board[row][col]
        node = node.children[self.board[row][col]]
        if node.end:
            self.res.add(word)
        
        self.visit.add((row, col))

        self.dfs(row + 1, col, node, word)
        self.dfs(row - 1, col, node, word)
        self.dfs(row, col + 1, node, word)
        self.dfs(row, col - 1, node, word)

        self.visit.remove((row, col))

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.tree = Trie()
        self.board = board
        for w in words:
            self.tree.insert(w)
        
        self.ROWS, self.COLS = len(self.board), len(self.board[0])
        self.res, self.visit = set(), set()

        for r in range(self.ROWS):
            for c in range(self.COLS):
                self.dfs(r, c, self.tree.start, "")

        return list(self.res)


# @lc code=end



#
# @lcpr case=start
# [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]\n["oath","pea","eat","rain"]\n
# @lcpr case=end

# @lcpr case=start
# [["a","b"],["c","d"]]\n["abcb"]\n
# @lcpr case=end

#

