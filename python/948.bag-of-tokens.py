# @lcpr-before-debug-begin
from python3problem948 import *
from typing import *

# @lcpr-before-debug-end

#
# @lc app=leetcode id=948 lang=python3
# @lcpr version=30204
#
# [948] Bag of Tokens
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        score = 0
        result = 0
        tokens.sort()

        left = 0
        right = len(tokens) - 1

        while left <= right:
            if power >= tokens[left]:
                power -= tokens[left]
                score += 1
                left += 1
                result = max(result, score)
            elif score > 0:
                power += tokens[right]
                score -= 1
                right -= 1
            else:
                break

        return result


# @lc code=end


#
# @lcpr case=start
# [100]\n50\n
# @lcpr case=end

# @lcpr case=start
# [200,100]\n150\n
# @lcpr case=end

# @lcpr case=start
# [100,200,300,400]\n200\n
# @lcpr case=end

# @lcpr case=start
# [50,50,50,100,100]\n50\n
# @lcpr case=end

#
