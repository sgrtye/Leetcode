# @lcpr-before-debug-begin
from python3problem22 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode id=22 lang=python3
# @lcpr version=30106
#
# [22] Generate Parentheses
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0: return ['']

        result = []
        for i in range(n):
            for left in self.generateParenthesis(i):
                for right in self.generateParenthesis(n - i - 1):
                    result.append(f'{left}({right})')
        
        return result
            
# @lc code=end



#
# @lcpr case=start
# 3\n
# @lcpr case=end

# @lcpr case=start
# 1\n
# @lcpr case=end

#

