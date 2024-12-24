# @lcpr-before-debug-begin
from python3problem347 import *
from typing import *
from collections import Counter

# @lcpr-before-debug-end

#
# @lc app=leetcode id=347 lang=python3
# @lcpr version=30105
#
# [347] Top K Frequent Elements
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_list: list[tuple[int, int]] = sorted(
            Counter(nums).items(), key=lambda x: x[1], reverse=True
        )
        result: list[int] = [n for n, f in nums_list[:k]]

        return result


# @lc code=end


#
# @lcpr case=start
# [1,1,1,2,2,3]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1]\n1\n
# @lcpr case=end

#
