# @lcpr-before-debug-begin
from python3problem76 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode id=76 lang=python3
# @lcpr version=30109
#
# [76] Minimum Window Substring
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        r = 0
        current_window = dict()
        t_dict = dict()
        res = None

        for c in t:
            t_dict[c] = t_dict.get(c, 0) + 1
        
        unmatched_count = len(t_dict)

        while r < len(s):
            current_window[s[r]] = current_window.get(s[r], 0) + 1

            if current_window[s[r]] == t_dict.get(s[r], 0):
                unmatched_count -= 1
            
            if unmatched_count == 0 and (res is None or len(res) > r - l + 1):
                res = s[l:r + 1]
            
            while unmatched_count == 0:
                current_window[s[l]] -= 1

                if s[l] in t_dict:
                    if current_window[s[l]] == t_dict[s[l]] - 1:
                        unmatched_count += 1
                
                l += 1
            
            while l <= r and (s[l] not in t_dict or (s[l] in t_dict and current_window[s[l]] > t_dict[s[l]])):
                current_window[s[l]] -= 1
                l += 1
            
            r += 1
        
        return res if res is not None else ""
        

# @lc code=end



#
# @lcpr case=start
# "ADOBECODEBANC"\n"ABC"\n
# @lcpr case=end

# @lcpr case=start
# "a"\n"a"\n
# @lcpr case=end

# @lcpr case=start
# "a"\n"aa"\n
# @lcpr case=end

# @lcpr case=start
# "ab"\n"a"\n
# @lcpr case=end

# @lcpr case=start
# "bba"\n"ab"\n
# @lcpr case=end

# @lcpr case=start
# "abcabdebac"\n"cea"\n
# @lcpr case=end

#

