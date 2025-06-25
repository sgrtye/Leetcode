/*
 * @lc app=leetcode id=1584 lang=rust
 *
 * [1584] Min Cost to Connect All Points
 */

// @lc code=start
use std::cmp::Reverse;
use std::collections::BinaryHeap;

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

    fn connected(&mut self, num1: usize, num2: usize) -> bool {
        self.find(num1) == self.find(num2)
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
    fn kruskals(points: Vec<Vec<i32>>) -> i32 {
        let mut edges: Vec<(i32, usize, usize)> = Vec::new();
        for i in 0..points.len() {
            let i_x: i32 = points[i][0];
            let i_y: i32 = points[i][1];

            for j in i + 1..points.len() {
                let j_x: i32 = points[j][0];
                let j_y: i32 = points[j][1];
                let distance: i32 = (i_x - j_x).abs() + (i_y - j_y).abs();

                edges.push((distance, i, j));
                edges.push((distance, j, i));
            }
        }
        edges.sort();

        let mut result: i32 = 0;
        let mut union: UnionFind = UnionFind::new(points.len());

        for (distance, source, target) in edges {
            if !union.connected(source, target) {
                result += distance;
                union.union(source, target);
            }
        }

        result
    }

    fn prims(points: Vec<Vec<i32>>) -> i32 {
        let mut adjacent_list: Vec<Vec<(i32, usize)>> = vec![vec![]; points.len()];
        for i in 0..points.len() {
            let i_x: i32 = points[i][0];
            let i_y: i32 = points[i][1];

            for j in i + 1..points.len() {
                let j_x: i32 = points[j][0];
                let j_y: i32 = points[j][1];
                let distance: i32 = (i_x - j_x).abs() + (i_y - j_y).abs();

                adjacent_list[i].push((distance, j));
                adjacent_list[j].push((distance, i));
            }
        }

        let mut result: i32 = 0;
        let mut connected: Vec<bool> = vec![false; points.len()];
        let mut heap: BinaryHeap<(Reverse<i32>, usize)> = BinaryHeap::new();
        heap.push((Reverse(0), 0));

        while !heap.is_empty() {
            let (Reverse(distance), vertex) = heap.pop().unwrap();

            if connected[vertex] {
                continue;
            }

            result += distance;
            connected[vertex] = true;

            for &(new_distance, target) in &adjacent_list[vertex] {
                if !connected[target] {
                    heap.push((Reverse(new_distance), target));
                }
            }
        }

        result
    }

    fn prims_eager(points: Vec<Vec<i32>>) -> i32 {
        let mut result: i32 = 0;
        let mut vertex: usize = 0;
        let mut connected: Vec<bool> = vec![false; points.len()];
        let mut distances: Vec<i32> = vec![i32::MAX; points.len()];
        distances[0] = 0;

        for _ in 0..points.len() {
            connected[vertex] = true;
            result += distances[vertex];

            let vertex_x: i32 = points[vertex][0];
            let vertex_y: i32 = points[vertex][1];
            let mut next_vertex: usize = usize::MAX;

            for j in 0..points.len() {
                if connected[j] {
                    continue;
                }

                let j_x: i32 = points[j][0];
                let j_y: i32 = points[j][1];
                let distance: i32 = (vertex_x - j_x).abs() + (vertex_y - j_y).abs();

                distances[j] = distance.min(distances[j]);
                if next_vertex == usize::MAX || distances[j] < distances[next_vertex] {
                    next_vertex = j;
                }
            }

            vertex = next_vertex;
        }

        result
    }

    pub fn min_cost_connect_points(points: Vec<Vec<i32>>) -> i32 {
        Self::prims(points)
    }
}
// @lc code=end
