from algorithms import abs_sort_algorithm
from algorithms import bubblesort

def main():
    print("=== Sort algorithms ===")
    data = [5, 3, 110, 8, 9, 10, 44, 22, 44, 77, 893]

    algorithm = bubblesort.BubbleSortAlgorithm()
    result = algorithm.sort(data)

    print("Sorted: ", result)

if __name__ == '__main__':
    main()