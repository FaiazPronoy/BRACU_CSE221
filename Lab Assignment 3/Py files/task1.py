#Task_1
input = open("input1.txt")
output = open("output1.txt", "w")

arr_length = int(input.readline())
unsorted_arr = [int(x) for x in input.readline().strip().split(" ")]

def merge(arr1, arr2):
  i = 0
  j = 0
  k = 0
  data = [None] * (len(arr1)+len(arr2))

  while i < len(arr1) and j < len(arr2):
    if arr1[i] < arr2[j]:
      data[k] = arr1[i]
      i+=1
      k+=1
    else:
      data[k] = arr2[j]
      j+=1
      k+=1
  while i < len(arr1):
    data[k] = arr1[i]
    i+=1
    k+=1
  while j < len(arr2):
    data[k] = arr2[j]
    j+=1
    k+=1
  return data

def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr)//2
        a1 = mergeSort(arr[:mid])  # write the parameter
        a2 = mergeSort(arr[mid:])  # write the parameter
        return merge(a1, a2)       # complete the merge funtemp_arrtion above

sorted_arr = mergeSort(unsorted_arr)

for num in sorted_arr:
    output.write(f'{num} ')

output.close()
