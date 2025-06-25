/*
 * @lc app=leetcode id=235 lang=rust
 *
 * [235] Lowest Common Ancestor of a Binary Search Tree
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
    fn lowest_common_ancestor_in_range(
        root: Option<Rc<RefCell<TreeNode>>>,
        left: i32,
        right: i32,
    ) -> Option<Rc<RefCell<TreeNode>>> {
        if let Some(node) = root {
            if node.borrow().val < left {
                Self::lowest_common_ancestor_in_range(node.borrow().right.clone(), left, right)
            } else if node.borrow().val > right {
                Self::lowest_common_ancestor_in_range(node.borrow().left.clone(), left, right)
            } else {
                Some(node)
            }
        } else {
            None
        }
    }

    pub fn lowest_common_ancestor(
        root: Option<Rc<RefCell<TreeNode>>>,
        p: Option<Rc<RefCell<TreeNode>>>,
        q: Option<Rc<RefCell<TreeNode>>>,
    ) -> Option<Rc<RefCell<TreeNode>>> {
        let p_value: i32 = p.unwrap().borrow().val;
        let q_value: i32 = q.unwrap().borrow().val;

        Self::lowest_common_ancestor_in_range(
            root.clone(),
            p_value.min(q_value),
            p_value.max(q_value),
        )
    }
}
// @lc code=end
