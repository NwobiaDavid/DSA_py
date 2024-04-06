def test_location(arrayy, query, midpoint):
    if arrayy[midpoint] == query:
        if midpoint == 0 or arrayy[midpoint - 1] != query:
            return "found"
        else:
            return "left"
    elif arrayy[midpoint] < query:
        return "right"
    else:
        return "left"


def binary_search(arrayy, query):
    first = 0
    last = len(arrayy) - 1

    while first <= last:
        midpoint = (first + last) // 2

        result = test_location(arrayy, query, midpoint)

        if result == "found":
            print("Value you are searching for is at index:", midpoint)
            return midpoint
        elif result == "left":
            last = midpoint - 1
        else:
            first = midpoint + 1

    print("Element doesn't exist in the array")
    return None


# Example usage:
numbers = [1, 1, 22, 90, 232, 232, 499]
binary_search(numbers, 22)
