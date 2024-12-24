#
# @lc app=leetcode id=1291 lang=python3
# @lcpr version=30122
#
# [1291] Sequential Digits
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from collections import deque


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        result = []
        queue = deque(range(1, 10))

        while queue:
            current = queue.popleft()

            if high < current:
                continue

            if low <= current:
                result.append(current)

            last_digit = current % 10

            if last_digit == 9:
                continue

            current = current * 10 + last_digit + 1

            queue.append(current)

        return result


# @lc code=end


#
# @lcpr case=start
# 100\n300\n
# @lcpr case=end

# @lcpr case=start
# 1000\n13000\n
# @lcpr case=end

#
