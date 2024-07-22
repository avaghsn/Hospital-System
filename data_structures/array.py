class Array:
    def __init__(self, size: int = 0):
        self.size = abs(size)
        self.array = [None] * abs(size)
        self.index = 0

    def __setitem__(self, index, data):
        if int(index) < self.size:
            self.array[int(index)] = data
        else:
            raise IndexError("Index out of range")

    def __getitem__(self, index):
        if abs(index) < self.size:
            return self.array[index]
        else:
            raise IndexError("Index out of range")

    def __contains__(self, key):
        for i in self.array:
            if i == key:
                return True, f" Element: {self.array[key]}"
            return False

    def __len__(self):
        return self.size

    def __repr__(self):
        return repr(self.array)

    def __iter__(self):
        for i in self.array:
            yield i

    def __delitem__(self, index):
        ...

    def get(self):
        return self.array

    def add(self, data):
        if abs(self.index) < self.size:
            self.array[self.index] = data
            self.index += 1
        else:
            raise IndexError("Index out of range")


class DynamicArray:
    def __init__(self, size: int = 0):
        self.size = abs(size)
        self.array = Array(size)
        self.useful_data = 0

    def __setitem__(self, index, data):
        if self.useful_data > abs(index):
            self.array[index] = data
        else:
            raise IndexError("index out of range")

    def __getitem__(self, index):
        if self.size > abs(index):
            return self.array[index]
        else:
            raise IndexError("index out of range")

    def __len__(self):
        return self.useful_data

    def __iter__(self):
        for i in range(self.useful_data):
            yield self.array[i]

    def __contains__(self, item):
        for i in self:
            if i == item:
                return True
        return False

    def get(self):
        return self.array

    def size(self):
        return self.size

    def extend(self):
        if self.size == 0:
            temp = Array(1)
        else:
            temp = Array(2 * self.size)

        for i in range(self.useful_data):
            temp[i] = self.array[i]
        self.array = temp
        self.size = len(temp)
        del temp

    def append(self, item):
        if self.useful_data == self.size:
            self.extend()
            self.array[self.useful_data] = item
        else:
            self.array[self.useful_data] = item

        self.useful_data += 1
        return None

    def pop(self):
        if self.useful_data - 1 >= 0:
            temp = self[-1]
            self[-1] = None
            self.useful_data -= 1
            return temp
