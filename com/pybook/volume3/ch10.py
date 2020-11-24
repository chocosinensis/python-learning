from .ch9 import Node, in_order

def bst_insert(root, node):
    last_node = None
    current_node = root

    while current_node is not None:
        last_node = current_node
        if node.data < current_node.data:
            current_node = current_node.left
        else:
            current_node = current_node.right

    if last_node is None:
        root = node
    elif node.data < last_node.data:
        last_node.add_left(node)
    else:
        last_node.add_right(node)

    return root


def create_bst():
    r"""
           10           The binary search tree (BST) created in this method
         /   \
        5    17
       / \  /  \
      3  7 12  19
     / \
    1   4
    """
    root = Node(10)
    for item in [5, 17, 3, 7, 12, 19, 1, 4]:
        node = Node(item)
        root = bst_insert(root, node)
    return root


def bst_search(node, key):
    while node is not None:
        if node.data == key:
            return node
        if node.data > key:
            node = node.left
        else:
            node = node.right
    return node


def bst_minimum(root):
    while root.left is not None:
        root = root.left
    return root


def bst_transplant(root, current_node, new_node):
    if current_node.parent is None:
        root = new_node
    elif current_node == current_node.parent.left:
        current_node.parent.add_left(new_node)
    else:
        current_node.parent.add_right(new_node)
    return root


def bst_delete(root, node):
    if node.left is None:
        root = bst_transplant(root, node, node.right)
    elif node.right is None:
        root = bst_transplant(root, node, node.left)
    else:
        min_node = bst_minimum(node.right)
        if min_node.parent != node:
            root = bst_transplant(root, min_node, min_node.right)
            min_node.add_right(min_node.right)
        root = bst_transplant(root, node, min_node)
        min_node.add_left(node.left)
    return root


if __name__ == '__main__':
    root_bst = create_bst()
    print('BST:', end=' ')
    in_order(root_bst)
    for a_key in [1, 5, 10]:
        a_node = bst_search(root_bst, a_key)
        print(f'will delete {a_node}')
        root_bst = bst_delete(root_bst, a_node)
        print('BST:', end=' ')
        in_order(root_bst)
    print(f'\n{create_bst.__doc__}\n')
