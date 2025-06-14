/*
 * @lc app=leetcode id=105 lang=rust
 *
 * [105] Construct Binary Tree from Preorder and Inorder Traversal
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
use std::collections::HashMap;
use std::rc::Rc;

impl Solution {
    fn build_node(
        preorder: &Vec<i32>,
        inorder_map: &HashMap<i32, i32>,
        preorder_index: &mut usize,
        left: i32,
        right: i32,
    ) -> Option<Rc<RefCell<TreeNode>>> {
        if left > right {
            return None;
        }

        let value: i32 = preorder[*preorder_index];
        let node: Rc<RefCell<TreeNode>> = Rc::new(RefCell::new(TreeNode::new(value)));
        *preorder_index += 1;

        if left == right {
            return Some(node);
        }

        let inorder_index: i32 = inorder_map[&value];

        node.borrow_mut().left = Self::build_node(
            preorder,
            inorder_map,
            preorder_index,
            left,
            inorder_index - 1,
        );
        node.borrow_mut().right = Self::build_node(
            preorder,
            inorder_map,
            preorder_index,
            inorder_index + 1,
            right,
        );

        Some(node)
    }

    pub fn build_tree(preorder: Vec<i32>, inorder: Vec<i32>) -> Option<Rc<RefCell<TreeNode>>> {
        let mut inorder_map: HashMap<i32, i32> = HashMap::new();
        for (index, value) in inorder.iter().enumerate() {
            inorder_map.entry(*value).or_insert(index as i32);
        }

        let mut preorder_index: usize = 0;

        Self::build_node(
            &preorder,
            &inorder_map,
            &mut preorder_index,
            0,
            preorder.len() as i32 - 1,
        )
    }
}
// @lc code=end
