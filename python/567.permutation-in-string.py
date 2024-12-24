# @lcpr-before-debug-begin
from python3problem567 import *
from typing import *

# @lcpr-before-debug-end

#
# @lc app=leetcode id=567 lang=python3
# @lcpr version=30109
#
# [567] Permutation in String
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        length: int = len(s1)

        s1_counter: dict[str, int] = dict()
        for s in s1:
            s1_counter[s] = s1_counter.get(s, 0) + 1

        left: int = 0
        s2_counter: dict[str, int] = dict()
        for right in range(len(s2)):
            s2_counter[s2[right]] = s2_counter.get(s2[right], 0) + 1

            if right - left + 1 < length:
                continue

            if s1_counter == s2_counter:
                return True

            if s2[right] not in s1_counter:
                s2_counter = dict()
                left = right + 1
            else:
                s2_counter[s2[left]] -= 1
                if s2_counter[s2[left]] == 0:
                    s2_counter.pop(s2[left])
                left += 1

            right += 1

        return False


# @lc code=end


#
# @lcpr case=start
# "ab"\n"eidbaooo"\n
# @lcpr case=end

# @lcpr case=start
# "ab"\n"eidboaoo"\n
# @lcpr case=end

# @lcpr case=start
# "hello"\n"ooolleoooleh"\n
# @lcpr case=end

# @lcpr case=start
# "a"\n"ab"\n
# @lcpr case=end

# @lcpr case=start
# "adc"\n"dcda"\n
# @lcpr case=end

#
