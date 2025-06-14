/*
 * @lc app=leetcode id=110 lang=rust
 *
 * [110] Balanced Binary Tree
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
    fn is_balanced_with_depth(root: Option<Rc<RefCell<TreeNode>>>) -> (bool, i32) {
        if let Some(node) = root {
            let (left_balanced, left_depth) =
                Self::is_balanced_with_depth(node.borrow_mut().left.clone());
            let (right_balanced, right_depth) =
                Self::is_balanced_with_depth(node.borrow_mut().right.clone());

            let self_balanced: bool =
                left_balanced && right_balanced && (left_depth - right_depth).abs() <= 1;

            (self_balanced, max(left_depth, right_depth) + 1)
        } else {
            (true, 0)
        }
    }

    pub fn is_balanced(root: Option<Rc<RefCell<TreeNode>>>) -> bool {
        Self::is_balanced_with_depth(root).0
    }
}
// @lc code=end
