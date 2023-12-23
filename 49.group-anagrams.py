# @lcpr-before-debug-begin
from python3problem49 import *
from typing import *

# @lcpr-before-debug-end

#
# @lc app=leetcode id=49 lang=python3
# @lcpr version=30105
#
# [49] Group Anagrams
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = dict()

        for s in strs:
            key = "".join(sorted(s))
            current = result.get(key, [])
            current.append(s)
            result[key] = current

        return result.values()


# @lc code=end


#
# @lcpr case=start
# ["eat","tea","tan","ate","nat","bat"]\n
# @lcpr case=end

# @lcpr case=start
# [""]\n
# @lcpr case=end

# @lcpr case=start
# ["a"]\n
# @lcpr case=end

#
