/*
 * @lc app=leetcode id=355 lang=rust
 *
 * [355] Design Twitter
 */

// @lc code=start
use std::collections::BinaryHeap;
use std::collections::HashMap;
use std::collections::HashSet;
use std::collections::VecDeque;

struct Twitter {
    following: HashMap<i32, HashSet<i32>>,
    tweets: HashMap<i32, VecDeque<(i32, i32)>>,
    timestamp: i32,
}

/**
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl Twitter {
    fn new() -> Self {
        Twitter {
            following: HashMap::new(),
            tweets: HashMap::new(),
            timestamp: 0,
        }
    }

    fn check_user(&mut self, user_id: i32) {
        if !self.following.contains_key(&user_id) {
            self.following.entry(user_id).or_default();
            self.tweets.entry(user_id).or_default();
        }
    }

    fn post_tweet(&mut self, user_id: i32, tweet_id: i32) {
        self.check_user(user_id);

        self.tweets
            .get_mut(&user_id)
            .unwrap()
            .push_back((self.timestamp, tweet_id));

        if self.tweets.get_mut(&user_id).unwrap().len() > 10 {
            self.tweets.get_mut(&user_id).unwrap().pop_front();
        }

        self.timestamp += 1;
    }

    fn get_news_feed(&self, user_id: i32) -> Vec<i32> {
        let mut heap: BinaryHeap<(i32, i32)> = BinaryHeap::new();

        if let Some(user_tweets) = self.tweets.get(&user_id) {
            for &(timestamp, tweet) in user_tweets {
                heap.push((timestamp, tweet));
            }
        }

        if let Some(following_set) = self.following.get(&user_id) {
            for &followee_id in following_set {
                if let Some(followee_tweets) = self.tweets.get(&followee_id) {
                    for &(timestamp, tweet) in followee_tweets {
                        heap.push((timestamp, tweet));
                    }
                }
            }
        }

        let mut result: Vec<i32> = Vec::new();
        for _ in 0..10 {
            if let Some((_, tweet)) = heap.pop() {
                result.push(tweet);
            } else {
                break;
            }
        }

        result
    }

    fn follow(&mut self, follower_id: i32, followee_id: i32) {
        self.check_user(follower_id);
        self.check_user(followee_id);

        self.following
            .get_mut(&follower_id)
            .unwrap()
            .insert(followee_id);
    }

    fn unfollow(&mut self, follower_id: i32, followee_id: i32) {
        self.following
            .get_mut(&follower_id)
            .unwrap()
            .remove(&followee_id);
    }
}

// /**
//  * Your Twitter object will be instantiated and called as such:
//  * let obj = Twitter::new();
//  * obj.post_tweet(userId, tweetId);
//  * let ret_2: Vec<i32> = obj.get_news_feed(userId);
//  * obj.follow(followerId, followeeId);
//  * obj.unfollow(followerId, followeeId);
//  */
// @lc code=end
