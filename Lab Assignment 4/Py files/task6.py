import numpy as np
input = open("input6.txt")
output = open("output6.txt", "w")

vert_edge = input.readline().strip().split(" ")
row = int(vert_edge[0])
col = int(vert_edge[1])

matrix = np.zeros((row, col), dtype = str)

for i in range(row):
    line = list(input.readline()[:col])
    for j in range(col):
      matrix[i][j] = line[j]

def max_diamonds_in_jumanji(R, H, graph):
    def dfs(row, col):
        if row < 0 or row >= R or col < 0 or col >= H or graph[row][col] == '#' or visited[row][col]:
            return 0

        visited[row][col] = True
        diamonds = 0 #initializing diamonds with 0 and updating it later to 1 if D found

        if graph[row][col] == 'D':
            diamonds = 1

        # Exploring adjacent cells in all four directions
        diamonds += dfs(row + 1, col)
        diamonds += dfs(row - 1, col)
        diamonds += dfs(row, col + 1)
        diamonds += dfs(row, col - 1)

        return diamonds

    visited = [[False for i in range(H)] for i in range(R)]
    max_diamonds = 0 #as diamonds inside the dfs funtion is a local variable we need to keep track of the max diamonds collected
    for i in range(R):
        for j in range(H):
            if graph[i][j] == '.' and not visited[i][j]:

                max_diamonds = max(max_diamonds,dfs(i, j))

    return max_diamonds

result = max_diamonds_in_jumanji(row,col,matrix)
output.write(f"{result}")
output.close()

# Defined a function max_diamonds_in_jumanji that takes the dimensions of the grid (R and H) and the grid itself (graph) as input.
# Inside this function, defines a recursive depth-first search (DFS) function (dfs) that explores adjacent cells to count diamonds.
# Initializes a 2D list visited to keep track of visited cells.
# Initializes a variable max_diamonds to keep track of the maximum diamonds collected.
# Iterates through each cell in the grid and calls the DFS function if the cell is empty ('.') and has not been visited.
# Updates max_diamonds with the maximum count of diamonds obtained.
# Calls the max_diamonds_in_jumanji function with the dimensions and matrix obtained from the input file.
# Writes the result to the output file.