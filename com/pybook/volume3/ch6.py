class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        if not self.items:
            return True
        return False


def is_balanced(input_string):
    s = list()

    for ch in input_string:
        if ch in ['[', '{', '(']:
            s.append(ch)
        if ch in [']', '}', ')']:
            if not s:
                return False
            s.pop()
    return not s


class Queue:
    def __init__(self, size):
        self.items = [0] * size
        self.max_size = size
        self.head = self.tail = self.size = 0

    def enqueue(self, item):
        if self.is_full():
            print('Queue is full!')
            return
        print(f'Inserting {item}')
        self.items[self.tail] = item
        self.tail = (self.tail + 1) % self.max_size
        self.size += 1

    def dequeue(self):
        item = self.items[self.head]
        self.head = (self.head + 1) % self.max_size
        self.size -= 1

        return item

    def is_empty(self):
        if self.size == 0:
            return True
        return False

    def is_full(self):
        if self.size == self.max_size:
            return True
        return False


if __name__ == '__main__':
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)

    while not stack.is_empty():
        an_item = stack.pop()
        print(an_item)

    input_str = input()
    if is_balanced(input_str):
        print(f'{input_str} is balanced')
    else:
        print(f'{input_str} is not balanced')

    queue = Queue(3)
    queue.enqueue('Saqib')
    queue.enqueue('Saadat')
    queue.enqueue('Kafi')
    queue.enqueue('Hi')

    while not queue.is_empty():
        person = queue.dequeue()
        print(person)

    queue.enqueue('Saqib')
    print(queue.items)
    print(f'head: {queue.head}\ntail: {queue.tail}')
