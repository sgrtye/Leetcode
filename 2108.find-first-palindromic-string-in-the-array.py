#
# @lc app=leetcode id=2108 lang=python3
# @lcpr version=30122
#
# [2108] Find First Palindromic String in the Array
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            l, r = 0, len(word) - 1

            while word[l] == word[r]:
                if l >= r:
                    return word
                l, r = l + 1, r - 1

        return ""


# @lc code=end


#
# @lcpr case=start
# ["abc","car","ada","racecar","cool"]\n
# @lcpr case=end

# @lcpr case=start
# ["notapalindrome","racecar"]\n
# @lcpr case=end

# @lcpr case=start
# ["def","ghi"]\n
# @lcpr case=end

#
