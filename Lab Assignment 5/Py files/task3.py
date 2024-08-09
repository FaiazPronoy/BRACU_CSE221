#Task_3
input = open("input3.txt")
output = open("output3.txt", "w")

vert_edge = input.readline().strip().split(" ")
vertex = int(vert_edge[0])
edges = int(vert_edge[1])

dict1 = {}
for key in range(1, vertex+1):
  dict1[key] = []

start = 0
while start < edges:
    line = input.readline().strip().split(" ")
    dict1[int(line[0])].append(int(line[1]))
    start += 1

def dfs(v, graph, visited, stack):
    visited[v] = True
    for neighbor in graph[v]:
        if not visited[neighbor]:

            dfs(neighbor, graph, visited, stack)
    stack.append(v)

def transpose(graph):
    transposed = {}
    for key in range(1, vertex+1):
      transposed[key] = []
    for u in graph:
        for v in graph[u]:
            transposed[v].append(u)
    return transposed

def kosaraju(graph, vertexes):
    stack = []
    visited = [False] * (vertexes+1)

    for i in range(1,vertexes+1):
        if not visited[i]:
            dfs(i, graph, visited, stack)

    transposed_graph = transpose(graph)

    visited = [False] * (vertexes+1)
    scc = []
    while stack:
        current = stack.pop()
        if not visited[current]:
            result = []
            dfs(current, transposed_graph, visited, result)
            result.sort()
            scc.append(result)
    scc.sort(key=lambda x: min(x))
    for result in scc:
        for i in result:
            output.write(f"{i} ")
        output.write("\n")
        
kosaraju(dict1,vertex)
output.close()


# The kosaraju function performs two DFS passes:
# First DFS on the original graph, using the dfs function. This filled the stack with nodes in reverse topological order of their SCCs.
# Transpose: The transpose function creates a transpose of the original graph by reversing the direction of edges.
# Second DFS on the transposed graph, starting from nodes in the stack. This identifies all nodes reachable from each node, forming individual SCCs.
# The scc list stores the identified SCCs as lists of nodes.
