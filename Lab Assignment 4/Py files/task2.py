input = open("input2.txt")
output = open("output2.txt", "w")

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


def BFS(graph, initial_vert): 
 
  queue = [] #For vertices to visit
  visited = [] #For keeping track of visited vertices
  result = [] #For storing the order of visited vertices.
  queue.append(initial_vert)
  visited.append(initial_vert)

  while queue != []: 
      vertex = queue.pop(0) #Dequeues a vertex from the queue, 
      result.append(vertex) #appends it to the result list

      for adj_vert in graph[vertex]:
          if adj_vert not in visited:
             queue.append(adj_vert) #Enqueues adjacent vertices to the queue if they have not been visited.
             visited.append(adj_vert) 
  return result

result = BFS(dict1, 1)
for item in result:
  output.write(f"{item} ")
output.close()
#I Made a graph using adjacency list from the input.
#Used the concept of Queue data structure in the BFS function(FIFO) which performs Breadth-First Search on a graph represented by an adjacency list.
#Visit the keys of the adjacency list until the queue is empty.
#Finally, writes the items of the result list in the output file.
