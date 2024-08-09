#Task_4
input = open("input4.txt")
output =  open("output4.txt","w")

arr_length = int(input.readline())
check_arr = [int(x) for x in input.readline().strip().split(" ")]


def getMax(arr):
    le = len(arr)

    if le == 1:
        return -999999
    
    elif le == 2:
        return arr[0] + arr[1]**2

    left = arr[:le//2]
    right = arr[le//2:]
    left_max = getMax(left)
    right_max = getMax(right)


    max1 = left[0]
    max2 = right[0]

    for i in left:
        if i > max1:
            max1 = i
    
    for i in right:
        if abs(i) > abs(max2):
            max2 = i 
    
    cross = max1 + max2**2
    
    return max(left_max,right_max,cross)


max = getMax(check_arr)
output.write(str(max))

output.close()