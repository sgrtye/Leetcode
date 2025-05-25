#
# @lc app=leetcode id=127 lang=python3
#
# [127] Word Ladder
#

# @lc code=start
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        if beginWord not in wordList:
            wordList.append(beginWord)

        adjecent_list: dict[str, list[str]] = dict()

        for word in wordList:
            for i in range(len(word)):
                pattern: str = word[:i] + "*" + word[i + 1 :]

                if pattern not in adjecent_list:
                    adjecent_list[pattern] = []

                adjecent_list[pattern].append(word)

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

                    for adjecent_word in adjecent_list[pattern]:
                        if adjecent_word not in visited:
                            visited.add(adjecent_word)
                            new_layer.append(adjecent_word)

            layer = new_layer

        return 0


# @lc code=end
