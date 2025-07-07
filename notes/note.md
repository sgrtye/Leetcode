# Algorithm Notes

## Binary Search
- **Use case**: Finding elements in sorted arrays
- **Time complexity**: O(log n)

## Graph Algorithms

### Kahn's Algorithm (Topological Sort)
- **Data structures**: Graph, adjacency list, indegree count
- **Process**: Collect nodes with 0 indegree, process in order
- **Related problems**: [207](../python/Q207_course_schedule.py)

### Minimum Spanning Tree (MST)

#### Kruskal's Algorithm (Union Find)
- **Use case**: Connecting components
- **Process**: Sort edges, choose smallest edge connecting two parts
- **Related problems**: [1584](../rust/src/leetcode/Q1584_min_cost_to_connect_all_points.rs), [684](../pythonQ684_redundant_connection.py)

#### Prim's Algorithm
- **Data structures**: Heap or indexed priority queue
- **Process**: Keep adding smallest edge already attached
- **Related problems**: [1584](../rust/src/leetcode/Q1584_min_cost_to_connect_all_points.rs)

### Shortest Path Algorithms
![Shortest Path Algorithms](<Shortest Path Algorithms.png>)

#### Floyd-Warshall
- **Use case**: All-pair shortest path, detect negative cycles
- **Time complexity**: O(V³)
- **Process**: DP-like approach, adding midpoint to reduce cost, run V times
- **Related problems**: [743](../rust/src/leetcode/Q743_network_delay_time.rs)

#### Bellman-Ford
- **Use case**: Single source shortest path, detect negative cycles
- **Time complexity**: O(VE)
- **Process**: Loop V-1 times over all vertices finding minimum distance
- **Related problems**: [743](../rust/src/leetcode/Q743_network_delay_time.rs)

#### Dijkstra's Algorithm
- **Use case**: Single source shortest path (non-negative weights)
- **Time complexity**: O((V + E) log E)
- **Process**: Min heap for visitable nodes, visit cells greedily
- **Related problems**: [743](../rust/src/leetcode/Q743_network_delay_time.rs), [778](../rust/src/leetcode/Q778_swim_in_rising_water.rs)

### Eulerian Path/Circuit
![Eulerian Path & Circuit](<Eulerian Path & Circuit.png>)

#### Hierholzer's Algorithm
- **Use case**: Finding Eulerian path/circuit
- **Process**: Shared adjacency list, DFS, add to list when 0 outdegree reached, reverse path
- **Related problems**: [332](../rust/src/leetcode/Q332_reconstruct_itinerary.rs)