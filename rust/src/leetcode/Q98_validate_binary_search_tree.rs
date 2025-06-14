/*
 * @lc app=leetcode id=98 lang=rust
 *
 * [98] Validate Binary Search Tree
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
    fn subtree_range(root: Option<Rc<RefCell<TreeNode>>>, min: i64, max: i64) -> bool {
        if let Some(node) = root {
            let value: i64 = node.borrow().val as i64;

            if !(min < value && value < max) {
                return false;
            }

            let left_valid = Self::subtree_range(node.borrow().left.clone(), min, value);
            let right_valid = Self::subtree_range(node.borrow().right.clone(), value, max);

            left_valid && right_valid
        } else {
            true
        }
    }

    pub fn is_valid_bst(root: Option<Rc<RefCell<TreeNode>>>) -> bool {
        Self::subtree_range(root, i64::MIN, i64::MAX)
    }
}
// @lc code=end
