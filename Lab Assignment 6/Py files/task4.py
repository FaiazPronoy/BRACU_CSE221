#TASK_4
import heapq

input_file = open("input4.txt")
output = open("output4.txt","w")
dict1 = {}

vert, edges = [int(x) for x in input_file.readline().strip().split(" ")]
for i in range(1, vert+1):
  dict1[i] = []
start = 0

while start < edges:
  line = [int(x) for x in input_file.readline().strip().split(" ")]
  dict1[line[0]].append([line[1], line[2]])
  dict1[line[1]].append([line[0], line[2]])
  start += 1

def Prims(graph, initial):
  min_cost = 0
  PQ = [(0, initial)]
  heapq.heapify(PQ)
  visited = [False] * (vert+1)

  while PQ != []:
    cost, edge = heapq.heappop(PQ)
    if not visited[edge]:
      visited[edge] = True
      min_cost += cost
    for i, j in graph[edge]:
      if not visited[i]:
        heapq.heappush(PQ, (j, i))
  return min_cost
  

result = Prims(dict1, 1)
output.write(f"{result}")
output.close()

# The undirected graph is represented as an adjacency list using a dictionary, 
# where each key-value pair represents a vertex and its adjacent vertices, respectively. 
# The code reads the graph data from an input file, where the first line contains 
# the number of vertices and edges, and the following lines contain the edge data 
# (two vertices and the cost of the edge between them). The Prims function implements 
# the algorithm, which starts from a source vertex and selects the edge with the smallest cost 
# that connects a visited and an unvisited vertex, until all vertices are visited. 
# The total cost of the selected edges, which is the cost of the minimum spanning tree, 
# is written to an output file. The priority queue operations are handled by the heapq module. 