#Task_6
input = open("input6.txt")
output = open("output6.txt","w")

line1 = input.readline().strip().split(" ")
arr_length = int(line1[0])

line2 = input.readline().strip().split(" ")
check_arr = [int(x) for x in line2]

line3 = input.readline().split(" ")
total_queries = int(line3[0])

queries_lst = []
for i in range(total_queries):
  queries_lst.append(int(input.readline().strip()))

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quickselect(arr, low, high, k):
    if low == high:
        return arr[low]

    pivot = partition(arr, low, high)

    if k == pivot:
        return arr[k]
    elif k < pivot:
        return quickselect(arr, low, pivot - 1, k)
    else:
        return quickselect(arr, pivot + 1, high, k)

for i in queries_lst:
  var1 = quickselect(check_arr, 0, arr_length-1, i-1) 
  output.write(f"{var1}\n")

output.close()
