/*
 * @lc app=leetcode id=143 lang=rust
 *
 * [143] Reorder List
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
    pub fn reorder_list(head: &mut Option<Box<ListNode>>) {
        if head.is_none() || head.as_ref().unwrap().next.is_none() {
            return;
        }

        let mut count: i32 = 0;
        let mut current: Option<&Box<ListNode>> = head.as_ref();

        while let Some(node) = current {
            count += 1;
            current = node.next.as_ref();
        }

        let mid_point: i32 = count / 2;

        let mut tail: &mut Option<Box<ListNode>> = head;

        for _ in 0..mid_point {
            tail = &mut tail.as_mut().unwrap().next;
        }

        let mut previous: Option<Box<ListNode>> = None;
        let mut current: Option<Box<ListNode>> = tail.take();

        while let Some(mut node) = current {
            current = node.next.take();
            node.next = previous;
            previous = Some(node);
        }

        let mut first_half: Option<Box<ListNode>> = head.take();
        let mut second_half: Option<Box<ListNode>> = previous;

        let mut dummy: Option<Box<ListNode>> = Some(Box::new(ListNode::new(0)));
        let mut current: &mut Option<Box<ListNode>> = &mut dummy;

        while first_half.is_some() || second_half.is_some() {
            if let Some(mut node) = first_half.take() {
                first_half = node.next.take();
                current.as_mut().unwrap().next = Some(node);
                current = &mut current.as_mut().unwrap().next;
            }

            if let Some(mut node) = second_half.take() {
                second_half = node.next.take();
                current.as_mut().unwrap().next = Some(node);
                current = &mut current.as_mut().unwrap().next;
            }
        }

        *head = dummy.unwrap().next;
    }
}
// @lc code=end
