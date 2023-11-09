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
    def getParenthesis(self, n: int) -> List[str]:
        if self.parenthesis_list[n]: return self.parenthesis_list[n]
        if n == 0: return ['']

        result = []
        for i in range(n):
            for left in self.getParenthesis(i):
                for right in self.getParenthesis(n - i - 1):
                    result.append(f'{left}({right})')
        
        return result

    def generateParenthesis(self, n: int) -> List[str]:
        self.parenthesis_list = [None] * (n + 1)
        
        return self.getParenthesis(n)
            
# @lc code=end



#
# @lcpr case=start
# 3\n
# @lcpr case=end

# @lcpr case=start
# 1\n
# @lcpr case=end

#

