#1
class Stack():
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return self.items == []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        last = len(self.items) - 1
        return self.items[last]
    
    def size(self):
        return len(self.items)

stack = Stack()
for c in "yesterday":
    stack.push(c)

reverse = ""

for i in range (len(stack.items)):
    reverse += stack.pop()

print(reverse)

#2
class Stack():
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return self.items == []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        last = len(self.items) - 1
        return self.items[last]
    
    def size(self):
        return len(self.items)

stack_two = Stack()

for i in range(1,6):
    stack.push(i)

reversed_list = []

for j in range(len(stack.items)):
    reversed_list.append(stack.pop())

print(reversed_list)
