def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    subarray_size = 1
    while subarray_size < len(arr):
        left = 0

        while left < len(arr):
            mid = left + subarray_size
            right = min(left + subarray_size, len(arr))
            merge(arr, left, mid, right)
            left += 2 * subarray_size
        subarray_size *= 2

    return arr


def merge(arr, left, mid, right):
    temp = []
    i = left
    j = mid
    while i < mid and j < right:
        if arr[i] < arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            j += 1
    while i < mid:
        temp.append(arr[i])
        i += 1
    while j < right:
        temp.append(arr[j])
        j += 1
    for k in range(left, right):
        arr[k] = temp[k - left]

arr = [2, 5, 3, 90, 5433, 1, 2, 1, 34, 43]
print("Original array:", arr)
merge_sort(arr)
print("Sorted array:", arr)