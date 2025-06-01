#
# @lc app=leetcode id=371 lang=python3
#
# [371] Sum of Two Integers
#

# @lc code=start
class Solution:
    def getSum(self, a: int, b: int) -> int:
        carry: int = 0
        res: int = 0
        mask: int = 0xFFFFFFFF

        for i in range(32):
            a_bit: int = (a >> i) & 1
            b_bit: int = (b >> i) & 1
            cur_bit: int = a_bit ^ b_bit ^ carry
            carry = (a_bit + b_bit + carry) >= 2
            if cur_bit:
                res |= 1 << i

        if res > 0x7FFFFFFF:
            res = ~(res ^ mask)

        return res


# @lc code=end
