def merge_sort(numbers, start=0, end=None):
    if end is None:
        end = len(numbers)
    if (end - start) > 1:
        mid = (start + end) // 2
        merge_sort(numbers, start, mid)
        merge_sort(numbers, mid, end)
        merge(numbers, start, mid, end)


def merge(numbers, start, mid, end):
    left = numbers[start:mid]
    right = numbers[mid:end]

    left_index, right_index = 0, 0

    for general_index in range(start, end):
        if left_index >= len(left):
            numbers[general_index] = right[right_index]
            right_index = right_index + 1
        elif right_index >= len(right):
            numbers[general_index] = left[left_index]
            left_index = left_index + 1
        elif left[left_index] < right[right_index]:
            numbers[general_index] = left[left_index]
            left_index = left_index + 1
        else:
            numbers[general_index] = right[right_index]
            right_index = right_index + 1


def is_anagram(first_string: str, second_string: str):
    first_string_array = list(first_string.lower())
    second_string_array = list(second_string.lower())

    merge_sort(first_string_array, 0, len(first_string_array))
    merge_sort(second_string_array, 0, len(second_string_array))

    order_first_string = "".join(first_string_array)
    order_second_string = "".join(second_string_array)

    if first_string == "":
        return ("", order_second_string, False)

    if second_string == "":
        return (order_first_string, "", False)

    if order_first_string == order_second_string:
        return (order_first_string, order_second_string, True)
    else:
        return (order_first_string, order_second_string, False)


# print(is_anagram("", "amor"))
# print(is_anagram("coxinha", "empada"))
# print(is_anagram("coxinha", "empada"))
# print(is_anagram("coxinha", "empada"))

# Mergesort
# Quicksort

# numbers = ["w", "g", "b", "a", "c"]
# merge_sort(numbers, 0, len(numbers))
# print(numbers)
