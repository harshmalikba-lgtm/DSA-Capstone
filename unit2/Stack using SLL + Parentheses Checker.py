# Node class for Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Stack implementation using Singly Linked List
class Stack:
    def __init__(self):
        self.top = None

    # Push operation
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    # Pop operation
    def pop(self):
        if self.is_empty():
            return None   # Underflow handling
        popped = self.top.data
        self.top = self.top.next
        return popped

    # Peek operation
    def peek(self):
        if self.is_empty():
            return None
        return self.top.data

    # Check if stack is empty
    def is_empty(self):
        return self.top is None


# Function to check balanced parentheses
def is_balanced(string):
    stack = Stack()
    pairs = {')': '(', '}': '{', ']': '['}

    for char in string:
        # If opening bracket → push
        if char in "({[":
            stack.push(char)

        # If closing bracket
        elif char in ")}]":
            if stack.is_empty():
                return False
            top = stack.pop()
            if pairs[char] != top:
                return False

    # Final check: stack should be empty
    return stack.is_empty()


# ---- Testing ----
test_strings = [
    "{[()]}",   # True
    "([)]",     # False
    "((()))",   # True
    "{[(])}",   # False
    "",         # True (empty string)
]

for s in test_strings:
    print(f"Input: {s} -> Output: {is_balanced(s)}")