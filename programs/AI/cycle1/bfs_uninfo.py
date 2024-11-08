from collections import deque

def bfs(graph,start,goal):
    queue=[start]
    visited=[start]
    predecessor={start:None}

    while queue:
        current_node=queue.pop(0)
        if current_node==goal:
            break
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.append(neighbor)
                predecessor[neighbor]=current_node
    
    path=[]
    if goal in visited:
        current=goal
        while current is not None:
            path.append(current)
            current=predecessor[current]
        path.reverse()
        return path
    else:
        return "no path exists"
    
graph={
    'a':['b','c'],
    'b':['d','e'],
    'c':['f'],
    'd':[],
    'e':['g'],
    'f':[],
    'g':[]
}

start='a'
goal='f'
path=bfs(graph,start,goal)
print("path from start to goal\n",path)