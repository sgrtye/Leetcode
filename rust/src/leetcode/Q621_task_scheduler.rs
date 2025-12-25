/*
 * @lc app=leetcode id=621 lang=rust
 *
 * [621] Task Scheduler
 */

// @lc code=start
use std::collections::BinaryHeap;
use std::collections::HashMap;
use std::collections::VecDeque;

impl Solution {
    pub fn least_interval(tasks: Vec<char>, n: i32) -> i32 {
        let mut task_map: HashMap<char, i32> = HashMap::new();

        for &c in tasks.iter() {
            *task_map.entry(c).or_default() += 1
        }

        let mut task_heap: BinaryHeap<i32> = BinaryHeap::new();
        for (_, &value) in task_map.iter() {
            task_heap.push(value);
        }

        let mut time: i32 = 0;
        let mut processing: VecDeque<(i32, i32)> = VecDeque::new();

        while !processing.is_empty() || !task_heap.is_empty() {
            if let Some(count) = task_heap.pop() {
                if count != 1 {
                    processing.push_back((time + n, count - 1));
                }
            }

            if let Some(&(ready_time, count)) = processing.front() {
                if ready_time == time {
                    processing.pop_front();
                    task_heap.push(count);
                }
            }

            time += 1;
        }

        time
    }
}
// @lc code=end
