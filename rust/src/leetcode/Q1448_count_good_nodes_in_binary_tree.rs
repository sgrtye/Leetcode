/*
 * @lc app=leetcode id=1448 lang=rust
 *
 * [1448] Count Good Nodes in Binary Tree
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
    fn count_good_nodes_with_cap(root: Option<Rc<RefCell<TreeNode>>>, mut cap: i32) -> i32 {
        if let Some(node) = root {
            let mut result: i32 = 0;

            if node.borrow().val >= cap {
                result += 1;
                cap = node.borrow().val;
            }

            result += Self::count_good_nodes_with_cap(node.borrow().left.clone(), cap);
            result += Self::count_good_nodes_with_cap(node.borrow().right.clone(), cap);

            result
        } else {
            0
        }
    }

    pub fn good_nodes(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        Self::count_good_nodes_with_cap(root, i32::MIN)
    }
}
// @lc code=end
