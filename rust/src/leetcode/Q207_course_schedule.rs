/*
 * @lc app=leetcode id=207 lang=rust
 *
 * [207] Course Schedule
 */

// @lc code=start
impl Solution {
    pub fn can_finish(num_courses: i32, prerequisites: Vec<Vec<i32>>) -> bool {
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
        while !current.is_empty() {
            finished += 1;
            let course: usize = current.pop().unwrap();

            for &advanced_course in &prerequisites_map[course] {
                indegrees[advanced_course] -= 1;
                if indegrees[advanced_course] == 0 {
                    current.push(advanced_course);
                }
            }
        }

        finished == num_courses
    }
}
// @lc code=end
