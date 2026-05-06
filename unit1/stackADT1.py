class StackADT:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if self.isEmpty():
            return None  # Safe underflow
        return self.items.pop()
    
    def peek(self):
        if self.isEmpty():
            return None
        return self.items[-1]
    
    def isEmpty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)

# Demo: Store recursion steps (e.g., factorial trace)
stack = StackADT()
stack.push('fact(3)')
stack.push('fact(2)')
stack.push('fact(1)')
print(stack.pop())  # fact(1)
print(stack.size())  # 2
print(stack.peek())  # fact(2)
