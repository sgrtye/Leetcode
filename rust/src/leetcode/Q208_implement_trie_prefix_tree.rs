/*
 * @lc app=leetcode id=208 lang=rust
 *
 * [208] Implement Trie (Prefix Tree)
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

struct Trie {
    start: TrieNode,
}

/**
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl Trie {
    fn new() -> Self {
        Trie {
            start: TrieNode::new(),
        }
    }

    fn insert(&mut self, word: String) {
        let mut current: &mut TrieNode = &mut self.start;

        for c in word.chars() {
            current = current
                .children
                .entry(c)
                .or_insert(Box::new(TrieNode::new()));
        }

        current.word = true;
    }

    fn search(&self, word: String) -> bool {
        let mut current: &TrieNode = &self.start;

        for c in word.chars() {
            if let Some(next_node) = current.children.get(&c) {
                current = next_node;
            } else {
                return false;
            }
        }

        current.word
    }

    fn starts_with(&self, prefix: String) -> bool {
        let mut current: &TrieNode = &self.start;

        for c in prefix.chars() {
            if let Some(next_node) = current.children.get(&c) {
                current = next_node;
            } else {
                return false;
            }
        }

        true
    }
}

// /**
//  * Your Trie object will be instantiated and called as such:
//  * let obj = Trie::new();
//  * obj.insert(word);
//  * let ret_2: bool = obj.search(word);
//  * let ret_3: bool = obj.starts_with(prefix);
//  */
// @lc code=end
