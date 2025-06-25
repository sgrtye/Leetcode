#
# @lc app=leetcode id=127 lang=python3
#
# [127] Word Ladder
#


# @lc code=start
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        if endWord not in wordList:
            return 0

        if beginWord not in wordList:
            wordList.append(beginWord)

        adjacent_list: dict[str, list[str]] = dict()

        for word in wordList:
            for i in range(len(word)):
                pattern: str = word[:i] + "*" + word[i + 1 :]

                if pattern not in adjacent_list:
                    adjacent_list[pattern] = []

                adjacent_list[pattern].append(word)

        result: int = 0
        layer: list[str] = [beginWord]
        visited: set[str] = set([beginWord])

        while layer:
            result += 1
            new_layer: list[str] = []

            for word in layer:
                if word == endWord:
                    return result

                for i in range(len(word)):
                    pattern: str = word[:i] + "*" + word[i + 1 :]

                    for adjacent_word in adjacent_list[pattern]:
                        if adjacent_word not in visited:
                            visited.add(adjacent_word)
                            new_layer.append(adjacent_word)

            layer = new_layer

        return 0


# @lc code=end
