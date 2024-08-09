input = open("input1b.txt")
output = open("output1b.txt", "w")

vert_edge = input.readline().strip().split(" ")
vert = int(vert_edge[0])
edges = int(vert_edge[1])

dict1 = {}
for key in range(vert+1):
  dict1[key] = []  #Created an empty dictionary named dict1 and initialized it with keys from 0 to vert (inclusive), each mapped to an empty list.

start = 0
while start < edges:
    line = input.readline().strip().split(" ")
    for key in dict1:              #Used nested loop to iterate over the keys of dict1.
      if key == int(line[0]):
        dict1[key].append(tuple([int(line[1]), int(line[2])])) #If the current key matches the first element of the input line, it appends a tuple of the second and third elements of the input line to the corresponding list in dict1 key.
    start += 1

for key, value in dict1.items():
  if value == []:
    output.write(f"{key}: \n")
  else:
    value_str = ""
    for item in value:
      value_str += str(item) + " "
    output.write(f"{key}: {value_str} \n")

output.close()
#Created a dictionary from O to vertice (inclusive). Then put the destination and weight as a tuple inside the key. Finally printed the dictionary.
