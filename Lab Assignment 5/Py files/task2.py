#Task_2
import heapq
input = open("input2.txt")
output = open("output2.txt", "w")

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
        heapq.heapify(queue)
        vert = heapq.heappop(queue)
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

# This code is very similar to the code for Task_1b, with the only difference being the use of a heap.
# The Kahn function uses heapq.heapify(queue) to initialize the queue as a heap.
# Instead of a simple queue.pop(0), the function uses heapq.heappop(queue) to remove the element with the highest priority (lowest indegree in this case) from the queue.
# All other logic remains the same.
# I used to get the lexicographical output.