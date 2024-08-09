input = open("input5.txt")
output = open("output5.txt", "w")

vert_edge_target = input.readline().strip().split(" ")
vert = int(vert_edge_target[0])
edges = int(vert_edge_target[1])
target = int(vert_edge_target[2])

dict1 = {}
for key in range(1, vert+1):
  dict1[key] = []

start = 0
while start < edges:
    line = input.readline().strip().split(" ")
    dict1[int(line[0])].append(int(line[1]))
    dict1[int(line[1])].append(int(line[0]))
    start += 1


def shortestPath(graph, root, target):
    path = []
    path.append(root)
    if root == target:
        return path
    queue = []
    visited = []
    queue.append((root, path))
    visited.append(root)
    while queue:
        vertex, current_path = queue.pop(0)
        for neighbor in graph[vertex]:
            if neighbor == target:
                return current_path + [neighbor]
            elif neighbor not in visited:
                new_path = current_path + [neighbor]
                queue.append((neighbor, new_path))
                visited.append(neighbor)
    return []

path = shortestPath(dict1, 1, target)
time = len(path)-1

if path != []:
    str1 = " ".join(map(str, path))
    output.write(f"Time: {time}\n")
    output.write(f"Shortest Path: {str1}")
else:
  output.write("NO PATH")

output.close()

# Defined a function shortestPath that performs Breadth-First Search (BFS) to find the shortest path between a root node and a target node in a graph represented by an adjacency list (graph).
# Initializes a list path with the root node.
# Checks if the root node is the target, and if so, returns the path.
# Initializes a queue with tuples containing a vertex and its current path, and a list of visited vertices.
# Enters a while loop that continues until the queue is empty.
# Dequeues a vertex and its current path from the queue.
# Checks if the vertex is the target, and if so, returns the current path.
# Otherwise, adds the neighboring vertices to the queue if they haven't been visited.
# Returns an empty list if no path is found.