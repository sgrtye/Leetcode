/*
 * @lc app=leetcode id=787 lang=rust
 *
 * [787] Cheapest Flights Within K Stops
 */

// @lc code=start
impl Solution {
    pub fn find_cheapest_price(n: i32, flights: Vec<Vec<i32>>, src: i32, dst: i32, k: i32) -> i32 {
        let mut distances: Vec<i32> = vec![i32::MAX; n as usize];
        distances[src as usize] = 0;

        for _ in 0..k + 1 {
            let mut new_distances: Vec<i32> = distances.clone();
            let mut updated: bool = false;

            for flight in &flights {
                let from: usize = flight[0] as usize;
                let to: usize = flight[1] as usize;
                let price: i32 = flight[2];

                if distances[from] != i32::MAX && distances[from] + price < new_distances[to] {
                    new_distances[to] = distances[from] + price;
                    updated = true;
                }
            }

            distances = new_distances;

            if !updated {
                break;
            }
        }

        if distances[dst as usize] == i32::MAX {
            -1
        } else {
            distances[dst as usize]
        }
    }
}
// @lc code=end
