'''Q4: Implement the Breadth-First Search algorithm for a graph. Apply BFS to find the shortest path between two nodes in a graph.'''

from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)  # For an undirected graph

    def bfs_shortest_path(self, start_node, end_node):
        visited = set()
        queue = deque([(start_node, [start_node])])

        while queue:
            current_node, path = queue.popleft()

            if current_node == end_node:
                return path  # Return the shortest path if the end node is reached

            if current_node not in visited:
                visited.add(current_node)

                for neighbor in self.graph[current_node]:
                    if neighbor not in visited:
                        queue.append((neighbor, path + [neighbor]))

        return None  # Return None if there is no path between the start and end nodes

# Example usage:
# Let's create a sample graph and find the shortest path between two nodes

# Sample graph:
#    1
#   / \
#  2   3
# / \
# 4  5

graph = Graph()
graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(2, 4)
graph.add_edge(2, 5)

# Nodes to find the shortest path between
start_node = 1
end_node = 5

shortest_path = graph.bfs_shortest_path(start_node, end_node)

if shortest_path:
    print(f"Shortest path between nodes {start_node} and {end_node}:", shortest_path)
else:
    print(f"No path found between nodes {start_node} and {end_node}.")

Shortest path between nodes 1 and 5: [1, 2, 5]
