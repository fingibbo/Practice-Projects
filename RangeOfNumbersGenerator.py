def range_of_numbers(start_num: int, end_num: int) -> list:
    if start_num > end_num:
        return []
    range_list = range_of_numbers(start_num, end_num - 1)
    range_list.append(end_num)
    return range_list

print(range_of_numbers(4,4))
