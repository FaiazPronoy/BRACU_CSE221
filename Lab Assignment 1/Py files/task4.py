#Task_4
input = open("/content/input4.txt")
output = open("/content/output4.txt", "w")

train_name_dest = []
time = []

start = 0
num_of_elem = int(input.readline().strip())

while start < num_of_elem:
    line = input.readline()
    line_elem_lst = line.strip().split(" ")
    var1, var2, var3, var4, var5, var6, var7 = line_elem_lst
    train_name_dest.append([var1, var5])
    time.append(var7)
    start += 1

for i in range(num_of_elem):
    for j in range(i+1, num_of_elem):

        if train_name_dest[i][0] > train_name_dest[j][0]: #sorting lexicographically

            train_name_dest[i][0], train_name_dest[j][0] = train_name_dest[j][0], train_name_dest[i][0]

            train_name_dest[i][1], train_name_dest[j][1] = train_name_dest[j][1], train_name_dest[i][1]

            time[i], time[j] = time[j], time[i]

        elif train_name_dest[i][0] == train_name_dest[j][0] and time[i] < time[j]: #checking if there  is tie even after lexicographical sort and if it exists , then prioritizing the departure time

            train_name_dest[i][0], train_name_dest[j][0] = train_name_dest[j][0], train_name_dest[i][0]

            train_name_dest[i][1], train_name_dest[j][1] = train_name_dest[j][1], train_name_dest[i][1]

            time[i], time[j] = time[j], time[i]

for idx in range(num_of_elem):
  if idx != num_of_elem - 1:
    output.write(f'{train_name_dest[idx][0]} will departure for {train_name_dest[idx][1]} at {time[idx]}\n')
  else:
    output.write(f'{train_name_dest[idx][0]} will departure for {train_name_dest[idx][1]} at {time[idx]}')

output.close()