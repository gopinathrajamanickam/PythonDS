# Implment a Stack in Python

# The default data structure list can be used as Stack
# A Stack data structure implements LIFO 
# Key functions
#  getSize()
#  isEmpty()
#  push()
#  pop()
#  peek()
#  __str__() 

class Stack:
    def __init__(self):
        self.stack = []
    def getSize(self):
        return len(self.stack)
    def isEmpty(self):
        return len(self.stack) == 0
    def push(self,item):
        self.stack.append(item)
    def pop(self):
        self.stack.pop()
    def peek(self):
        return self.stack[-1]
    def __str__(self):
        return str(self.stack)

if __name__ =="__main__":
    s = Stack()
    print(s.isEmpty())
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    print(s)
    s.pop()
    print(s)
    print(s.peek())
    print(s)
    
