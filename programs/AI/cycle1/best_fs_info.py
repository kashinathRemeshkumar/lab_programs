class Node:
    def __init__(self, name, heuristics):
        self.name = name
        self.heuristics = heuristics
        self.neighbors = {}

    def add_neighbor(self, neighbor, cost):
        self.neighbors[neighbor] = cost

def bfs(start, goal):
    open_list = [start]
    closed_list = set()

    while open_list:
        current_node = min(open_list, key=lambda node: node.heuristics)
        open_list.remove(current_node)
        print(f"Expanding node: {current_node.name}")
        
        if current_node.name == goal.name:
            print(f"Goal node {goal.name} found")
            return
        closed_list.add(current_node)
        for neighbor in current_node.neighbors:
            if neighbor in closed_list or neighbor in open_list:
                continue
            open_list.append(neighbor)
    print("Goal node not found")

if __name__ == "__main__":
    a = Node('A',5)
    b = Node('B',3)
    c = Node('C',1)
    d = Node('D',2)
    e = Node('E',0)
    a.add_neighbor(b, 1)
    b.add_neighbor(c, 4)
    c.add_neighbor(d, 2)
    d.add_neighbor(e, 3)
    d.add_neighbor(e, 1)
    bfs(a, c)
