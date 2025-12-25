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

        for (i, h) in heights.iter().enumerate() {
            let mut start: usize = i;

            while let Some(&(index, height)) = stack.last() {
                if h <= &height {
                    stack.pop();

                    if height * (i - index) as i32 > result {
                        result = height * (i - index) as i32;
                    }

                    start = index;
                } else {
                    break
                }
            }

            stack.push((start, *h));
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
