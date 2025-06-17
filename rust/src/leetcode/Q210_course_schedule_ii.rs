/*
 * @lc app=leetcode id=210 lang=rust
 *
 * [210] Course Schedule II
 */

// @lc code=start
impl Solution {
    pub fn find_order(num_courses: i32, prerequisites: Vec<Vec<i32>>) -> Vec<i32> {
        let mut indegrees: Vec<usize> = vec![0; num_courses as usize];
        let mut prerequisites_map: Vec<Vec<usize>> = vec![vec![]; num_courses as usize];

        for prerequisite in prerequisites {
            indegrees[prerequisite[0] as usize] += 1;
            prerequisites_map[prerequisite[1] as usize].push(prerequisite[0] as usize);
        }

        let mut current: Vec<usize> = indegrees
            .iter()
            .enumerate()
            .filter_map(|(course, &indegree)| (indegree == 0).then_some(course))
            .collect();

        let mut finished: i32 = 0;
        let mut result: Vec<i32> = Vec::new();
        while !current.is_empty() {
            finished += 1;

            let course: usize = current.pop().unwrap();
            result.push(course as i32);

            for &advanced_course in &prerequisites_map[course] {
                indegrees[advanced_course] -= 1;
                if indegrees[advanced_course] == 0 {
                    current.push(advanced_course);
                }
            }
        }

        if finished == num_courses {
            result
        } else {
            Vec::new()
        }
    }
}
// @lc code=end
