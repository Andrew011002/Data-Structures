import sys

class StaticArray:

    def __init__(self, size: int, dtype: type):
        self.size = size
        self.dtype = dtype
        self.length = 0
        self.pointer = 0
        self.array = [None] * size

    def append(self, item):
        # full array
        if len(self) == self.size:
            raise ValueError("Array is full")
        # invalid dtype
        if type(item) is not self.dtype:
            raise TypeError("Invalid dtype")

        # add item updating attributes
        self.array[self.pointer] = item
        self.pointer += 1
        self.length += 1

    def insert(self, index, item):
        # full array
        if len(self) == self.size:
            raise ValueError("Array is full")
        # index out of bounds
        if index > self.size or index < -self.size:
            raise IndexError("Index out of bounds")
        # invalid dtype
        if type(item) is not self.dtype:
            raise TypeError("Invalid dtype")

        # index less than (converted)
        index = index + self.size if index < 0 else index

        # place at specified location or most open position

        # greater than pointer (add to end)
        if index >= self.pointer:
            self.append(item)
            return None

        # insert item
        tmp = self.array[index]
        self.array[index] = item
        index += 1
        item = tmp

        # shift any elements right 1\
        for i in range(index, self.pointer + 1):
            tmp = self.array[i]
            self.array[i] = item
            item = tmp

        # update length & pointer
        self.length += 1
        self.pointer += 1

    def remove(self, item):
        # empty array
        if not len(self):
            raise ValueError("Array is empty")
        # wrong dtype
        if type(item) is not self.dtype:
            raise TypeError("Invalid dtype")

        found = False # flag
        
        # locate item
        for i in range(self.pointer):
            # item found
            if self.array[i] == item:
                self.array[i] = None
                found = True
                index = i
                break
        
        # item not in the array
        if not found:
            raise ValueError("The item is not in the array")

        # shift items left most
        for i in range(index, self.pointer - 1):
            tmp = self.array[i + 1]
            self.array[i + 1] = None
            self.array[i] = tmp
        
        # adjust attributes
        self.pointer -= 1
        self.length -= 1

        return item

    def __getitem__(self, index):
        # index out of bounds
        if index > self.size or index < -self.size:
            raise IndexError("Index out of bounds")
        return self.array[index]

    def __setitem__(self, index, item):
        # index out of bounds
        if index > self.size or index < -self.size:
            raise IndexError("Index out of bounds")
        # invalid dtype
        if type(item) is not self.dtype:
            raise TypeError("Invalid dtype")
        # index less than (converted)
        index = index + self.size if index < 0 else index

        # add to most open position
        if index > self.pointer:
            self.append(item)
        # add at desired position
        else:
            self.array[index] = item

    def __iter__(self):
        return iter(self.array)

    def __len__(self):
        return self.length

    def __str__(self):
        return str(self.array)


    

if __name__ == "__main__":
    arr = StaticArray(10, int)
    for i in range(10):
        arr.append(i * i)

    print(arr)
    for val in arr:
        print(val)

    

        
    
    
   


