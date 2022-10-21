import numpy as np

class MergeSort:

    def mergeSort(self, arr, start, end):
        
        # base case of sorted array (len == 1)
        if end - start + 1 <= 1:
            return arr

        mid = (start + end) // 2 # mid point (floored)

        # divide into left & right subarrays
        self.mergeSort(arr, start, mid)
        self.mergeSort(arr, mid + 1, end)

        # merge sub arrays
        self.merge(arr, start, mid, end)

        return arr
 
    def merge(self, arr, start, mid, end):
        
        # create sub arrays
        left = arr[start: mid + 1]
        right = arr[mid + 1: end + 1]

        # get pointers for left, right, and new sub array
        l = r = 0
        i = start 

        # merge sort while both pointers are in bounds
        while l < len(left) and r < len(right):
            
            # left sub element smaller or equal (stable)
            if left[l] <= right[r]:
                arr[i] = left[l]
                l += 1
            # right sub element larger
            else:
                arr[i] = right[r]
                r += 1
            i += 1
        
        # add what remains of left or right
        while l < len(left):
            arr[i] = left[l]
            l += 1
            i += 1
        while r < len(right):
            arr[i] = right[r]
            r += 1
            i += 1
            
        return arr

    def __call__(self, arr, start, end):
        return self.mergeSort(arr, start, end)
        
if __name__ == "__main__":
    n = 15
    arr = list(np.random.randint(-10, 10, (n, )))
    print(arr)
    sort = MergeSort()
    print(sort(arr, 0, len(arr) - 1))
            
