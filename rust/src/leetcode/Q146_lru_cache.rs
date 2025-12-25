/*
 * @lc app=leetcode id=146 lang=rust
 *
 * [146] LRU Cache
 */

// @lc code=start
use std::collections::HashMap;

struct Node {
    key: i32,
    value: i32,
    previous: Option<usize>,
    next: Option<usize>,
}

impl Node {
    fn new(key: i32, value: i32) -> Self {
        Node {
            key,
            value,
            previous: None,
            next: None,
        }
    }
}

struct LRUCache {
    capacity: usize,
    dict: HashMap<i32, usize>,
    nodes: Vec<Node>,
    start: Option<usize>, // Head (LRU)
    end: Option<usize>,   // Tail (MRU)
}

/**
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl LRUCache {
    fn new(capacity: i32) -> Self {
        let cap = capacity as usize;
        LRUCache {
            capacity: cap,
            dict: HashMap::with_capacity(cap),
            nodes: Vec::with_capacity(cap),
            start: None,
            end: None,
        }
    }

    fn get(&mut self, key: i32) -> i32 {
        if let Some(&index) = self.dict.get(&key) {
            self.remove_node(index);
            self.attach(index);
            self.nodes[index].value
        } else {
            -1
        }
    }

    fn put(&mut self, key: i32, value: i32) {
        // Key exists
        if let Some(&index) = self.dict.get(&key) {
            self.nodes[index].value = value;
            self.remove_node(index);
            self.attach(index);
            return;
        }

        // Cache not full
        if self.dict.len() < self.capacity {
            let index = self.nodes.len();
            self.nodes.push(Node::new(key, value));
            self.attach(index);
            self.dict.insert(key, index);
            return;
        }

        // Cache full
        let lru_index = self.start.unwrap();
        let lru_key = self.nodes[lru_index].key;
        self.dict.remove(&lru_key);

        self.remove_node(lru_index);

        self.nodes[lru_index].key = key;
        self.nodes[lru_index].value = value;
        self.attach(lru_index);
        self.dict.insert(key, lru_index);
    }

    fn remove_node(&mut self, index: usize) {
        let prev = self.nodes[index].previous;
        let next = self.nodes[index].next;

        if let Some(p) = prev {
            self.nodes[p].next = next;
        } else {
            self.start = next;
        }

        if let Some(n) = next {
            self.nodes[n].previous = prev;
        } else {
            self.end = prev;
        }

        self.nodes[index].previous = None;
        self.nodes[index].next = None;
    }

    fn attach(&mut self, index: usize) {
        if let Some(e) = self.end {
            self.nodes[e].next = Some(index);
            self.nodes[index].previous = Some(e);
            self.nodes[index].next = None;
            self.end = Some(index);
        } else {
            // First node in the list
            self.start = Some(index);
            self.end = Some(index);
            self.nodes[index].previous = None;
            self.nodes[index].next = None;
        }
    }
}

/*
 * Your LRUCache object will be instantiated and called as such:
 * let obj = LRUCache::new(capacity);
 * let ret_1: i32 = obj.get(key);
 * obj.put(key, value);
 */
// @lc code=end
