#Task_1b
input = open("input1.txt")
output = open("output1b.txt", "w")

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

def Kahns(graph):
    in_degree = [0]*(vertex+1)
    for i in range(1,vertex+1):
        if graph[i] != []:
            for j in graph[i]:
                    in_degree[j] += 1
    count = 0
    top_sort = []
    queue = []
    for i in range(1,vertex):
        if in_degree[i] == 0:
            queue.append(i)

    while queue != []:
        vert = queue.pop(0)
        top_sort.append(vert)

        for adj_vert in graph[vert]:
            in_degree[adj_vert] -= 1
            if in_degree[adj_vert] == 0:
                queue.append(adj_vert)
        count += 1
    return top_sort, count

top_sort, count = Kahns(dict1)
if count != vertex:
    output.write("IMPOSSIBLE")
else:
    for i in top_sort: 
        output.write(f"{i} ")

output.close()

# First I made a graph using adjacency list (dict1). Then made a Kahn function
# The Kahn function takes graph as an argument. (dict1)
# It initializes two lists:
# in_degree: An array to store the indegree of each vertex.
# top_sort: An empty list to store the topologically sorted vertices.
# It iterates over the graph and calculates the indegree of each vertex by counting the number of incoming edges.
# It then initializes a queue and a count variable.
# The loop iterates through all vertices:
# If a vertex has an indegree of 0 (no incoming edges), it is added to the queue.
# The while loop runs until the queue is empty.
# The work of the loop:
# Pops a vertex from the queue and adds it to the top_sort list.
# Iterates over the outgoing neighbours of the popped vertex and decreases their indegree by 1.
# If any neighbour's indegree becomes 0, it is added to the queue.
# Increments the counter to track the number of processed vertices.
# Finally, it returns the top_sort list and the counter.
