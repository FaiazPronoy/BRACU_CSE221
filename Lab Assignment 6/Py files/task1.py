#TASK_1
input = open("input1.txt")
output = open("output1.txt", "w")
import math
import heapq
vert, edges = [int(x) for x in input.readline().strip().split(" ")]

dict1 = {}
for i in range(1, vert+1):
  dict1[i] = []
start = 0
while start < edges:
  line = [int(x) for x in input.readline().strip().split()]
  dict1[line[0]].append([line[1], line[2]])
  start+= 1

source = int(input.readline().strip())

def Dijkstara(graph,initial):
  distance = [math.inf] * (vert+1)
  distance[initial] = 0

  visited = []
  queue = []
  queue.append([initial,0])
  visited.append(initial)

  while queue != []:
    heapq.heapify(queue)
    vertx, weight = heapq.heappop(queue)
    for adj_vert, dis in graph[vertx]:
        if  dis + distance[vertx] <  distance[adj_vert]:
          distance[adj_vert] = dis + distance[vertx]
          heapq.heappush(queue, [adj_vert, distance[adj_vert]])
          visited.append(adj_vert)
  return distance

distance = Dijkstara(dict1,source)
for i in range(1, len(distance)):
  if distance[i] == math.inf:
    output.write(f"-1 ")
  else:
    output.write(f"{distance[i]} ")

output.close()


# The code reads a graph from an input file, where the first line contains the number 
# of vertices and edges, and the following lines contain the edge data 
# (two vertices and the weight of the edge between them). The graph is represented
# as an adjacency list using a dictionary. It uses Dijkstra’s algorithm to find 
# the shortest path from each source vertex to all other vertices in the graph. 
# It keeps track of visited points and tentative distances, updating paths as 
# needed until all points are explored.The function alsouses a priority queue 
# to select the vertex with the smallest distance at each step.  Finally, it 
# writes the shortest distances to a new file, marking unreachable points with "-1".