#Task_5
input = open("input5.txt")
output = open("output5.txt", "w")

arr_length = int(input.readline())
check_arr = input.readline().strip().split(" ")

def quicksort(arr, low, high):
    if low < high:
        p = partition(arr, low, high)
        quicksort(arr, low, p-1)
        quicksort(arr, p+1, high)
    return arr
           
def partition(arr, low, high):
    pivot = arr[high]
    i = low-1
    for j in range(low, high):
        if arr[j] <= pivot:
            i+=1
            arr[i], arr[j]= arr[j], arr[i]
    arr[i+1], arr[high]= arr[high],arr[i+1]
    return i+1

sorted_arr = quicksort(check_arr, 0, arr_length-1)

for x in sorted_arr:
    output.write(f"{x} ")
output.close()
