/*
 * @lc app=leetcode id=226 lang=rust
 *
 * [226] Invert Binary Tree
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

impl Solution {
    pub fn invert_tree(root: Option<Rc<RefCell<TreeNode>>>) -> Option<Rc<RefCell<TreeNode>>> {
        if let Some(node) = root {
            let left = node.borrow_mut().left.clone();
            let right = node.borrow_mut().right.clone();

            node.borrow_mut().left = Self::invert_tree(right);
            node.borrow_mut().right = Self::invert_tree(left);

            Some(node)
        } else {
            None
        }
    }
}
// @lc code=end
