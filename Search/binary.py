import numpy as np

class BinarySearch:

    def search(self, arr, target):
        # get pointers
        l, h = 0, len(arr) - 1

        # search while l doesn't over-cross h
        while l <= h:
            
            # get mid pointer
            m = (l + h) // 2

            # target reached
            if arr[m] == target:
                return arr[m], m

            # under-estimate
            if arr[m] < target:
                # elimate [l, m]
                l = m + 1
            # over-estimate 
            elif arr[m] > target:
                # elimate [m, h]
                h = m - 1

        # not in the array
        return - 1
            

    def __call__(self, arr, target):
        return self.search(arr, target)

if __name__ == "__main__":
    n = 100
    arr = list(np.random.randint(0, 100, (n , )))
    arr.sort()
    print(arr)
    search = BinarySearch()
    target = 25
    print(search(arr, target))