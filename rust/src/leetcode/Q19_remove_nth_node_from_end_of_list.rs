/*
 * @lc app=leetcode id=19 lang=rust
 *
 * [19] Remove Nth Node From End of List
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
    pub fn remove_nth_from_end(head: Option<Box<ListNode>>, n: i32) -> Option<Box<ListNode>> {
        let mut count: i32 = 0;
        let mut current: Option<&Box<ListNode>> = head.as_ref();

        while let Some(node) = current {
            count += 1;
            current = node.next.as_ref();
        }

        let mut dummy: Box<ListNode> = Box::new(ListNode::new(0));
        dummy.next = head;
        let mut dummy: Option<Box<ListNode>> = Some(dummy);

        let mut previous: Option<&mut Box<ListNode>> = dummy.as_mut();

        for _ in 0..(count - n) {
            previous = previous.unwrap().next.as_mut();
        }

        let node_to_remove: Option<Box<ListNode>> = previous.as_mut().unwrap().next.take();
        if let Some(node) = node_to_remove {
            previous.as_mut().unwrap().next = node.next;
        }

        dummy.unwrap().next
    }
}
// @lc code=end
