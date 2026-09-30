#Implementation of Queue using Linked List
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    def enqueue(self,val):
        new_node = Node(val)
        if self.rear is None:
            self.rear = self.front = new_node
            return
        self.rear.next = new_node
        self.rear = new_node
    def is_empty(self):
        return self.front is None
    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        del_val = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return del_val
    def peek(self):
        if self.is_empty():
            return "Queue is empty"
        return self.front.data
    def display(self):
        if self.is_empty():
            return "queue is empty"
        curr = self.front
        while curr:
            print(curr.data,end = " ")
            curr = curr.next

ab = Queue()
print(ab.is_empty())
ab.enqueue(10)
ab.enqueue(20)
ab.enqueue(30)
print(ab.is_empty())
ab.dequeue()
ab.display()
ab.peek()

