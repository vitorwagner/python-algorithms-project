def is_anagram(first_string, second_string):
    if first_string == "" and second_string == "":
        return (first_string, second_string, False)
    first_string = list(first_string.casefold())
    second_string = list(second_string.casefold())
    quick_sort(first_string, 0, len(first_string) - 1)
    quick_sort(second_string, 0, len(second_string) - 1)
    sorted_first_string = ''.join(first_string)
    sorted_second_string = ''.join(second_string)
    if len(sorted_first_string) != len(sorted_second_string):
        return (sorted_first_string, sorted_second_string, False)
    if sorted_first_string != (sorted_second_string):
        return (sorted_first_string, sorted_second_string, False)
    return (sorted_first_string, sorted_second_string, True)
# https://stackoverflow.com/a/319435 case insensitive comparison


def quick_sort(string, low, high):
    if low < high:
        partition_index = partition(string, low, high)
        quick_sort(string, low, partition_index - 1)
        quick_sort(string, partition_index + 1, high)


def partition(string, low, high):
    pivot = string[high]
    i = low - 1
    for j in range(low, high):
        if string[j] <= pivot:
            i += 1
            string[i], string[j] = string[j], string[i]
    string[i + 1], string[high] = string[high], string[i + 1]
    return i + 1
