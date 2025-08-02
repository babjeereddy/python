class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

a=Node(10)
b=Node(20)
c=Node(30)
a.next=b
b.next=c
head =a

current = head
while current:
    print(current.data, end=" -> ")
    current = current.next
print("None")

#adding node @ first
new_node =Node(5)
new_node.next=head

head=new_node

current =head
while current:
    print(current.data, end=" -> ")
    current = current.next
print("None")

# adding node @ loast
current = head
while current.next:
    current = current.next
current.next = Node(40)


current =head
while current:
    print(current.data, end=" -> ")
    current = current.next
print("None")
