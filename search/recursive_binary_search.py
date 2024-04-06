
def binary_search(lst, target):
    if len(lst) == 0:
        return False
    else:
        mid = len(lst) // 2

        if lst[mid] == target:
            print("found")
            return True
        else:
            if lst[mid] < target:
                return binary_search(lst[mid+1:], target)
            else:
                return binary_search(lst[:mid], target)


# Example usage:
numbers = [1, 1, 22, 90, 232, 232, 499]
binary_search(numbers, 12)