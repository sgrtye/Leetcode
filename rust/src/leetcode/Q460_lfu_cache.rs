/*
 * @lc app=leetcode id=460 lang=rust
 *
 * [460] LFU Cache
 */

// @lc code=start
use std::cell::RefCell;
use std::collections::HashMap;
use std::rc::Rc;

struct Node {
    key: i32,
    value: i32,
    count: i32,
    previous: Option<Rc<RefCell<Node>>>,
    next: Option<Rc<RefCell<Node>>>,
}

impl Node {
    fn new(key: i32, value: i32) -> Self {
        Node {
            key,
            value,
            count: 1,
            previous: None,
            next: None,
        }
    }
}

struct LinkedList {
    start: Rc<RefCell<Node>>,
    end: Rc<RefCell<Node>>,
    size: i32,
}

impl LinkedList {
    fn new() -> Self {
        let start: Rc<RefCell<Node>> = Rc::new(RefCell::new(Node::new(-1, -1)));
        let end: Rc<RefCell<Node>> = Rc::new(RefCell::new(Node::new(-1, -1)));

        start.borrow_mut().next = Some(end.clone());
        end.borrow_mut().previous = Some(start.clone());

        LinkedList {
            start,
            end,
            size: 0,
        }
    }

    fn add_to_head(&mut self, node: Rc<RefCell<Node>>) {
        let tmp = self.start.borrow().next.clone().unwrap();

        self.start.borrow_mut().next = Some(node.clone());
        node.borrow_mut().next = Some(tmp.clone());

        node.borrow_mut().previous = Some(self.start.clone());
        tmp.borrow_mut().previous = Some(node.clone());

        self.size += 1;
    }

    fn remove_node(&mut self, node: Rc<RefCell<Node>>) {
        let previous = node.borrow().previous.clone().unwrap();
        let next = node.borrow().next.clone().unwrap();

        previous.borrow_mut().next = Some(next.clone());
        next.borrow_mut().previous = Some(previous.clone());

        self.size -= 1;
    }

    fn remove_from_tail(&mut self) -> Rc<RefCell<Node>> {
        let node = self.end.borrow().previous.clone().unwrap();

        self.remove_node(node.clone());

        node
    }
}

struct LFUCache {
    capacity: i32,
    node_dict: HashMap<i32, Rc<RefCell<Node>>>,
    f_dict: HashMap<i32, LinkedList>,
    min_f: i32,
}

/**
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl LFUCache {
    fn new(capacity: i32) -> Self {
        LFUCache {
            capacity,
            node_dict: HashMap::new(),
            f_dict: HashMap::new(),
            min_f: 0,
        }
    }

    fn update(&mut self, node: Rc<RefCell<Node>>) {
        let current_count = node.borrow().count;

        self.f_dict
            .get_mut(&current_count)
            .unwrap()
            .remove_node(node.clone());

        node.borrow_mut().count += 1;

        self.f_dict
            .entry(current_count + 1)
            .or_insert(LinkedList::new())
            .add_to_head(node.clone());

        if current_count == self.min_f && self.f_dict.get(&self.min_f).unwrap().size == 0 {
            self.min_f += 1;
        }
    }

    fn get(&mut self, key: i32) -> i32 {
        if !self.node_dict.contains_key(&key) {
            return -1;
        }

        let node = self.node_dict.get(&key).cloned().unwrap();
        self.update(node.clone());

        return node.borrow().value;
    }

    fn put(&mut self, key: i32, value: i32) {
        if self.capacity == 0 {
            return;
        }

        if let Some(node) = self.node_dict.get(&key).cloned() {
            node.borrow_mut().value = value;
            self.update(node);
            return;
        }

        if self.node_dict.len() as i32 == self.capacity {
            let list = self.f_dict.get_mut(&self.min_f).unwrap();
            let removed_node = list.remove_from_tail();
            self.node_dict.remove(&removed_node.borrow().key);
        }

        let new_node = Rc::new(RefCell::new(Node::new(key, value)));
        self.node_dict.insert(key, new_node.clone());
        self.f_dict
            .entry(1)
            .or_insert(LinkedList::new())
            .add_to_head(new_node);

        self.min_f = 1;
    }
}

/*
 * Your LFUCache object will be instantiated and called as such:
 * let obj = LFUCache::new(capacity);
 * let ret_1: i32 = obj.get(key);
 * obj.put(key, value);
 */
// @lc code=end
