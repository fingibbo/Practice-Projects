def selection_sort(array):
    if len(array) <= 1:
        return array
    
    current_iter = 0

    while current_iter < len(array):
        starting_number = array[current_iter]
        current_smallest = array[current_iter]
        smallest_index = current_iter

        for index, num in enumerate(array[current_iter:]):
            if num < current_smallest:
                current_smallest = num
                smallest_index = current_iter + index

        if smallest_index != current_iter:
            array[smallest_index] = starting_number
            array[current_iter] = current_smallest

        current_iter +=1
        
    return array




arr = [5, 16, 99, 12, 567, 23, 15, 72, 3]

print("Original array:")
print(arr)

selection_sort(arr)

print("Sorted array:")
print(arr)