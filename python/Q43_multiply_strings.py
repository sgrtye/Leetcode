#
# @lc app=leetcode id=43 lang=python3
#
# [43] Multiply Strings
#

# @lc code=start
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        nums1: list[int] = [int(n) for n in num1[::-1]]
        nums2: list[int] = [int(n) for n in num2[::-1]]
        result: list[int] = [0] * (len(num1) + len(num2))

        for i in range(len(nums1)):
            for j in range(len(nums2)):
                digit: int = nums1[i] * nums2[j]

                result[i + j] += digit

                if (value := result[i + j]) >= 10:
                    result[i + j + 1] += value // 10
                    result[i + j] = value % 10

        result.reverse()

        for i in range(len(result)):
            if result[i] != 0:
                break

        return "".join(str(c) for c in result[i:])


# @lc code=end
