input = open("input4.txt")
output = open("output4.txt", "w")

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


def detectCycle(graph, vert, visited, visiting):
        if vert in visited:
            return False

        if vert in visiting:
            return True

        visiting.append(vert)

        for adj_vert in graph[vert]:
            if detectCycle(graph, adj_vert, visited, visiting):
                return True

        visiting.remove(vert)
        visited.append(vert)

        return False

visiting = []
visited = []

result = detectCycle(dict1, 1, visited, visiting)
if result == True:
  output.write("YES")
else:
  output.write("NO")
output.close()

# Defines a function detectCycle that uses Depth-First Search (DFS) to detect cycles in a graph represented by an adjacency list (graph).
# Takes the graph, current vertex (vert), a list of visited vertices (visited), and a list of vertices currently being visited (visiting).
# If the current vertex is in the visited list, returns False (no cycle).
# If the current vertex is in the visiting list, returns True (cycle detected).
# Appends the current vertex to the visiting list.
# Recursively calls the detectCycle function on adjacent vertices.
# Removes the current vertex from the visiting list and appends it to the visited list.
# Returns False if no cycle is detected.