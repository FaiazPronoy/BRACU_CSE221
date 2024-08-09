#Task_3
input = open("/content/input3.txt")
output = open("/content/output3.txt", "w")

def selection_sort_of_list_descending(lst, length):
      for i in range(length):
        min_idx = i
        for j in range(i+1, length):
          if lst[min_idx] < lst[j]:
            min_idx = j
        lst[i], lst[min_idx] = lst[min_idx], lst[i]
      return lst

def selection_sort_of_dict_ascending(input_dict, length):
    keys = list(input_dict.keys())
    for i in range(length - 1):
        min_idx = i
        for j in range(i + 1, length):
            if keys[j] < keys[min_idx]:
                min_idx = j
        keys[i], keys[min_idx] = keys[min_idx], keys[i]

    sorted_dict = {}
    for k in keys:
       sorted_dict[k] = input_dict[k]

    return sorted_dict

num_of_test_case = int(input.readline())
dict1 = {}

all_id_line = input.readline()
id_lst = all_id_line.split(" ")

all_mark_line = input.readline()
mark_lst = []
for i in all_mark_line.split(" "):
  mark_lst.append(int(i))

for i in range(num_of_test_case):
    dict1[int(id_lst[i])] = int(mark_lst[i])

dict1 = selection_sort_of_dict_ascending(dict1, num_of_test_case)

sorted_marks = selection_sort_of_list_descending(mark_lst, num_of_test_case)
sorted_dict = {}
for i in sorted_marks:
    for k in dict1.keys():
        if dict1[k] == i:
            sorted_dict[k] = dict1[k]

for key, value in sorted_dict.items():
  output.write(f"ID: {key} Mark: {value} \n")

output.close()