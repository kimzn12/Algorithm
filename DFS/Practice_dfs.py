def dfs(graph, v, visited):
    visited[v] = True
    print(v)

    for i in graph[v]:
        if visited[i] is False: # if not visited[i]
            dfs(graph,i,visited)




graph = [
    [],
    [2,3],
    [2,7],
    [1,6],
    [5,7],
    [3,4],
    [3],
    [4,8],
    [7]
]

visited = [False] * 9

dfs(graph, 1, visited)