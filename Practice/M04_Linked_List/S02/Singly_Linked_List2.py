class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def insert_at_beginning(head, value):
    new_node = Node(value)
    new_node.next = head
    return new_node
def deletion_begin(head):
    if head is None:
        print("Error")
        return None
    new_head = head.next
    del head
    return new_head
def insert_at_end(head, value):
    new_node = Node(value)
    if head is None:
        return new_node
    current = head
    while current.next:
        current = current.next
    current.next = new_node
    return head

def deletion_end(head):
    if head is None or head.next is None:
        print("Error")
        return None
    current = head
    while current.next.next:
        current = current.next
    del current.next
    current.next = None
    return head

def insert_at_position(head, value, position):
    new_node = Node(value)
    if position == 0:
        new_node.next = head
        return new_node
    current = head
    for _ in range(position - 1):
        if current is None:
            print("Error")
            return head
        current = current.next
    if current is None:
        print("Error")
        return head
    new_node.next = current.next
    current.next = new_node
    return head
def delete_at_position(head, position):
    if head is None:
        print("Error")
        return None
    if position == 0:
        new_head = head.next
        del head
        return new_head
    current = head
    for _ in range(position - 1):
        if current is None or current.next is None:
            print("Error")
            return head
        current = current.next
    node_to_delete = current.next
    if node_to_delete is None:
        print("Error")
        return head
    current.next = node_to_delete.next
    del node_to_delete
    return head
def traverse(head):
    current = head
    while current:
        print(current.data, end="->")
        current = current.next
    print("None")

head = None
head = insert_at_beginning(head, 50)
head = insert_at_beginning(head, 60)
head = insert_at_beginning(head, 70)

print("Insertion at beginning")
traverse(head)
print("Insertion at end")
head = insert_at_end(head, 80)
traverse(head)
print("Insertion at position 2")
head = insert_at_position(head, 90, 2)
traverse(head)
print()

print("Deletion at beginning")
head = deletion_begin(head)
traverse(head)
print()

print("Deletion at end")
head = deletion_end(head)
traverse(head)
print()