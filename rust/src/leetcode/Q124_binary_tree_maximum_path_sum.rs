/*
 * @lc app=leetcode id=124 lang=rust
 *
 * [124] Binary Tree Maximum Path Sum
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
    fn contained_and_included_path(root: Option<Rc<RefCell<TreeNode>>>) -> (i32, i32) {
        if let Some(node) = root {
            let (left_contained, left_included) =
                Self::contained_and_included_path(node.borrow().left.clone());
            let (right_contained, right_included) =
                Self::contained_and_included_path(node.borrow().right.clone());

            let left_updated: i32 = max(left_included, 0);
            let right_updated: i32 = max(right_included, 0);

            let sub_contained: i32 = max(left_contained, right_contained);
            let contaiend: i32 = max(
                sub_contained,
                left_updated + right_updated + node.borrow().val,
            );

            let included: i32 = max(left_updated, right_updated) + node.borrow().val;

            (contaiend, included)
        } else {
            (i32::MIN, 0)
        }
    }

    pub fn max_path_sum(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        Self::contained_and_included_path(root).0
    }
}
// @lc code=end
