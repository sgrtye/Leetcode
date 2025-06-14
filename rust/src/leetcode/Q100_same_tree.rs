/*
 * @lc app=leetcode id=100 lang=rust
 *
 * [100] Same Tree
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
    pub fn is_same_tree(
        p: Option<Rc<RefCell<TreeNode>>>,
        q: Option<Rc<RefCell<TreeNode>>>,
    ) -> bool {
        match (p, q) {
            (None, None) => true,
            (Some(node1), Some(node2)) => {
                if node1.borrow().val == node2.borrow().val {
                    Self::is_same_tree(
                        node1.borrow_mut().left.clone(),
                        node2.borrow_mut().left.clone(),
                    ) && Self::is_same_tree(
                        node1.borrow_mut().right.clone(),
                        node2.borrow_mut().right.clone(),
                    )
                } else {
                    false
                }
            }
            _ => false,
        }
    }
}
// @lc code=end
