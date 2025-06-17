/*
 * @lc app=leetcode id=127 lang=rust
 *
 * [127] Word Ladder
 */

// @lc code=start
use std::collections::HashMap;
use std::collections::HashSet;

impl Solution {
    pub fn ladder_length(begin_word: String, end_word: String, word_list: Vec<String>) -> i32 {
        if !word_list.contains(&end_word) {
            return 0;
        }

        let mut adjecent_list: HashMap<String, Vec<String>> = HashMap::new();
        let mut all_words: Vec<String> = word_list.clone();
        all_words.push(begin_word.clone());

        for word in &all_words {
            for j in 0..word.len() {
                let pattern: String = format!("{}*{}", &word[..j], &word[j + 1..]);
                adjecent_list.entry(pattern).or_default().push(word.clone());
            }
        }

        let mut result: i32 = 0;
        let mut current: Vec<String> = vec![begin_word.clone()];
        let mut visit: HashSet<String> = HashSet::from([begin_word.clone()]);

        while !current.is_empty() {
            result += 1;
            let mut next: Vec<String> = Vec::new();

            for _ in 0..current.len() {
                let word: String = current.pop().unwrap();
                if word == end_word {
                    return result;
                }

                for j in 0..word.len() {
                    let pattern: String = format!("{}*{}", &word[..j], &word[j + 1..]);

                    if let Some(neighbors) = adjecent_list.get(&pattern) {
                        for neighbor_word in neighbors {
                            if !visit.contains(neighbor_word) {
                                visit.insert(neighbor_word.clone());
                                next.push(neighbor_word.clone());
                            }
                        }
                    }
                }
            }

            current = next;
        }

        0
    }
}
// @lc code=end
