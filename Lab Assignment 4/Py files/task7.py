input = open("input7.txt")
output = open("output7.txt", "w")

vert_line = input.readline()
vert = int(vert_line)
edges = vert-1

dict1 = {}
for key in range(1, vert+1):
  dict1[key] = []

start = 0
while start < edges:
    line = input.readline().strip().split(" ")
    dict1[int(line[0])].append(int(line[1]))
    dict1[int(line[1])].append(int(line[0]))
    start += 1

def dfs(graph, node, parent, distance):
    farthest_node = node
    max_distance = distance
    for neighbor in graph[node]:
        if neighbor != parent:
            neighbor_node, neighbor_distance = dfs(graph, neighbor, node, distance+1)
            if neighbor_distance > max_distance:
                farthest_node = neighbor_node
                max_distance = neighbor_distance
    return farthest_node, max_distance


node1, distance1 = dfs(dict1, 1, 0, 0)
node2, distance2 = dfs(dict1, node1, 0, 0)

output.write(f"{node1} {node2}")
output.close()