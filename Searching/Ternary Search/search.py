def simpleTernarySearch(item_list):
    """
    Find the maximum value in a strictly increasing and then strictly decreasing list
    N.B.- This method won't work if the list does not represent an unimodal function
    e.g. if the maximum value present in the first or last index of the list
    """
    left, right = 0, len(item_list) - 1

    found = False

    while left <= right:
        if (right - left) < 3: #Here 3 is the smallest range to divide the left and right value
            found = True
            break

        leftThird = left + (right - left) // 3
        rightThird = right - (right - left) // 3

        #To find the minimum in an unimodal function change the following comparison to >
        if item_list[leftThird] < item_list[rightThird]:
            left = leftThird
        else:
            right = rightThird

    return (left + right) // 2


def ternarySearch(func, left, right, absolutePrecision):
    """
    Find maximum of unimodal function func() within [left, right]
    To find the minimum, reverse the if/else statement or reverse the comparison.
    """
    while True:
        #left and right are the current bounds; the maximum is between them
        if abs(right - left) < absolutePrecision:
            return (left + right)/2

        leftThird = left + (right - left)/3
        rightThird = right - (right - left)/3

        if func(leftThird) < func(rightThird):
            left = leftThird
        else:
            right = rightThird


def ternarySearchRecursive(func, left, right, absolutePrecision):
    """
    left and right are the current bounds. the maximum is between them
    """
    if abs(right - left) < absolutePrecision:
        return (left + right)/2

    leftThird = (2*left + right)/3
    rightThird = (left + 2*right)/3

    if func(leftThird) < func(rightThird):
        return ternarySearch(func, leftThird, right, absolutePrecision)
    else:
        return ternarySearch(func, left, rightThird, absolutePrecision)
