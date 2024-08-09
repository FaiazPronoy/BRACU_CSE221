#Task_1a

input = open("/content/input1a.txt")
output = open("/content/output1a.txt", "w")

len = int(input.readline())

for idx in range(len):
  if idx != len-1:
    var1 = int(input.readline())
    if int(var1) % 2 == 0:
      output.write(f"{var1} is an Even number.\n")
    else:
      output.write(f"{var1} is an Odd number.\n")

  else:
    var1 = int(input.readline())
    if int(var1) % 2 == 0:
      output.write(f"{var1} is an Even number.")
    else:
      output.write(f"{var1} is an Odd number.")

output.close()
