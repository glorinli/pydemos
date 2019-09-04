from . import abs_sort_algorithm

class QuickSortAlgorithm(abs_sort_algorithm.AbsSortAlgorithm):
    def sort(self, list: list):
        print("Quick sorting...")
        length = len(list)
        print("Size: ", length)

        self.quickSort(list, 0, length - 1)

        return list

    def quickSort(self, list, left, right):
        base = list[left]

        i, j = left, right

        print("base = ", base)

        while i < j:
            while i < j and list[j] >= base:
                j = j - 1
            while i < j and list[i] <= base:
                i = i + 1

            print("i, j = ", i , "," ,j)

            if i < j:
                list[i], list[j] = list[j], list[i]

        list[left], list[i] = list[i], base

        print("End one time, left = ", list[left])

        if left < i - 1:
            self.quickSort(list, left, i - 1)
        if i + 1 < right:
            self.quickSort(list, i + 1, right)