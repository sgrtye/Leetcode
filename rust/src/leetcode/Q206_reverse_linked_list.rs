/*
 * @lc app=leetcode id=206 lang=rust
 *
 * [206] Reverse Linked List
 */

// Definition for singly-linked list.
#[derive(PartialEq, Eq, Clone, Debug)]
pub struct ListNode {
    pub val: i32,
    pub next: Option<Box<ListNode>>,
}

impl ListNode {
    #[inline]
    fn new(val: i32) -> Self {
        ListNode { next: None, val }
    }
}

// @lc code=start
impl Solution {
    pub fn reverse_list(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        let mut previous: Option<Box<ListNode>> = None;
        let mut current: Option<Box<ListNode>> = head;

        while let Some(mut node) = current {
            current = node.next.take();
            node.next = previous;
            previous = Some(node);
        }

        previous
    }
}
// @lc code=end
