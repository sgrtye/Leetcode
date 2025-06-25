/*
 * @lc app=leetcode id=23 lang=rust
 *
 * [23] Merge k Sorted Lists
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
    fn merge_two_lists(
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

    pub fn merge_k_lists(lists: Vec<Option<Box<ListNode>>>) -> Option<Box<ListNode>> {
        let mut lists: Vec<Option<Box<ListNode>>> = lists;

        while lists.len() > 1 {
            let mut new_lists: Vec<Option<Box<ListNode>>> = vec![];

            while lists.len() >= 2 {
                new_lists.push(Self::merge_two_lists(
                    lists.pop().unwrap(),
                    lists.pop().unwrap(),
                ));
            }

            if !lists.is_empty() {
                new_lists.push(lists.pop().unwrap());
            }

            lists = new_lists;
        }

        if lists.is_empty() {
            None
        } else {
            lists.pop().unwrap()
        }
    }
}
// @lc code=end
