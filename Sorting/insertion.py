import numpy as np

# Stable O(n^2) sorting algorithm
# sorts through sorting sub arrays
# swaps values through a second pointer


class InsertionSort():

    """
    class for iterative and recursive insertion sort
    """

    def iterative(self, arr):

        n = len(arr)
        for i in range(1, n):

            j = i - 1 # pointer

            # sort sub array until sorted
            while j >= 0 and arr[j] > arr[j + 1]:
                # swap
                tmp = arr[j + 1]
                arr[j + 1] = arr[j]
                arr[j] = tmp

                j -= 1 # compare next element before
        
        return arr

    def recursive(self, arr, i=1):

        # base case of sorted all sub arrays
        if i == len(arr):
            return arr

        j = i - 1

        # sort sub array until sorted
        while j >= 0 and arr[j + 1] < arr[j]:
            # swap 
            tmp = arr[j + 1]
            arr[j + 1] = arr[j]
            arr[j] = tmp

            j -= 1 # compare next element before

        return self.recursive(arr, i + 1) # go to next subarray

    def __call__(self, arr, recursive=False):
        if recursive:
            return self.recursive(arr)
        return self.iterative(arr)

if __name__ == "__main__":
    n = 15
    arr = list(np.random.randint(-10, 10, (n, )))
    print(arr)
    sort = InsertionSort()
    print(sort(arr))
    print(sort(arr, recursive=True))
    
    


