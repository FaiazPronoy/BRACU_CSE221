import numpy as np
input = open("input1a.txt")
output = open("output1a.txt", "w")

vert_edge = input.readline().strip().split(" ")
row = int(vert_edge[0]) + 1
col = int(vert_edge[0]) + 1
edges = int(vert_edge[1])

matrix = np.zeros((row, col), dtype = int)
start = 0

while start < edges:
  line = input.readline().strip().split(" ")
  for i in range(row):
    for j in range(col):
      if i == int(line[0]) and j == int(line[1]):
        matrix[i][j] = int(line[2]) # I used nested loops to iterate over the matrix. If the current indices match the indices provided in the input line, the corresponding element in the matrix is updated with the value from the input line.
        break
  start += 1

for i in range(row):
    for j in range(col):
        output.write(f"{matrix[i][j]} ")
    output.write("\n")
output.close()

# Created a square matrix of size (vertice + 1)^2. Then put the row, column , and weight in the matrix. Finally write the matrix.
