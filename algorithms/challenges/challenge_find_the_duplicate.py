def analize_list(list_num):
    for index, num in enumerate(list_num):
        if not isinstance(num, int):
            return False
        elif num < 0 or index == len(list_num) - 1:
            return False
        elif list_num[index] == list_num[index + 1]:
            return num


def find_duplicate(nums):
    sorted_nums = sorted(nums)

    if not isinstance(nums, list):
        return False
    elif len(nums) == 0:
        return False

    return analize_list(sorted_nums)


# print(find_duplicate([1, 3, 4, 2, 2]))
# print(find_duplicate([3, 1, 3, 4, 2]))
# print(find_duplicate([1, 1]))
# print(find_duplicate([3, 1, 2, 4, 6, 5, 7, 7, 7, 8]))
# print(find_duplicate([1, 2]))
