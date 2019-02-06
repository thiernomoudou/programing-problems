from collections import deque


# dephth first search using the iterative approach

def dfs(graph, start):
    stack, visited = [start], set()
    while stack:
        vertex = stack.pop()
        for neighbour in graph[vertex]:
            if not neighbour in visited:
                visited.add(neighbour)
                stack.append(neighbour)
    return visited

# breadth first search using the iterative approach

def bfs(graph, start):
    queue, visited = deque([start]), set()
    while queue:
        vertex = queue.popleft()
        for neighbour in graph[vertex]:
            if not neighbour in visited:
                visited.add(neighbour)
                queue.append(neighbour)
    return visited

graph = {0: [1, 2], 1: [2], 2: [3], 3: [1,2]} 
print(bfs(graph, 0))

