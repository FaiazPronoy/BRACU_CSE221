#TASK_3
input = open("input3.txt")
output = open("output3.txt","w")
query = []

vert , edge  = [int(x) for x in input.readline().strip().split(" ")]
start = 0
while start < edge:
  node, des = [int(x) for x in input.readline().strip().split(" ")]

  query.append((node, des)) #this query will store the node and it's adjacent node
  start += 1
count = [1] * (vert+1) #
par = [i for i in range(vert+1)] #initially everyone's parent is they themselves

def find(r):
  if par[r] == r:
    return r
  return find(par[r])

def union(a,b):
  global rank
  rank = [0]*(vert+1) # Parent will be decided based on the rank of a node
  u = find(a)
  v = find(b)
  if u ==v :
    return
  elif rank[u] < rank[v]: #node with higher rank becomes delegate or parent when 2 people become friend
    par[u] = v
    count[v]+=count[u] #delegate's friend number updating
  elif rank[v] < rank[u]:
    par[v] = u
    count[u] += count[v]
  else:
    par[v] = u
    rank[u] += 1
    count[u]+= count[v]

circle_size = []
for k in query:
    i, j = k
    union(i,j)
    circle_size.append(count[find(i)])

for i in circle_size:
  output.write(f"{str(i)}\n")

output.close()

# This code be used for merging groups based on friendships  and tracking their size. 
# I used a function called "Union-Find" to efficiently identify the biggest bunch 
# of friends, ensuring no one gets left out. Each time two friends connect, 
# their circles merge, and the code keeps tabs on the largest one, ultimately 
# revealing its size in the output file. 