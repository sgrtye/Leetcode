/*
 * @lc app=leetcode id=25 lang=rust
 *
 * [25] Reverse Nodes in k-Group
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
    pub fn reverse_k_group(head: Option<Box<ListNode>>, k: i32) -> Option<Box<ListNode>> {
        let mut count: i32 = 0;
        let mut current: &Option<Box<ListNode>> = &head;
        while let Some(node) = current {
            count += 1;
            if count == k {
                break;
            }
            current = &node.next;
        }

        if count < k {
            return head;
        }

        let mut previous: Option<Box<ListNode>> = None;
        let mut current: Option<Box<ListNode>> = head;

        for _ in 0..k {
            if let Some(mut node) = current {
                let next: Option<Box<ListNode>> = node.next.take();
                node.next = previous;
                previous = Some(node);
                current = next;
            }
        }

        if let Some(ref mut tail) = previous {
            let mut tail_node: &mut Box<ListNode> = tail;
            while tail_node.next.is_some() {
                tail_node = tail_node.next.as_mut().unwrap();
            }
            tail_node.next = Self::reverse_k_group(current, k);
        }

        previous
    }
}
// @lc code=end
