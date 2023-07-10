class s:
    def __init__(self):
        self.s = []

    def is_empty(self):
        return len(self.s) == 0

    def push(self, item):
        self.s.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.s.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.s[-1]

    def size(self):
        return len(self.s)


s= s()
s.push(1)
s.push(2)
s.push(9)
s.push(5)
s.push(7)
s.push(3)
print(s.pop())  # Output: 3
print(s.peek())  # Output: 2
print(s.size())  # Output: 2
