'''Q3: Implement the Depth-First Search algorithm for a graph. Test it on a sample graph and print the visited nodes.'''

from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs_util(self, v, visited):
        # Mark the current node as visited
        visited[v] = True
        print(v, end=' ')

        # Recur for all the adjacent vertices
        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                self.dfs_util(neighbor, visited)

    def dfs(self, start_node):
        # Initialize an array to keep track of visited nodes
        visited = [False] * (max(self.graph) + 1)

        # Call the utility function to perform DFS
        self.dfs_util(start_node, visited)

# Example usage:
# Let's create a sample graph and test the DFS algorithm

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

# Starting node for DFS
start_node = 1

print("DFS traversal starting from node", start_node, ":")
graph.dfs(start_node)

DFS traversal starting from node 1 :
1 2 4 5 3
