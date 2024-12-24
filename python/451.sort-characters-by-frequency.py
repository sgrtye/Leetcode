#
# @lc app=leetcode id=451 lang=python3
# @lcpr version=30122
#
# [451] Sort Characters By Frequency
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def frequencySort(self, s: str) -> str:
        result = []
        count = dict()
        max_count = 0

        for c in s:
            count[c] = count.get(c, 0) + 1

        buckets = dict()
        for char, number in count.items():
            buckets[number] = buckets.get(number, [])
            buckets[number].append(char)
            max_count = max(max_count, number)

        for i in range(max_count, 0, -1):
            if i in buckets:
                for c in buckets[i]:
                    result.append(c * i)

        return "".join(result)


# @lc code=end


#
# @lcpr case=start
# "tree"\n
# @lcpr case=end

# @lcpr case=start
# "cccaaa"\n
# @lcpr case=end

# @lcpr case=start
# "Aabb"\n
# @lcpr case=end

#
