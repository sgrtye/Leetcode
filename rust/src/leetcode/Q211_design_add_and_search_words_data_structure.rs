/*
 * @lc app=leetcode id=211 lang=rust
 *
 * [211] Design Add and Search Words Data Structure
 */

// @lc code=start
use std::collections::HashMap;

struct TrieNode {
    children: HashMap<char, Box<TrieNode>>,
    word: bool,
}

impl TrieNode {
    #[inline]
    fn new() -> Self {
        TrieNode {
            children: HashMap::new(),
            word: false,
        }
    }
}

struct WordDictionary {
    start: TrieNode,
}

/**
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl WordDictionary {
    fn new() -> Self {
        WordDictionary {
            start: TrieNode::new(),
        }
    }

    fn add_word(&mut self, word: String) {
        let mut current: &mut TrieNode = &mut self.start;

        for c in word.chars() {
            current = current
                .children
                .entry(c)
                .or_insert(Box::new(TrieNode::new()));
        }

        current.word = true;
    }

    fn search_range(chars: &Vec<char>, node: &TrieNode, index: usize) -> bool {
        if index != chars.len() {
            if chars[index] == '.' {
                return node
                    .children
                    .values()
                    .any(|child| Self::search_range(chars, child, index + 1));
            }

            if let Some(next_node) = node.children.get(&chars[index]) {
                Self::search_range(chars, next_node, index + 1)
            } else {
                false
            }
        } else {
            node.word
        }
    }

    fn search(&self, word: String) -> bool {
        let chars: Vec<char> = word.chars().collect();
        Self::search_range(&chars, &self.start, 0)
    }
}

// /**
//  * Your WordDictionary object will be instantiated and called as such:
//  * let obj = WordDictionary::new();
//  * obj.add_word(word);
//  * let ret_2: bool = obj.search(word);
//  */
// @lc code=end
