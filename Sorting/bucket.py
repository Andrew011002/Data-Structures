import numpy as np

class BucketSort:

    def bucketSort(self, arr, interval):
        
        for n in arr:
            interval[n] += 1

        i = 0
        for n in interval:
            for c in range(interval[n]):
                arr[i] = n
                i += 1

        return arr

    def __call__(self, arr, interval):
        return self.bucketSort(arr, interval)

if __name__ == "__main__":
    n = 20
    interval = {-1: 0, 0: 0, 1: 0}
    arr = np.random.randint(-1, 2, (n, ))
    sort = BucketSort()
    print(arr)
    print(sort(arr, interval))
    
    