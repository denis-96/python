def binary_search(array, item):
    low = 0
    high = len(array) - 1

    while low <= high:
        mid = low + high
        guess = array[mid]
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None
