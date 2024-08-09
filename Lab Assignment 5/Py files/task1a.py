#Task_1a
input = open("input1.txt")
output = open("output1a.txt", "w")

vert_edge = input.readline().strip().split(" ")
vert = int(vert_edge[0])
edges = int(vert_edge[1])

dict1 = {}
for key in range(1, vert+1):
  dict1[key] = []

start = 0
while start < edges:
    line = input.readline().strip().split(" ")
    dict1[int(line[0])].append(int(line[1]))
    start += 1

def detectCycle(graph, vert, visited=[], visiting=[]):
    if vert in visited:
        return False

    elif vert in visiting:
        return True

    visiting.append(vert)

    for adj_vert in graph[vert]:
        if detectCycle(graph, adj_vert, visited, visiting):
            return True

    visiting.remove(vert)
    visited.append(vert)

    return False

def dfs(vertex, graph, visited=[], sorted_lst=[]):
    visited.append(vertex)

    for adj_vert in graph[vertex]:
        if adj_vert not in visited:
            dfs(adj_vert, graph, visited, sorted_lst)

    sorted_lst.append(vertex)

def TopSort(graph):
    sorted_lst = []
    visited = []
    for i in range(1, vert+1):
        if i not in visited:
            if detectCycle(graph, i) == True:
                sorted_lst = []
                break
            else:
                dfs(i, graph, visited, sorted_lst)

    sorted_lst.reverse()
    return sorted_lst

result = TopSort(dict1)

if result != []:     
      for i in result: 
        output.write(f"{i} ")
else:
  output.write("IMPOSSIBLE")

output.close()


# The detectCycle  function implements a recursive depth-first search (DFS) to check if the graph contains any cycles
# The dfs function performs a DFS to find the topological order of the vertices in the DAG.
# It takes the graph graph, a starting vertex vertex, and two lists visited and sorted_lst as arguments.
# The function marks the vertex as visited and recursively explores its outgoing neighbours that haven't been visited yet.
# Once all neighbours have been explored, the vertex is added to the sorted_lst.
# The function TopSort uses the detectCycle and dfs functions to perform the topological sorting.
# It iterates over all vertices and checks for cycles using detectCycle. If a cycle is found, the sorted list is cleared and the function returns an empty list.
# Otherwise, it performs a DFS using dfs to find the topological order and reverses the order before returning it.