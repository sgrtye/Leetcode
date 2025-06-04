/*
 * @lc app=leetcode id=49 lang=rust
 *
 * [49] Group Anagrams
 */

// @lc code=start
use std::collections::HashMap;

impl Solution {
    pub fn group_anagrams(strs: Vec<String>) -> Vec<Vec<String>> {
        let mut map: HashMap<String, Vec<String>> = HashMap::new();

        for str in strs {
            let mut chars: Vec<char> = str.chars().collect();
            chars.sort();
            let key: String = chars.into_iter().collect();

            map.entry(key).or_insert(vec![]).push(str);
        }

        map.into_values().collect()
    }
}
// @lc code=end
