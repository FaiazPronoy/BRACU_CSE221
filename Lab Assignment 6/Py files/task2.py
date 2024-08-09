#TASK_2
input = open("input2.txt")
output = open("output2.txt", "w")
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

source1, source2 = [int(x) for x in input.readline().strip().split(" ")]

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


Alice = Dijkstara(dict1,source1)
Bob = Dijkstara(dict1,source2)
Node = None
time = 0
for i in range(1,vert+1):
  if Node == None:
    Node = i
    time = max(Alice[i],Bob[i])
  elif Node != None:
    temp = max(Alice[i],Bob[i])
    if temp < time:
      time = temp
      Node = i


if time == math.inf or Node == None:
  output.write("Impossible")

elif time == 0 or Node == None:
  output.write("Impossible")

else:
  output.write(f"Time {time} \n")
  output.write(f"Node {Node}")

output.close()

# The code reads a graph from an input file, where the first line contains the number 
# of vertices and edges, and the following lines contain the edge data 
# (two vertices and the weight of the edge between them). The graph is represented
# as an adjacency list using a dictionary. The code then reads two source vertices 
# from the input file. It uses Dijkstra’s algorithm to find the shortest path 
# from each source vertex to all other vertices in the graph. The function
# uses a priority queue to select the vertex with the smallest distance at each step. 
# After finding the shortest paths, the code iterates over all vertices to find 
# the vertex that has the maximum shortest path distance from the two source 
# vertices. This is the vertex that takes the longest time to reach from both 
# source vertices. The time to reach this vertex and its index are written to an output file.