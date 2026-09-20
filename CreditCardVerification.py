def verify_card_number(card_no: str) -> str:
    stripped_no = card_no.translate({ord(char): None for char in "- "})
    split_card_no = []
    total = 0
    for num in stripped_no:
        split_card_no.append(int(num))

    for index, digit in enumerate(split_card_no[-2::-2]):
        real_index = len(split_card_no) - 2 - (2 * index)
        new_digit = digit * 2
        if new_digit > 9:
            new_digit = new_digit - 9
        split_card_no[real_index] = new_digit

    for num in split_card_no:
        total += num

    print(split_card_no)
    print(total)
    if total % 10 == 0:
        return "VALID!"
    else:
        return "INVALID!"
