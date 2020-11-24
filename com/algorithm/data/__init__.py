class Stack:
    def __init__(self, size):
        self.elements = []
        self.top = -1
        self.size = size

    def __repr__(self):
        stack = '['
        for i in range(len(self.elements) - 1):
            stack += self.elements[i] + ', '
        stack += self.elements[-1] + ']'
        return stack

    def push(self, element):
        if self.is_full():
            return
        self.elements.append(element)
        self.top += 1

    def pop(self):
        if self.is_empty():
            return None
        self.top -= 1
        return self.elements.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.elements[self.top]

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.size


class Queue:
    def __init__(self, size):
        self.elements = [0] * size
        self.max_size = size
        self.head = self.tail = self.size = 0

    def __repr__(self):
        queue = '['
        for i in range(self.head, len(self.elements) - 1):
            queue += str(self.elements[i]) + ', '
        queue += str(self.elements[-1]) + ']'
        return queue

    def enqueue(self, element):
        if self.is_full():
            return
        self.elements[self.tail] = element
        self.tail = (self.tail + 1) % self.max_size
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            return None
        element = self.elements[self.head]
        self.head = (self.head + 1) % self.max_size
        self.size -= 1

        return element

    def peek(self):
        if self.is_empty():
            return None
        return self.elements[0]

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.max_size


class Deque:
    def __init__(self, size):
        self.elements = [0] * size
        self.size = size
        self.head = -1
        self.tail = 0

    def __repr__(self):
        deque = '['
        for i in range(len(self.elements) - 1):
            deque += f'{self.elements[i]}, '
        deque += f'{self.elements[-1]}]'
        return deque

    def append(self, element):
        if self.is_full():
            self.tail = 0
        else:
            self.tail += 1
        self.elements[self.tail] = element

    def prepend(self, element):
        if self.head < 1:
            self.head = self.size - 1
        else:
            self.head -= 1
        self.elements[self.head] = element

    def remove_first(self):
        if self.is_empty():
            return None
        element = self.elements[self.head]
        if self.head == self.tail:
            self.head = self.tail = -1
        elif self.head == self.size - 1:
            self.head = 0
        else:
            self.head += 1
        return element

    def remove_last(self):
        if self.is_empty():
            return None
        element = self.elements[self.tail]
        if self.head == self.tail:
            self.head = self.tail = -1
        if self.tail == 0:
            self.tail = self.size - 1
        else:
            self.tail -= 1
        return element

    def is_empty(self):
        return self.head == -1

    def is_full(self):
        return self.head == 0 and self.tail == self.size - 1
