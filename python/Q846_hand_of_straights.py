#
# @lc app=leetcode id=846 lang=python3
#
# [846] Hand of Straights
#

# @lc code=start
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        cards: dict[int, int] = dict()

        for h in hand:
            cards[h] = cards.get(h, 0) + 1

        for h in sorted(set(hand)):
            while cards[h] != 0:
                for i in range(groupSize):
                    if h + i not in cards or cards[h + i] == 0:
                        return False

                    cards[h + i] -= 1

        return True


# @lc code=end
