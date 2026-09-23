#Double Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

node1=Node(10)
node2=Node(20)
node3=Node(30)
node4=Node(40)
'''
node1.next = node2
node2.prev = node1
node2.next = node3
node3.prev = node2
node3.next = node4
node4.prev = node3

def traverse():
    curr = node4
    while curr:
        print(curr.data,end = "<->")
        curr = curr.prev
    print("None")

traverse()
'''

def insert_begin(head,data):
    new_node = Node(data)
    new_node.next = head
    if head:
        head.prev = new_node
    return new_node
def insert_end(head,data):
    new_node = Node(data)
    if head is None:
        return new_node
    curr = head
    while curr.next:
        curr = curr.next
    curr.next = new_node
    new_node.prev = curr.next
    return head
def traverse(head):
    curr = head
    while curr:
        print(curr.data,end = "<->")
        curr = curr.next
    print("None")
head = None
head = insert_begin(head,50)
head = insert_begin(head,60)
head = insert_begin(head,70)
traverse(head)