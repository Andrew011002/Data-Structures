import numpy as np

class QuickSort:

    def quickSort(self, arr, start, end):
        
        # base case array of len 1
        if end - start + 1 <= 1:
            return arr

        # get pivot, left, and iterator pointer
        pivot = arr[end]
        l = start

        for i in range(start, end):
            if arr[i] < pivot:
                tmp = arr[i]
                arr[i] = arr[l]
                arr[l] = tmp
                l += 1

        # swap pivot with element at left pointer (create partition)
        arr[end] = arr[l]
        arr[l] = pivot

        # recurr on left & right of pivot
        self.quickSort(arr, start, l - 1)
        self.quickSort(arr, l + 1, end)

        return arr

    def __call__(self, arr, start, end):
        return self.quickSort(arr, start, end)

if __name__ == "__main__":
    n = 15
    arr = list(np.random.randint(-10, 10, (n, )))
    print(arr)
    sort = QuickSort()
    print(sort(arr, 0, len(arr) - 1))
        