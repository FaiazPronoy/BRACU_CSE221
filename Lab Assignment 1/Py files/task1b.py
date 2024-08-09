#Task_1b
input = open("/content/input1b.txt")
output = open("/content/output1b.txt", "w")

start = 0
num_of_test_case = int(input.readline())

while start < num_of_test_case:

  if start != num_of_test_case-1:
      line = input.readline()
      var1, var2, var3, var4 = line.split(" ")

      if var3 == "+":
        result = int(var2) + int(var4)
        output.write("The result of " + var2 + " " + var3 + " " + var4 + " is "  + str(result) + "\n")

      elif var3 == "-":
        result = int(var2) - int(var4)
        output.write("The result of " + var2 + " " + var3 + " " + var4 + " is "  + str(result) + "\n")

      elif var3 == "*":
        result = int(var2) * int(var4)
        output.write("The result of " + var2 + " " + var3 + " " + var4 + " is "  + str(result) + "\n")

      elif var3 == "/":
        result = int(var2) / int(var4)
        output.write("The result of " + var2 + " " + var3 + " " + var4 + " is " + str(result) + "\n")

  else: # For removing extra space in output
      line = input.readline()
      var1, var2, var3, var4 = line.split(" ")

      if var3 == "+":
        result = int(var2) + int(var4)
        output.write("The result of " + var2 + " " + var3 + " " + var4 + " is "  + str(result))

      elif var3 == "-":
        result = int(var2) - int(var4)
        output.write("The result of " + var2 + " " + var3 + " " + var4 + " is "  + str(result))

      elif var3 == "*":
        result = int(var2) * int(var4)
        output.write("The result of " + var2 + " " + var3 + " " + var4 + " is "  + str(result))

      elif var3 == "/":
        result = int(var2) / int(var4)
        output.write("The result of " + var2 + " " + var3 + " " + var4 + " is " + str(result))

  start += 1

output.close()