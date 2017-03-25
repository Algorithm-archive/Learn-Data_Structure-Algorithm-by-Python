def binarySearch(item, item_list):
    low, high = 0, len(item_list) - 1

    found = False

    while low <= high and not found:
        mid = (low + high) // 2

        if item_list[mid] == item:
            found = True # You can catch the found value or it's position here too
        else:
            if item < item_list[mid]:
                high = mid - 1
            else:
                low = mid + 1

    return found
