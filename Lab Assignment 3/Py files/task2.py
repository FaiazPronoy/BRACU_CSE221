#Task_2
input = open("input2.txt")
output = open("output2.txt", "w")

arr_length = int(input.readline())
check_arr = [int(x) for x in input.readline().strip().split(" ")]

def find_maximum_value(var1, var2, maximum):
      if var1 > var2:
        maximum = var1
      else:
        maximum = var2
      return maximum

def mergesort(arr):
    maximum = arr[0]
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr)//2
        var1  = mergesort(arr[:mid])
        var2 = mergesort(arr[mid:])
    return find_maximum_value(var1, var2, maximum)

maximum = mergesort(check_arr)
for item in maximum:
    output.write(f'{int(item)} ')

output.close()
