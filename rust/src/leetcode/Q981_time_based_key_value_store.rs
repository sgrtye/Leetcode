/*
 * @lc app=leetcode id=981 lang=rust
 *
 * [981] Time Based Key-Value Store
 */

// @lc code=start
use std::collections::HashMap;

struct TimeMap {
    map: HashMap<String, Vec<(String, i32)>>,
}

/**
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl TimeMap {
    fn new() -> Self {
        TimeMap {
            map: HashMap::new(),
        }
    }

    fn set(&mut self, key: String, value: String, timestamp: i32) {
        self.map
            .entry(key)
            .or_insert(vec![])
            .push((value, timestamp));
    }

    fn get(&self, key: String, timestamp: i32) -> String {
        static EMPTY: Vec<(String, i32)> = vec![];
        let saved = self.map.get(&key).unwrap_or(&EMPTY);

        let mut left: i32 = 0;
        let mut right: i32 = saved.len() as i32 - 1;

        while left <= right {
            let mid: i32 = left + (right - left) / 2;

            if saved[mid as usize].1 <= timestamp {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }

        if right >= 0 {
            saved[right as usize].0.clone()
        } else {
            String::new()
        }
    }
}

// /**
//  * Your TimeMap object will be instantiated and called as such:
//  * let obj = TimeMap::new();
//  * obj.set(key, value, timestamp);
//  * let ret_2: String = obj.get(key, timestamp);
//  */
// @lc code=end
