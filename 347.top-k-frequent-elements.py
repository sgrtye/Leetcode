# @lcpr-before-debug-begin
from python3problem347 import *
from typing import *

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
        counter = dict()

        for num in nums:
            counter[num] = counter.get(num, 0) + 1

        counter = sorted(counter.items(), key=lambda x: x[1], reverse=True)

        return [x for x, y in counter[:k]]


# @lc code=end


#
# @lcpr case=start
# [1,1,1,2,2,3]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1]\n1\n
# @lcpr case=end

#
