/*
 * @lc app=leetcode id=297 lang=rust
 *
 * [297] Serialize and Deserialize Binary Tree
 */

// Definition for a binary tree node.
#[derive(Debug, PartialEq, Eq)]
pub struct TreeNode {
    pub val: i32,
    pub left: Option<Rc<RefCell<TreeNode>>>,
    pub right: Option<Rc<RefCell<TreeNode>>>,
}

impl TreeNode {
    #[inline]
    pub fn new(val: i32) -> Self {
        TreeNode {
            val,
            left: None,
            right: None,
        }
    }
}

// @lc code=start
use std::cell::RefCell;
use std::rc::Rc;

struct Codec {}

/**
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl Codec {
    fn new() -> Self {
        Self {}
    }

    fn preorder_traversal(root: Option<Rc<RefCell<TreeNode>>>, nodes: &mut Vec<String>) {
        if let Some(node) = root {
            nodes.push(node.borrow().val.to_string());

            Self::preorder_traversal(node.borrow().left.clone(), nodes);
            Self::preorder_traversal(node.borrow().right.clone(), nodes);
        } else {
            nodes.push(String::from("N"));
        }
    }

    fn serialize(&self, root: Option<Rc<RefCell<TreeNode>>>) -> String {
        let mut nodes: Vec<String> = vec![];
        Self::preorder_traversal(root, &mut nodes);

        nodes.join(",")
    }

    fn build_node(nodes: &Vec<&str>, index: &mut usize) -> Option<Rc<RefCell<TreeNode>>> {
        *index += 1;

        if nodes[*index - 1] == "N" {
            return None;
        }

        let value: i32 = nodes[*index - 1].parse().unwrap();

        let node: Rc<RefCell<TreeNode>> = Rc::new(RefCell::new(TreeNode::new(value)));

        node.borrow_mut().left = Self::build_node(nodes, index);
        node.borrow_mut().right = Self::build_node(nodes, index);

        Some(node)
    }

    fn deserialize(&self, data: String) -> Option<Rc<RefCell<TreeNode>>> {
        let nodes: Vec<&str> = data.split(",").collect();
        let mut index: usize = 0;

        Self::build_node(&nodes, &mut index)
    }
}

// /**
//  * Your Codec object will be instantiated and called as such:
//  * let obj = Codec::new();
//  * let data: String = obj.serialize(strs);
//  * let ans: Option<Rc<RefCell<TreeNode>>> = obj.deserialize(data);
//  */
// @lc code=end
