
from collections import deque

def bfs(graph, start):
    visited = set([])
    queue = deque()
    visited.add(start)
    queue.append(start)

    while queue:
        val = queue.popleft()
        print(val)
        for neighbor in graph[val]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)

    return visited









graph = {'0': set(['1', '2']),
         '1': set(['0', '3', '4']),
         '2': set(['0']),
         '3': set(['1']),
         '4': set(['2', '3'])}

bfs(graph, '0')