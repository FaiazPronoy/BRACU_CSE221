#Task_3
input = open("input3.txt")
output = open("output3.txt","w")

arr_length = int(input.readline())
check_arr = [int(x) for x in input.readline().strip().split(" ")]

def merge(arr1,arr2, k=0):
  i= 0
  j = 0
  data = []
  while i < len(arr1) and j < len(arr2):
    if arr1[i] < arr2[j]:
      data.append(arr1[i])
      i+=1
      k+=j
    else:
      data.append(arr2[j])
      j+=1
  while i < len(arr1):
    data.append(arr1[i])
    i+=1
    k+=j
  while j < len(arr2):
    data.append(arr2[j])
    j+=1

  return data,k

def mergesort(arr,k):
  if len(arr) <= 1:
    return arr, k

  mid = len(arr)//2
  a1 = mergesort(arr[:mid], k)
  a2 = mergesort(arr[mid:], k)

  x = a1[0]
  y = a2[0]
  k += a1[1] + a2[1]
  return merge(x, y, k)

result = mergesort(check_arr, 0)
output.write(f"{result[1]}")

output.close()
