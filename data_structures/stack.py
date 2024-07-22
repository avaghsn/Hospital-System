class Stack:
    def __init__(self, size):
        self.size = size
        self.array = [None] * size
        self.pointer = -1

    def __iter__(self):
        temp = self.pointer
        while temp:
            yield self.array[temp]
            self.pointer += 1

    def __len__(self):
        return self.size

    def top(self):
        return self.array[self.pointer]

    def push(self, data):
        if self.pointer > self.size:
            return f"Overflow, can't push {data}."
        else:
            self.pointer += 1
            self.array[self.pointer] = data

    def pop(self):
        if self.pointer > -1:
            self.pointer -= 1
            return self.array[self.pointer + 1]

    def is_empty(self):
        if self.pointer == -1:
            return True
        return False

    def is_full(self):
        if self.pointer == self.size:
            return True
        return False


class StackNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class SLLStack:
    def __init__(self):
        self.top = None
        self.len = 0

    def __len__(self):
        return self.len

    def __iter__(self):
        temp = self.top
        while temp:
            yield temp.data
            temp = temp.next

    def create_node(self, data):
        node = StackNode(data)
        return node

    def is_empty(self):
        return self.top is None

    def top(self):
        return self.top.data

    def push(self, data):
        node = StackNode(data)
        if self.is_empty():
            self.top = node
            self.len += 1
        else:
            node.next = self.top
            self.top = node
            self.len += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        else:
            temp = self.top
            self.top = self.top.next
            temp.next = None
            self.len -= 1
            return temp.data
