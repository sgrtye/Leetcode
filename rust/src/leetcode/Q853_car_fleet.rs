/*
 * @lc app=leetcode id=853 lang=rust
 *
 * [853] Car Fleet
 */

// @lc code=start
impl Solution {
    pub fn car_fleet(target: i32, position: Vec<i32>, speed: Vec<i32>) -> i32 {
        let mut cars: Vec<(i32, i32)> = position.into_iter().zip(speed).collect();
        cars.sort();
        cars.reverse();

        let required_time: Vec<f64> = cars
            .into_iter()
            .map(|(p, s)| (target - p) as f64 / s as f64)
            .collect();

        let mut result: i32 = 1;
        let mut previous_time: f64 = required_time[0];

        for time in required_time {
            if time > previous_time {
                previous_time = time;
                result += 1;
            }
        }

        result
    }
}
// @lc code=end
