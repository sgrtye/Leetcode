#
# @lc app=leetcode id=355 lang=python3
#
# [355] Design Twitter
#


# @lc code=start
import heapq


class Twitter:
    def __init__(self) -> None:
        self.count: int = 0
        self.tweets: dict[int, list[tuple[int, int]]] = dict()
        self.followers: dict[int, set[int]] = dict()

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweets:
            self.tweets[userId] = []

        self.tweets[userId].append((self.count, tweetId))
        self.count += 1

    def getNewsFeed(self, userId: int) -> list[int]:
        all_ids: set[int] = self.followers.get(userId, set()) | set([userId])

        all_feeds: list[tuple[int, int]] = []
        for id in all_ids:
            all_feeds.extend(self.tweets.get(id, []))

        return [tweet for _, tweet in heapq.nlargest(10, all_feeds)]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followers:
            self.followers[followerId] = set()
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followers:
            self.followers[followerId] = set()

        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
# @lc code=end
