from collections import deque

def bfs(graph, start):
    # Initialize a queue fro BFS and add the start node
    queue = deque([start])
    # Set to keep track of visited nodes
    visited = set()
    # Mark the start node as visited 
    visited.add(start)

    while queue:
        # Dequeue a node from  the queue
        node = queue.popleft()
        print(node, end=" ")

        # Get all adjacent nodes of the dequeued node
        for neighbor in graph[node]:
            if neighbor not in visited:
                # If a neighbor has not been visited, mark it as visited and enqueue it
                visited.add(neighbor)
                queue.append(neighbor)

# Example graph as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# perform BFS starting from node 'A'
bfs(graph, 'A')
