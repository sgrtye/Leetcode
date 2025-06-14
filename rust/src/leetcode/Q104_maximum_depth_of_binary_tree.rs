/*
 * @lc app=leetcode id=104 lang=rust
 *
 * [104] Maximum Depth of Binary Tree
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
use std::cmp::max;
use std::rc::Rc;

impl Solution {
    pub fn max_depth(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        if let Some(node) = root {
            let left_count = Self::max_depth(node.borrow_mut().left.clone());
            let right_count = Self::max_depth(node.borrow_mut().right.clone());

            max(left_count, right_count) + 1
        } else {
            0
        }
    }
}
// @lc code=end
