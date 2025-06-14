/*
 * @lc app=leetcode id=543 lang=rust
 *
 * [543] Diameter of Binary Tree
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
    fn depth_and_diameter_of_subtree(root: Option<Rc<RefCell<TreeNode>>>) -> (i32, i32) {
        if let Some(node) = root {
            let (left_depth, left_diameter) =
                Self::depth_and_diameter_of_subtree(node.borrow_mut().left.clone());
            let (right_depth, right_diameter) =
                Self::depth_and_diameter_of_subtree(node.borrow_mut().right.clone());

            let max_depth: i32 = max(left_depth, right_depth) + 1;
            let max_subtree_diameter: i32 = max(left_diameter, right_diameter);
            let max_diameter: i32 = max(max_subtree_diameter, left_depth + right_depth);

            (max_depth, max_diameter)
        } else {
            (0, 0)
        }
    }

    pub fn diameter_of_binary_tree(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        Self::depth_and_diameter_of_subtree(root).1
    }
}
// @lc code=end
