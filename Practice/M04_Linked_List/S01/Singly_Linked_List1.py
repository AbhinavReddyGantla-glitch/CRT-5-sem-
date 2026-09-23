class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    node 1 = Node(20) 
    node 2 = Node(30)
    node 3 = Node(40)
    node 4 = Node(50)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    def traverse(self):
        curr = node1
        while curr:
            print(curr.data,end = "->")
            curr = curr.next
        print("None")
    traverse(head)
    print()
    print("Deletion at the Beginning")
    head = deletion_begin(head)
    traverse(head)
    print()
    print("Deletion at the End")
    head = deletion_end(head)
    traverse(head)
    print()
    print("Deletion at the Position")
    deletion_at_pos(head.next) 

    