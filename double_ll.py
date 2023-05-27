class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_after(self, node, value):
        if node is None:
            return

        new_node = Node(value)
        new_node.prev = node
        new_node.next = node.next

        if node.next is not None:
            node.next.prev = new_node
        else:
            self.tail = new_node

        node.next = new_node

    def delete(self, node):
        if node is None:
            return

        if node.prev is not None:
            node.prev.next = node.next
        else:
            self.head = node.next

        if node.next is not None:
            node.next.prev = node.prev
        else:
            self.tail = node.prev

    def print_forward(self):
        current = self.head
        while current is not None:
            print(current.value, end=" ")
            current = current.next
        print()

    def print_backward(self):
        current = self.tail
        while current is not None:
            print(current.value, end=" ")
            current = current.prev
        print()


# Example usage:
dll = DoublyLinkedList()
dll.append(1)
dll.append(2)
dll.append(3)

dll.prepend(0)

dll.insert_after(dll.head, 1.5)

#dll.delete(dll.head.next)

dll.print_forward()  # Output: 0 1.5 2 3
dll.print_backward()  # Output: 3 2 1.5 0
