num_list = []
for i in range(1,101, 3):
    num_list.append(i)

print(num_list)

def binary_search(array: list, target_num: int) -> int:

    #start point from 0 so the mid point originally is always half of high
    low = 0
    #high point is legnth of the array, -1 is because arrays start at 0 but length starts counting from 1.
    high = len(array) - 1

    while low <= high:
        #mid is a local variable which changes during the loop
        mid = (low + high) // 2


        #if returns the number if it matches what mid is currently assigned to.
        if array[mid] == target_num:
            return mid

        # if the current mid number in the array is less than the target number, the new low point gets changed to whatever mid currently is + 1 so if mid is range is 0-50, mid is 25, then it'll become 26 and then search in the middle of 26 and 50
        if array[mid] < target_num:
            low = mid + 1
        # else, meaning the mid point if higher than the target number, then the low number remains at 0 and the high changeds to 24 (25-1), then it repeats
        else:
            high = mid - 1
    return - 1

print(binary_search(num_list, 52))