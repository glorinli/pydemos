from . import abs_sort_algorithm

class BubbleSortAlgorithm(abs_sort_algorithm.AbsSortAlgorithm):
    def sort(self, list: list):
        print("Bubble sorting...")
        length = len(list)
        print("Size: ", length)

        for i in range(length - 2, 0, -1):
            print("Checking ", i)
            for j in range(0, i):
                if (list[j] > list[j + 1]):
                    temp = list[j]
                    list[j] = list[j + 1]
                    list[j + 1] = temp
                    print("swap ", list[j], "and", list[j + 1])

        return list