/*
 * @lc app=leetcode id=230 lang=rust
 *
 * [230] Kth Smallest Element in a BST
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
    fn inorder(root: Option<Rc<RefCell<TreeNode>>>, remained: &mut i32) -> Option<i32> {
        if let Some(node) = root {
            if let Some(result) = Self::inorder(node.borrow().left.clone(), remained) {
                return Some(result);
            }

            *remained -= 1;
            if *remained == 0 {
                return Some(node.borrow().val);
            }

            Self::inorder(node.borrow().right.clone(), remained)
        } else {
            None
        }
    }

    pub fn kth_smallest(root: Option<Rc<RefCell<TreeNode>>>, k: i32) -> i32 {
        let mut remained: i32 = k;
        Self::inorder(root, &mut remained).unwrap()
    }
}
// @lc code=end
