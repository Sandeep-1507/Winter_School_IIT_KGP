

class Queue:

    def __init__(self):
        self.que = []

    def front(self):
        return (self.que[0])

    def back(self):
        return (self.que[-1])    

    
    def enqueue(self, item): #to add element
        self.que.append(item)

    
    def dequeue(self):#remove first element
        if len(self.que) < 1:
            return None
        return self.que.pop(0) 

    
    def display(self):#print
        print(self.que)

    def size(self):#print size
        return len(self.que)


q = Queue()
q.enqueue('a')
q.enqueue('b')
q.enqueue('c')
q.enqueue('d')
q.enqueue('e')

print("The First element is ")
print(q.front())
print("THe Last element is ")
print(q.back())


q.display()

q.dequeue()


print("After removing an element")
q.display()
print("The size of the Queue is")
print(q.size())