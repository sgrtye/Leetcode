/*
 * @lc app=leetcode id=84 lang=rust
 *
 * [84] Largest Rectangle in Histogram
 */

// @lc code=start
impl Solution {
    pub fn largest_rectangle_area(heights: Vec<i32>) -> i32 {
        let mut result: i32 = 0;
        let mut stack: Vec<(usize, i32)> = vec![];

        for i in 0..heights.len() {
            let mut start: usize = i;
            let current_height: i32 = heights[i];

            while !stack.is_empty() && current_height <= stack.last().unwrap().1 {
                let (index, height) = stack.pop().unwrap();

                if height * (i - index) as i32 > result {
                    result = height * (i - index) as i32;
                }

                start = index;
            }

            stack.push((start, current_height));
        }

        for (index, height) in stack {
            if height * (heights.len() - index) as i32 > result {
                result = height * (heights.len() - index) as i32;
            }
        }

        result
    }
}
// @lc code=end
