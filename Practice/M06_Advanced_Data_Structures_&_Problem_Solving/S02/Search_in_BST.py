class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

root = Node(10)
root.left = Node(5)
root.right = Node(20)
root.left.right = Node(7)
root.right.left = Node(15)

def Search(root,val):
