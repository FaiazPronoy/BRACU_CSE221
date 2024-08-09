#Task_2
input = open("/content/input2.txt")
output = open("/content/output2.txt", "w")

def bubbleSort(arr, length):
    for i in range(length-1):
        flag = False
        for j in range(length-i-1):
            if arr[j] > arr[j+1]:
                flag = True
                arr[j], arr[j+1] = arr[j+1], arr[j]
        if flag == False:
          break

num_of_elem = int(input.readline())
new_arr = [None] * num_of_elem

all_elem_line = input.readline()
new_lst = all_elem_line.split(" ")

for i in range(num_of_elem):
  new_arr[i] = int(new_lst[i])

bubbleSort(new_arr, num_of_elem)

for idx in range(num_of_elem):
  if idx != num_of_elem-1:
     output.write(str(new_arr[idx]) + " ")
  else:
     output.write(str(new_arr[idx]))

output.close()


# The best case scenario is where the list/array is already sorted.

# The code of bubbleSort in the question, has a run time complexity of O(n^2).
# This is how I modified the bubbleSort function so that it achieves
# the run time complexity of 0(n):

# I used a flag in the outer loop and initialized it with False, then I traverse
# the array once and checked if my code is performing any swap opertion or not.
# If any swap operation occurs then the flag will be True, otherwise the code
# will break the outer loop.

# As input 2 is sorted, so the code will not perform any swap operation that
# means the code will run at time complexity O(n) instead of O(n^2).

# That is how I have achieved the θ(n) with bubbleSort for
# input 2(best-case scenario)