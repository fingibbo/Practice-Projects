def quick_sort(array):
    if len(array) < 1:
        return []

    pivot = array[len(array) - 1]
    less_than_pivot = []
    equal_to_pivot = []
    more_than_pivot = []

    for num in array:
        if num < pivot:
            less_than_pivot.append(num)
        if num > pivot:
            more_than_pivot.append(num)
        if num == pivot:
            equal_to_pivot.append(num)
    return quick_sort(less_than_pivot) + equal_to_pivot + quick_sort(more_than_pivot)

numbers = [87, 11, 23, 18, 18, 23, 11, 56, 87, 56]

print(quick_sort(numbers))

