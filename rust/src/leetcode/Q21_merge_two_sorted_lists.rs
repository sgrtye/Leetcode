/*
 * @lc app=leetcode id=21 lang=rust
 *
 * [21] Merge Two Sorted Lists
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
    pub fn merge_two_lists(
        list1: Option<Box<ListNode>>,
        list2: Option<Box<ListNode>>,
    ) -> Option<Box<ListNode>> {
        let mut list1: Option<Box<ListNode>> = list1;
        let mut list2: Option<Box<ListNode>> = list2;

        let mut dummy: Box<ListNode> = Box::new(ListNode::new(0));
        let mut current: &mut Box<ListNode> = &mut dummy;

        loop {
            match (&list1, &list2) {
                (Some(node1), Some(node2)) => {
                    if node1.val <= node2.val {
                        let next: Option<Box<ListNode>> = list1.as_mut().unwrap().next.take();
                        current.next = list1.take();
                        current = current.next.as_mut().unwrap();
                        list1 = next;
                    } else {
                        let next: Option<Box<ListNode>> = list2.as_mut().unwrap().next.take();
                        current.next = list2.take();
                        current = current.next.as_mut().unwrap();
                        list2 = next;
                    }
                }
                (Some(_), _) => {
                    current.next = list1.take();
                    break;
                }
                (_, Some(_)) => {
                    current.next = list2.take();
                    break;
                }
                (None, None) => break,
            }
        }

        dummy.next
    }
}
// @lc code=end
