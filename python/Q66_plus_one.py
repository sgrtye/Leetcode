#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#


# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry: int = 1
        result: list[int] = []

        for d in reversed(digits):
            if carry:
                if d + carry == 10:
                    result.append(0)
                else:
                    result.append(d + carry)
                    carry = 0
            else:
                result.append(d)

        if carry:
            result.append(carry)

        result.reverse()

        return result


# @lc code=end
