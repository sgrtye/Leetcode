/*
 * @lc app=leetcode id=2 lang=rust
 *
 * [2] Add Two Numbers
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
    pub fn add_two_numbers(
        l1: Option<Box<ListNode>>,
        l2: Option<Box<ListNode>>,
    ) -> Option<Box<ListNode>> {
        let mut dummy: Option<Box<ListNode>> = Some(Box::new(ListNode::new(0)));
        let mut current: &mut Option<Box<ListNode>> = &mut dummy.as_mut().unwrap().next;

        let mut carry: i32 = 0;
        let mut l1: Option<Box<ListNode>> = l1;
        let mut l2: Option<Box<ListNode>> = l2;

        while l1.is_some() || l2.is_some() || carry == 1 {
            let mut sum: i32 = carry;

            if let Some(node) = l1.take() {
                sum += node.val;
                l1 = node.next;
            }

            if let Some(node) = l2.take() {
                sum += node.val;
                l2 = node.next;
            }

            carry = sum / 10;
            sum = sum % 10;

            *current = Some(Box::new(ListNode::new(sum)));
            current = &mut current.as_mut().unwrap().next;
        }

        dummy.unwrap().next
    }
}
// @lc code=end
