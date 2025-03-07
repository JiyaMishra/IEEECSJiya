class MyStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []
        self.max_stack = []
    def push(self, x):
        self.stack.append(x)
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)
        if not self.max_stack or x >= self.max_stack[-1]:
            self.max_stack.append(x)
    def pop(self):
        if not self.stack:
            return None
        popped_element = self.stack.pop()
        if popped_element == self.min_stack[-1]:
            self.min_stack.pop()
        if popped_element == self.max_stack[-1]:
            self.max_stack.pop()
    def top(self):
        if not self.stack:
            return None
        return self.stack[-1]
    def getMin(self):
        if not self.min_stack:
            return None
        return self.min_stack[-1]
    def getMax(self):
        if not self.max_stack:
            return None
        return self.max_stack[-1]
stack = MyStack()
stack.push(5)
stack.push(3)
stack.push(7)
stack.push(1)
stack.push(6)
print("Top of stack:", stack.top())
print("Min element:", stack.getMin())
print("Max element:", stack.getMax())
stack.pop()
print("\nAfter popping:")
print("Top of stack:", stack.top())
print("Min element:", stack.getMin())
print("Max element:", stack.getMax())
stack.pop()
stack.pop()
stack.pop()
stack.pop()
print("\nAfter popping all elements:")
print("Top of stack:", stack.top())
print("Min element:", stack.getMin())
print("Max element:", stack.getMax())
