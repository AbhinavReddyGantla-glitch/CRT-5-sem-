#Queue implementation using python list
class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self,val):
        self.queue.append(val)
    def is_empty(self):
        return len(self.queue) == 0
    def dequeue(self):
        if self.is_empty():
            return "Queue is Empty"
        return self.queue.pop(0)
    def front(self):
        if self.is_empty():
            return "Queue is Empty"
        return self.queue[0]
    def display(self):
        if self.is_empty():
            return "Queue is Empty"
        for i in self.queue:
            print(i,end=" ")

qu = Queue()
print(qu.is_empty())
qu.enqueue(10)
qu.enqueue(20)
qu.enqueue(30)
print(qu.is_empty)
qu.dequeue()
qu.front()
qu.display()

#Queue implementation using python  Linked List
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        

class Queue_LL:
    def __init__(self):
        self.front = None
        self.rear = None
    def enqueue(self,val):
        new_node = Node(val)
        if self.rear is None:
            self.front = new_node
            self.rear = new_node
            return
        self.rear.next = new_node
        new_node.prev = self.rear
        self.rear = new_node
    def is_empty(self):
        return self.front is None
    def dequeue(self):
        if self.is_empty():
            return "Queue is Empty"
        del_val = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return del_val
    def display(self):
        if self.is_empty():
            return "Queue is Empty"
        curr = self.front
        while curr:
            print(curr.data,end=" ")
            curr = curr.next
