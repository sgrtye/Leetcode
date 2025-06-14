/*
 * @lc app=leetcode id=212 lang=rust
 *
 * [212] Word Search II
 */

// @lc code=start
use std::collections::HashMap;
use std::collections::HashSet;

struct TrieNode {
    children: HashMap<char, Box<TrieNode>>,
    word: bool,
}

impl TrieNode {
    #[inline]
    fn new() -> Self {
        TrieNode {
            children: HashMap::new(),
            word: false,
        }
    }
}

impl Solution {
    fn dictionary(words: Vec<String>, node: &mut TrieNode) {
        for word in words {
            let mut current: &mut TrieNode = node;

            for c in word.chars() {
                current = current
                    .children
                    .entry(c)
                    .or_insert(Box::new(TrieNode::new()));
            }

            current.word = true;
        }
    }

    fn dfs(
        row: i32,
        col: i32,
        board: &Vec<Vec<char>>,
        visited: &mut HashSet<(i32, i32)>,
        current: &mut Vec<char>,
        node: &TrieNode,
        result: &mut HashSet<String>,
    ) {
        if row < 0
            || col < 0
            || row >= board.len() as i32
            || col >= board[0].len() as i32
            || visited.contains(&(row, col))
        {
            return;
        }

        if let Some(next_node) = node.children.get(&board[row as usize][col as usize]) {
            visited.insert((row, col));
            current.push(board[row as usize][col as usize]);

            if next_node.word {
                result.insert(current.iter().collect());
            }

            Self::dfs(
                row + 1,
                col,
                board,
                visited,
                current,
                next_node,
                result,
            );
            Self::dfs(
                row - 1,
                col,
                board,
                visited,
                current,
                next_node,
                result,
            );
            Self::dfs(
                row,
                col + 1,
                board,
                visited,
                current,
                next_node,
                result,
            );
            Self::dfs(
                row,
                col - 1,
                board,
                visited,
                current,
                next_node,
                result,
            );

            visited.remove(&(row, col));
            current.pop();
        }
    }

    pub fn find_words(board: Vec<Vec<char>>, words: Vec<String>) -> Vec<String> {
        let mut root = TrieNode::new();
        Self::dictionary(words, &mut root);

        let mut current: Vec<char> = vec![];
        let mut visited: HashSet<(i32, i32)> = HashSet::new();

        let mut result: HashSet<String> = HashSet::new();

        for i in 0..board.len() {
            for j in 0..board[0].len() {
                Self::dfs(
                    i as i32,
                    j as i32,
                    &board,
                    &mut visited,
                    &mut current,
                    &root,
                    &mut result,
                );
            }
        }

        result.into_iter().collect()
    }
}
// @lc code=end
