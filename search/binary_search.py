
def test_location(arrayy, query, midpoint):
    if arrayy[midpoint] == query:
        if midpoint - 1 > 0 and arrayy[midpoint - 1] == query:
            return "left"
        else:
            return "found"
    elif arrayy[midpoint] < query:
        return "left"
    else:
        return "right"


def binary_search(arrayy, query):
    first = 0
    last = len(arrayy)-1

    while first <= last:
        midpoint = (first+last) // 2

        result = test_location(arrayy, query, midpoint)

        if result == "found":
            print("value you are searching for is at index: ", midpoint)
            return midpoint
        elif result == "left":
            first = midpoint + 1
        else:
            last = midpoint - 1
    print("element doesn't exist in the array")
    return None


numbers = [1, 1, 22, 90, 232, 232, 499]
binary_search(numbers, 90)

