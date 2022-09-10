import sys

class StaticArray:

    def __init__(self, size: int, type: type):
        self.size = size
        self.dtype = type
        self.pointer = 0
        self.values = [None] * size

    def __getitem__(self, index):
        if index < -self.size or index > self.size:
            raise IndexError(f"index {index} out of bounds")
        return self.values[index]

    def __setitem__(self, index, item):
        if index < -self.size or index > self.size:
            raise IndexError(f"Index {index} out of bounds")
        if type(item) != self.dtype:
            raise TypeError(f"Incompatible type for array")
        self.values[index] = item

    def insert(self, index, item):
        if index < -self.size or index > self.size:
            raise IndexError(f"Index {index} out of bounds")
        if self.__len__() == self.size:
            raise ValueError(f"Array is full")
        if type(item) != self.dtype:
            raise TypeError(f"Incompatible type for array")

        if index >= self.pointer:
            self.values[self.pointer] = item
            self.pointer += 1
            return None
        for i in range(self.size):
            if i == index:
                value = self.values[i]    
                self.values[i] = item
                while value is not None:
                    i += 1
                    temp = self.values[i]
                    self.values[i] = value
                    value = temp
                self.pointer += 1
                return None
                        
    def append(self, item):
        if self.__len__() == self.size:
            raise ValueError(f"Array is full")
        if type(item) != self.dtype:
            raise TypeError("Incompatible type for array")
        self.values[self.pointer] = item
        self.pointer += 1

    def remove(self, index=None):
        if not self.__len__():
            raise ValueError(f"Array is empty")
        if index is None:
            self.pointer -= 1
            item = self.values[self.pointer]
            self.values[self.pointer] = None
            return item
        if index < -self.size or index > self.size:
            raise IndexError(f"Index {index} out of bounds")

        self.pointer -= 1
        if index >= self.pointer:
            item = self.values[self.pointer]
            self.values[self.pointer] = None
            return item
        for i in range(self.size):
            if i == index:
                item = self.values[i]
                self.values[i] = None
                while self.values[i] is None and i < self.pointer:
                    value = self.values[i + 1]
                    self.values[i] = value
                    self.values[i + 1] = None
                    i += 1
                return item
    
    def bytes(self):
        return sys.getsizeof(self.values)

    def __len__(self):
        return self.size - self.values.count(None)

    def __str__(self):
        return f"{self.values}"

if __name__ == "__main__":
    array = StaticArray(10, int)
    for i in range(8):
        array.append(i)
    print(array)
    array.remove(5)
    print(array)
    print(len(array))
    
   


