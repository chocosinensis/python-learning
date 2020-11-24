from . import *

def stack_test():
    stack = Stack(4)
    stack.push(str(1))
    stack.push(str(2))
    stack.push(str(3))
    stack.push(str(4))
    print(str(stack))
    print("popped item: " + stack.pop())
    print("stack after popping an element: " + str(stack))


def queue_test():
    q = Queue(5)
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)
    print(q)
    print(q.dequeue())
    print(q)
    print(q.peek())


def deque_test():
    d = Deque(5)
    d.append(8)
    d.append(5)
    d.prepend(7)
    d.prepend(10)
    print(d)
    print(d.remove_last())
    print(d.remove_first())
    d.prepend(45)
    d.append(55)
    print(d)


if __name__ == '__main__':
    stack_test()
    queue_test()
    deque_test()
