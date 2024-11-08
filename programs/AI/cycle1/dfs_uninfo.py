def dfs(graph, start, goal):
    open_list = [start]
    closed_list = []
    path = {start: None}
    
    while open_list:
        current_node = open_list.pop()
        
        if current_node == goal:
            return reconstruct(path, start, goal)
        
        if current_node not in closed_list:
            closed_list.append(current_node)
            
            for neighbor in graph[current_node]:
                if neighbor not in closed_list:
                    open_list.append(neighbor)
                    path[neighbor] = current_node
    
    

def reconstruct(path, start, goal):
    current_node = goal
    reconstructed_path = []
    
    while current_node is not None:
        reconstructed_path.append(current_node)
        current_node = path[current_node]
    
    reconstructed_path.reverse()
    return reconstructed_path

# Example usage:
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

start = 'A'
goal = 'F'
print(dfs(graph, start, goal))  # Output: ['A', 'C', 'F']
