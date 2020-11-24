from .ch7_2 import *

def test_append():
    dll = DoublyLinkedList()
    assert dll.head.next is None, 'Linked list empty, so head should point to None'

    item = 5
    dll.append(item)
    assert dll.head.next.data == item, 'head should point to the first node'

    item2 = 8
    dll.append(item2)
    assert dll.head.next.data == item, 'head should point to the first node'

    first_node = dll.head.next
    second_node = first_node.next
    assert first_node.next.data == item2, 'first node should point to second item'
    assert second_node.prev.data == item, 'previous node of second node should be the first node'
    assert str(dll) == '5 8', 'string representation of dll should match \'5 8\''


def test_prepend():
    dll = DoublyLinkedList()
    assert dll.head.next is None, 'Linked list empty, so head should point to None'

    item = 5
    dll.prepend(item)
    assert dll.head.next.data == item, 'head should point to the first node'

    new_item = 10
    dll.prepend(new_item)
    assert dll.head.next.data == new_item, 'head should point to the first node'

    new_node = dll.head.next
    old_node = new_node.next
    assert new_node.prev is None, 'previous node of new node should be None'
    assert old_node.prev == new_node, 'previous node of old node should be new node'
    assert old_node.data == item, 'checking the data of old node'
    assert str(dll) == '10 5', 'string representation of dll should match \'10 5\''


def test_search():
    dll = DoublyLinkedList()

    item = 5
    assert dll.search(item) is None, 'item should not be found in an empty list'
    dll.append(item)
    node = dll.search(item)
    assert node.data == item, 'item should be found in the list'

    dll.append(10)
    dll.append(15)
    node = dll.search(10)
    assert node.data == 10, '10 should be found in the list'

    node = dll.search(20)
    assert node is None, '20 should not be found in the list'


def test_remove_node():
    dll = DoublyLinkedList()
    dll.append(5)
    node = dll.search(5)
    assert dll.head.next == node, 'head should point to node'
    dll.remove_node(node)
    assert dll.head.next is None, 'head should point to None, as list is empty'


def test_remove():
    dll = DoublyLinkedList()
    dll.append(5)
    dll.append(10)
    dll.append(15)
    dll.append(20)

    node5 = dll.search(5)
    node10 = dll.search(10)
    node15 = dll.search(15)
    node20 = dll.search(20)

    assert node10.next == node15
    assert node15.prev == node10

    dll.remove(15)
    assert node10.next == node20
    assert node20.prev == node10
    assert str(dll) == '5 10 20'

    dll.remove(20)
    assert node10.next is None
    assert str(dll) == '5 10'

    dll.remove(5)
    assert dll.head.next == node10
    assert node10.prev is None
    assert str(dll) == '10'
