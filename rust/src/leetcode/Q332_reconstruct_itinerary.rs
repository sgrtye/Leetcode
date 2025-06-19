/*
 * @lc app=leetcode id=332 lang=rust
 *
 * [332] Reconstruct Itinerary
 */

// @lc code=start
use std::collections::HashMap;

impl Solution {
    fn hierholzers_dfs(
        adjecent_list: &mut HashMap<String, Vec<String>>,
        result: &mut Vec<String>,
        current: String,
    ) {
        while let Some(destinations) = adjecent_list.get_mut(&current) {
            if destinations.is_empty() {
                break;
            }

            let next: String = destinations.pop().unwrap();
            Self::hierholzers_dfs(adjecent_list, result, next);
        }

        result.push(current);
    }

    fn hierholzers_recursive(tickets: Vec<Vec<String>>) -> Vec<String> {
        let mut tickets: Vec<Vec<String>> = tickets;
        tickets.sort();
        tickets.reverse();

        let mut adjecent_list: HashMap<String, Vec<String>> = HashMap::new();
        for ticket in tickets {
            let from: String = ticket[0].clone();
            let to: String = ticket[1].clone();

            adjecent_list.entry(from).or_default().push(to);
        }

        let mut result: Vec<String> = Vec::new();
        Self::hierholzers_dfs(&mut adjecent_list, &mut result, String::from("JFK"));

        result.reverse();
        result
    }

    fn hierholzers_iterative(tickets: Vec<Vec<String>>) -> Vec<String> {
        let mut tickets: Vec<Vec<String>> = tickets;
        tickets.sort();
        tickets.reverse();

        let mut adjecent_list: HashMap<String, Vec<String>> = HashMap::new();
        for ticket in tickets {
            let from: String = ticket[0].clone();
            let to: String = ticket[1].clone();

            adjecent_list.entry(from).or_default().push(to);
        }

        let mut result: Vec<String> = Vec::new();
        let mut stack: Vec<String> = vec![String::from("JFK")];

        while let Some(current) = stack.pop() {
            if let Some(destinations) = adjecent_list.get_mut(&current) {
                if !destinations.is_empty() {
                    stack.push(current);
                    let next: String = destinations.pop().unwrap();
                    stack.push(next);
                } else {
                    result.push(current);
                }
            } else {
                result.push(current);
            }
        }

        result.reverse();
        result
    }

    pub fn find_itinerary(tickets: Vec<Vec<String>>) -> Vec<String> {
        Self::hierholzers_iterative(tickets)
    }
}
// @lc code=end
