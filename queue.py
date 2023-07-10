
class Queue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.queue.pop(0)

    def peek(self):
        if self.is_empty():
            return None
        return self.queue[0]

    def size(self):
        return len(self.queue)


queue = Queue()
queue.enqueue('A')
queue.enqueue('B')
queue.enqueue('C')
print(queue.dequeue())  # Output: A
print(queue.peek())  # Output: B
print(queue.size())  # Output: 2
