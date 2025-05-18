#
# @lc app=leetcode id=212 lang=python3
#
# [212] Word Search II
#


# @lc code=start
class TrieNode:
    def __init__(self) -> None:
        self.children: dict[str, TrieNode] = dict()
        self.end: bool = False


class Solution:
    def insert(self, word: str) -> None:
        current: TrieNode = self.words

        for c in word:
            if c not in current.children:
                current.children[c] = TrieNode()

            current = current.children[c]

        current.end = True

    def find(self, row: int, col: int, node: TrieNode, word: list[str]) -> None:
        if node.end:
            self.result.add("".join(word))

        # out of bounds, visited cell, or no valid words left
        if (
            row < 0
            or col < 0
            or row >= self.ROWS
            or col >= self.COLS
            or self.visiting[row][col]
            or self.board[row][col] not in node.children
        ):
            return

        next_node: TrieNode = node.children[self.board[row][col]]

        self.visiting[row][col] = True
        word.append(self.board[row][col])
        for d1, d2 in self.directions:
            self.find(row + d1, col + d2, next_node, word)
        word.pop()
        self.visiting[row][col] = False

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.ROWS: int = len(board)
        self.COLS: int = len(board[0])

        self.board: list[list[str]] = board
        self.directions: list[tuple[int, int]] = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        self.visiting: list[list[bool]] = [
            [False for _ in range(self.COLS)] for _ in range(self.ROWS)
        ]

        self.result: set[str] = set()

        self.words: TrieNode = TrieNode()
        for word in words:
            self.insert(word)

        for i in range(self.ROWS):
            for j in range(self.COLS):
                self.find(i, j, self.words, [])

        return list(self.result)


# @lc code=end
