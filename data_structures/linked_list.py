class SLLNode:
    def __init__(self, data):
        self.data = data
        self.next = None

    def delete_pointers(self):
        self.next = None


class DLLNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

    def delete_pointers(self):
        self.next = None
        self.previous = None


class SLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.len = 0

    def __len__(self):
        return self.len

    def __iter__(self):
        temp = self.head
        while temp:
            yield temp
            temp = temp.next

    def __delitem__(self, node):
        if node is self.head:
            self.delete_first()
            return None
        if node is self.tail:
            self.delete_last()
            return None
        for i in self:
            if i.next is node:
                temp = node.next
                i.next = temp
                node.data = None
                node.next = None
                del node
                self.len -= 1
                return None

    def __getitem__(self, item):
        for i, value in enumerate(self):
            if i == item:
                if value is not None:
                    return value
                return None

    def is_empty(self):
        if self.head is None:
            return True

    def first(self):
        if not self.is_empty():
            return self.head

    def traverse(self):
        if self.is_empty():
            return "List is empty"
        temp = self.head
        while temp is not None:
            yield temp
            temp = temp.next

    def search2(self, value):
        if self.is_empty():
            return "List is empty"
        temp = self.head
        while temp is not None and temp.data != value:
            temp = temp.next
        if temp is None:
            return "not found"
        else:
            return temp

    def search(self, target, key=lambda x: x.data):
        for i in self:
            if key(i) == target:
                return i

    def add_first(self, data):
        node = SLLNode(data)
        if self.is_empty():
            self.tail = node
        node.next = self.head
        self.head = node
        self.len += 1

    def insert(self, data, node=None):
        """
        inserts after given node
        if node = None inserts 1st
        """
        new_node = SLLNode(data)
        if node is None:
            self.add_first(data)
            return
        temp = node.next
        node.next = new_node
        new_node.next = temp

    def add_last(self, data):
        node = SLLNode(data)
        if self.is_empty():
            self.head = node
            self.tail = node
            self.len += 1
        else:
            self.tail.next = node
            self.tail = self.tail.next
            self.len += 1

    def add_after(self, value, data):
        node = SLLNode(data)
        target = self.search(value)
        if target is not None and target.next is None:
            target.next = node
            self.tail = node
            self.len += 1
        elif target is not None and target.next is not None:
            node.next = target.next
            target.next = node
            self.len += 1
        else:
            return "node not found"

    def delete_first(self):
        if not self.is_empty():
            self.head = self.head.next
            if self.len == 1:
                self.tail = self.head
            self.len -= 1

    def delete_last(self):
        if self.is_empty():
            return None

        result = self.tail.data
        if self.head is self.tail:
            self.head = None
            self.tail = None
            self.len -= 1
            return result

        temp = self.head
        while temp and temp.next is not None:
            if not temp.next.next:
                temp.next = None
                self.tail = temp
                self.len -= 1
                return result
            else:
                temp = temp.next

    def delete(self, node):
        self.__delitem__(node)

    def clear(self):
        while self.head:
            self.delete_first()

    def remove(self, node=None):
        """ node is the given obj to delete if = none, first element is removed from the list """
        if node is None:
            self.delete_first()
            return
        prev_node = self.search(node, key=lambda x: x.next if x.next is not None else None)
        if prev_node.next is self.tail:
            self.delete_last()
            return
        if prev_node:
            target = prev_node.next
            prev_node.next = target.next
            target.data = None
            target.next = None
            del target
            self.len -= 1
        else:
            return ValueError("node not found")


class DLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.len = 0

    def is_empty(self):
        return self.head is None

    def size(self):
        return self.len

    def first(self):
        if not self.is_empty():
            return self.head

    def search(self, value):
        if self.is_empty():
            return "List is empty"
        temp = self.head
        while temp is not None and temp.data != value:
            temp = temp.next
        if temp is None:
            return "not found"
        else:
            return temp

    def traverse(self):
        if self.is_empty():
            return "List is empty"
        temp = self.head
        while temp is not None:
            yield temp
            temp = temp.next

    def add_first(self, data):
        node = DLLNode(data)
        if self.is_empty():
            self.tail = node
        node.next = self.head
        self.head = node
        self.len += 1

    def add_last(self, data):
        node = DLLNode(data)
        if self.is_empty():
            self.head = node
            self.tail = node
            self.len += 1
        else:
            node.previous = self.tail
            self.tail.next = node
            self.len += 1

    def delete_first(self):
        # not completed yet
        temp = self.head
        self.head = self.head.next

    def delete_last(self):
        pass

    def delete_this(self):
        pass
