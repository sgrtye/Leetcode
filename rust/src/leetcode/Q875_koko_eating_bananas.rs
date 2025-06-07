/*
 * @lc app=leetcode id=875 lang=rust
 *
 * [875] Koko Eating Bananas
 */

// @lc code=start
impl Solution {
    pub fn min_eating_speed(piles: Vec<i32>, h: i32) -> i32 {
        let mut left: i32 = 1;
        let mut right: i32 = *piles.iter().max().unwrap();

        while left <= right {
            let mid: i32 = left + (right - left) / 2;
            let time: i64 = piles
                .iter()
                .map(|&p| (p / mid) as i64 + if p % mid > 0 { 1 } else { 0 })
                .sum();

            if time > h as i64 {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }

        left
    }
}
// @lc code=end
