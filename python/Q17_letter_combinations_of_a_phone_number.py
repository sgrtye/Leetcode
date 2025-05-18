#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#


# @lc code=start
class Solution:
    def backtrack(self, index: int, stack: list[str]) -> None:
        if index == self.length:
            self.result.append("".join(stack))
            return

        for c in self.mapping[self.digits[index]]:
            stack.append(c)
            self.backtrack(index + 1, stack)
            stack.pop()

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        self.digits: str = digits
        self.length: int = len(digits)
        self.mapping: dict[str, list[str]] = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

        self.result: list[str] = []

        self.backtrack(0, [])

        return self.result


# @lc code=end
