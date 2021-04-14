# Implementing a Queue in Python

# A Queue is a data structure that follows FIFO principle
# Main methods involved are
# enqueue
# dequeue
# getSize
# isEmpty 
class Queue:
    def __init__(self):
        self.items = []
    def getSize(self):
        return len(self.items)
    def isEmpty(self):
        return len(self.items) > 0
    def enqueue(self, item):
        self.items.insert(0,item)
    def dequeue(self):
        self.items.pop()
    def __str__(self):
        return str(self.items)
        
if __name__ == "__main__":
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    print(q)
    while( q.getSize() > 0 ):
        q.dequeue()
        print(q)

    print(q)
    
    
