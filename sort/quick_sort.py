
def quick_sort(values):
    if len(values) <= 1:
        return values
    less_than_pivot = []
    greater_than_pivot = []

    pivot = values[0]
    for values in values[1:]:
        if values <= pivot:
            less_than_pivot.append(values)
        else:
            greater_than_pivot.append(values)
    return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)

numbers = [33,33,552,2131,79,0,442,21,55,95,442435,675,3213455,5523455,6635567,999765,323,6798765,346789,8765433,765,18]
sorted_numbers = quick_sort(numbers)
print(sorted_numbers)

