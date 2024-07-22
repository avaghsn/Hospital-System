class QueueArray:
    def __init__(self, size):
        self.queue = [None] * abs(size)
        self.size = size
        self.max = self.size
        self.front = 0
        self.rear = 0

    def is_full(self):
        return (self.rear + 1) % self.max == self.front

    def is_empty(self):
        return self.front == self.rear

    def enqueue(self, data):
        if self.is_full():
            return "Queue is full."
        else:
            self.queue[self.rear] = data
            self.rear += 1

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty."
        else:
            """
            element = self.queue[self.front]
            self.front -= 1
            return element
            """

            self.front += 1
            return self.queue[self.front - 1]

    def size(self):
        return (self.max + self.rear - self.front) % self.max

    def front_element(self):
        return self.queue[self.front]

    def print(self):
        for i, j in enumerate(self.queue):
            print(i, j)


class QueueNode:
    def __init__(self, data):
        self.next = None
        self.data = data

    def delete_next(self):
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.length = 0

    def __len__(self):
        return self.length

    def __iter__(self):
        node = self.front
        while node:
            yield node
            node = node.next

    def enqueue(self, data):
        node = QueueNode(data)
        if self.front is None:
            self.front = node
            self.rear = node
            self.length += 1
        else:
            self.rear.next = node
            self.rear = self.rear.next
            self.length += 1

    def dequeue(self):
        if self.front is not None:
            temp = self.front
            self.front = self.front.next
            temp.delete_next()
            self.length -= 1
            return temp.data

    def is_empty(self):
        return self.front is None

    def size(self):
        return self.length
