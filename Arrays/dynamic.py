from static import StaticArray

class DynamicArray(StaticArray):

    def __init__(self, size: int, dtype: type):
        super().__init__(size, dtype)

    def append(self, item):
        # update size if full
        if len(self) == self.size:
            self.update()
        super().append(item)

    def insert(self, index, item):
        # update size if full
        if len(self) == self.size:
            self.update()
        super().insert(index, item)

    def remove(self, item):
        # update size if full
        if len(self) == self.size:
            self.update()
        return super().remove(item)
    
    def update(self):
        # double array size
        self.array += [None] * self.size
        self.size *= 2

if __name__ == "__main__":
    arr = DynamicArray(5, int)
    pass
    
    
    