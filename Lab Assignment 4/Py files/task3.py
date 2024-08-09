input = open("input3.txt")
output = open("output3.txt", "w")

vert_edge = input.readline().strip().split(" ")
vert = int(vert_edge[0])
edges = int(vert_edge[1])

dict1 = {}
for key in range(vert+1):
  dict1[key] = []

start = 0
while start < edges:
    line = input.readline().strip().split(" ")
    dict1[int(line[0])].append(int(line[1]))
    dict1[int(line[1])].append(int(line[0]))
    start += 1


def DFS(graph, vertex, visited):

  if vertex not in visited:
        visited.append(vertex)

        for adj_vert in graph[vertex]:
            DFS(graph, adj_vert, visited)

  return visited

result = DFS(dict1, 1, [])

for items in result:
  output.write(f"{items} ")

output.close()
# I Made a graph using adjacency list from the input.
# Defined a function DFS that performs Depth-First Search on a graph represented by an adjacency list.
# Takes the graph, current vertex (vertex), and a list of visited vertices (visited).
# If the current vertex is not in the visited list, appends it to the visited list and recursively calls the DFS function on its adjacent vertices.
#Finally, writes the items of the result list in the output file.
