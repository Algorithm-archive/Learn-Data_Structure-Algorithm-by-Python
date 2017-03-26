from search import *

def main():
    # This list must be sorted. If it is not given as sorted, sort it first, then call the binarySearch method
    testlist = [1, 50, 20, 10, 2, 1]
    index = simpleTernarySearch(testlist)
    print(testlist[index])

    result = ternarySearch(func, 0, 1, 1e-6)
    print(func(result))

    result = ternarySearchRecursive(func, 0, 1, 1e-6)
    print(func(result))


def func(x):
    return -1*1*x*x + 2*x +3 # (-a*x*x + b*x + c) is an unimodal function, here a = 1, b = 2, c = 3

if __name__ == '__main__':
    main()
