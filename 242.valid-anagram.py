# @lcpr-before-debug-begin
from python3problem242 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode id=242 lang=python3
# @lcpr version=30105
#
# [242] Valid Anagram
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        sDict = {}
        tDict = {}

        for i, j in zip(s, t):
            sDict[i] = sDict.get(i, 0) + 1
            tDict[j] = tDict.get(j, 0) + 1
        
        return sDict == tDict
# @lc code=end



#
# @lcpr case=start
# "anagram"\n"nagaram"\n
# @lcpr case=end

# @lcpr case=start
# "rat"\n"car"\n
# @lcpr case=end

# @lcpr case=start
# "aacc"\n"ccac"\n
# @lcpr case=end
#

