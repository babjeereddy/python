class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Insert at the end
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node
        new_node.prev = curr

    # Traverse forward
    def print_forward(self):
        curr = self.head
        while curr:
            print(curr.data, end=" <-> " if curr.next else " -> None\n")
            last = curr
            curr = curr.next

    # Traverse backward
    def print_backward(self):
        curr = self.head
        if not curr:
            return
        # Go to the last node
        while curr.next:
            curr = curr.next
        # Traverse backward
        while curr:
            print(curr.data, end=" <-> " if curr.prev else " -> None\n")
            curr = curr.prev

    #dll = DoublyLinkedList()
dll.append(10)
dll.append(20)
dll.append(30)
dll.append(40)

print("Forward:")
dll.print_forward()    # 10 <-> 20 <-> 30 <-> 40 -> None

print("Backward:")
dll.print_backward()   # 40 <-> 30 <-> 20 <-> 10 -> None