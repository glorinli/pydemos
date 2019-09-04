from algorithms import abs_sort_algorithm
from algorithms import bubblesort
from algorithms import quicksort

def main():
    print("=== Sort algorithms ===")
    data = [5, 3, 110, 8, 9, 10, 44, 22, 44, 77, 893]

#    algorithm = bubblesort.BubbleSortAlgorithm()
    algorithm = quicksort.QuickSortAlgorithm()
    result = algorithm.sort(data)

    print("Sorted: ", result)

if __name__ == '__main__':
    main()