# @lcpr-before-debug-begin
from python3problem150 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode id=150 lang=python3
# @lcpr version=30106
#
# [150] Evaluate Reverse Polish Notation
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t == "+":
                stack.append(stack.pop() + stack.pop())
            elif t == "-":
                tmp = stack.pop()
                stack.append(stack.pop() - tmp)
            elif t == "*":
                stack.append(stack.pop() * stack.pop())
            elif t == "/":
                tmp = stack.pop()
                stack.append(int(stack.pop() / tmp))
            else:
                stack.append(int(t))

        return stack[0]


# @lc code=end


#
# @lcpr case=start
# ["2","1","+","3","*"]\n
# @lcpr case=end

# @lcpr case=start
# ["4","13","5","/","+"]\n
# @lcpr case=end

# @lcpr case=start
# ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]\n
# @lcpr case=end

#
