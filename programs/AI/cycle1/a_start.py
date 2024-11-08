import heapq

class Node:
    def __init__(self, name, heuristics):
        self.name = name
        self.heuristics = heuristics
        self.neighbors = {}
        self.g = float('inf')
        self.parent = None

    def add_neighbor(self, neighbor, cost):
        self.neighbors[neighbor] = cost

    def __lt__(self, other):
        return (self.g + self.heuristics) < (other.g + other.heuristics)

def a_star(start, goal):
    open_list = []
    start.g = 0
    heapq.heappush(open_list, start)

    while open_list:
        current_node = heapq.heappop(open_list)
        
        if current_node == goal:
            return reconstruct_path(goal)
        
        for neighbor, cost in current_node.neighbors.items():
            tentative_g = current_node.g + cost
            if tentative_g < neighbor.g:
                neighbor.g = tentative_g
                neighbor.parent = current_node
                heapq.heappush(open_list, neighbor)
    
    print("Goal node not found")
    return None

def reconstruct_path(goal):
    path = []
    current = goal
    while current:
        path.append(current.name)
        current = current.parent
    return path[::-1]

# Example usage
if __name__ == "__main__":
    a = Node('A', 5)
    b = Node('B', 3)
    c = Node('C', 1)
    d = Node('D', 2)
    e = Node('E', 0)
    a.add_neighbor(b, 1)
    b.add_neighbor(c, 4)
    c.add_neighbor(d, 2)
    c.add_neighbor(e, 3)
    d.add_neighbor(e, 1)

    path = a_star(a, e)
    if path:
        print("Path found:", " -> ".join(path))
