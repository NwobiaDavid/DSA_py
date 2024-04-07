
def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    mid_index = len(lst) // 2
    left_lst = merge_sort(lst[:mid_index])
    right_lst = merge_sort(lst[mid_index:])
    sorted_lst = []
    left_index = 0
    right_index = 0

    while left_index < len(left_lst) and right_index < len(right_lst):
        if left_lst[left_index] < right_lst[right_index]:
            sorted_lst.append(left_lst[left_index])
            left_index += 1
        else:
            sorted_lst.append(right_lst[right_index])
            right_index += 1

    sorted_lst.extend(left_lst[left_index:])
    sorted_lst.extend(right_lst[right_index:])

    return sorted_lst


sorted_number = merge_sort([2,5,3,90,5433, 202, 37871, 0,1,2,1,34,43])
print(sorted_number)
