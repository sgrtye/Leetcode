/*
 * @lc app=leetcode id=684 lang=rust
 *
 * [684] Redundant Connection
 */

// @lc code=start
struct UnionFind {
    parents: Vec<usize>,
}

impl UnionFind {
    fn new(size: usize) -> Self {
        Self {
            parents: (0..size).collect(),
        }
    }

    fn find(&mut self, n: usize) -> usize {
        let mut current: usize = n;

        while current != self.parents[current] {
            self.parents[current] = self.parents[self.parents[current]];
            current = self.parents[current];
        }

        current
    }

    fn union(&mut self, num1: usize, num2: usize) -> bool {
        let p1: usize = self.find(num1);
        let p2: usize = self.find(num2);

        if p1 != p2 {
            self.parents[p1] = p2;
            true
        } else {
            false
        }
    }
}

impl Solution {
    pub fn find_redundant_connection(edges: Vec<Vec<i32>>) -> Vec<i32> {
        let mut union: UnionFind = UnionFind::new(edges.len());

        for edge in edges {
            if !union.union(edge[0] as usize - 1, edge[1] as usize - 1) {
                return vec![edge[0], edge[1]];
            }
        }

        Vec::new()
    }
}
// @lc code=end
