def solve_csp_backtracking(graph, colors):
    # Check if we can assign a color to a node without conflict
    def is_safe(node, color, assignment):
        for neighbor in graph[node]:  # Check each neighboring node
            if assignment.get(neighbor) == color:  # If neighbor has the same color, return False
                return False
        return True  # No conflicts, so it's safe to assign the color

    # Backtracking function to assign colors to all nodes
    def backtrack(assignment):
        # If every node has a color, we found a solution
        if len(assignment) == len(graph):
            return assignment

        # Pick the next unassigned node
        for node in graph:
            if node not in assignment:
                for color in colors:
                    # Try assigning each color to the node
                    if is_safe(node, color, assignment):
                        assignment[node] = color  # Assign color to the node
                        result = backtrack(assignment)  # Recur to assign colors to remaining nodes
                        if result:  # If we find a solution, return it
                            return result
                        del assignment[node]  # If no solution, remove color and backtrack
                return None  # No valid color assignments found for this node
        return None

    # Start backtracking with an empty assignment
    return backtrack({})

# Example graph and colors
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D', 'E'],
    'D': ['B', 'C', 'E'],
    'E': ['C', 'D']
}

colors = ['Red', 'Blue', 'Green']
solution = solve_csp_backtracking(graph, colors)

# Print the result
if solution:
    print("Solution found:")
    for node, color in solution.items():
        print(f"Node {node}: Color {color}")
else:
    print("No solution found")
