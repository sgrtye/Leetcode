/*
 * @lc app=leetcode id=846 lang=rust
 *
 * [846] Hand of Straights
 */

// @lc code=start
use std::collections::HashMap;

impl Solution {
    pub fn is_n_straight_hand(hand: Vec<i32>, group_size: i32) -> bool {
        if hand.len() % group_size as usize != 0 {
            return false;
        }

        let mut cards: HashMap<i32, i32> = HashMap::new();
        for h in &hand {
            *cards.entry(*h).or_insert(0) += 1;
        }

        let mut unique_cards: Vec<i32> = cards.keys().cloned().collect();
        unique_cards.sort();

        for h in unique_cards {
            while cards[&h] != 0 {
                for i in 0..group_size {
                    let card = h + i;
                    if cards.get(&card).unwrap_or(&0) == &0 {
                        return false;
                    }

                    *cards.get_mut(&card).unwrap() -= 1;
                }
            }
        }

        true
    }
}
// @lc code=end
