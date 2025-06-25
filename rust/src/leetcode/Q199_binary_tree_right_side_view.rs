/*
 * @lc app=leetcode id=199 lang=rust
 *
 * [199] Binary Tree Right Side View
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
    pub fn right_side_view(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<i32> {
        let mut result: Vec<i32> = vec![];
        let mut current_level: Vec<Option<Rc<RefCell<TreeNode>>>> = vec![root];

        while !current_level.is_empty() {
            let mut new_level: Vec<Option<Rc<RefCell<TreeNode>>>> = vec![];
            let mut level_result: Vec<i32> = vec![];

            for n in current_level.into_iter().flatten() {
                level_result.push(n.borrow().val);
                new_level.push(n.borrow().left.clone());
                new_level.push(n.borrow().right.clone());
            }

            if !level_result.is_empty() {
                result.push(*level_result.last().unwrap());
            }

            current_level = new_level;
        }

        result
    }
}
// @lc code=end
